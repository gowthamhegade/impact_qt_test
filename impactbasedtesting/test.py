import pygit2
from difflib import unified_diff

def get_function_diff(repo_path, old_commit, new_commit):
    repo = pygit2.Repository(repo_path)

    function_diff = []

    for entry in repo.walk(repo.revparse_single(old_commit).oid, pygit2.GIT_SORT_TOPOLOGICAL):
        old_blob = entry.tree
        new_blob = repo[new_commit].tree

        for old_entry, new_entry in zip(old_blob, new_blob):
            if old_entry.type == pygit2.GIT_OBJ_BLOB and old_entry.name.endswith('.cpp'):
                old_content = repo[old_entry.id].data.decode('utf-8')
                new_content = repo[new_entry.id].data.decode('utf-8')

                # Compute unified diff
                diff = unified_diff(old_content.splitlines(), new_content.splitlines(), lineterm='')

                # Extract function-level changes
                in_function = False
                for line in diff:
                    if line.startswith("@@"):
                        in_function = True
                        function_diff.append(line)
                    elif in_function and (line.startswith("-") or line.startswith("+")):
                        function_diff.append(line)
                    elif in_function and line.startswith(" "):
                        break
                    elif in_function and not line.startswith("@@"):
                        in_function = False

    return '\n'.join(function_diff)


# Example usage
repo_path = "C:\\Users\\Dell\\Documents\\qtcc\\GitHub\\impact_qt_test"
old_commit = 'a647b7501523c048926b27382ae636bdee623434'
new_commit = 'be909fa7ea7f33a222a52867fa7a8808c7b3a358'
file_path = 'path/to/your/file.cpp'

result = get_function_diff(repo_path, old_commit, new_commit)
print(result)
