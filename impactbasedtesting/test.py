import subprocess

def get_function_changes(diff_content):
    """
    Extract function-level changes from the unified diff content.
    """
    function_changes = []
    current_function = None

    for line in diff_content:
        if line.startswith("@@"):
            # Start of a new hunk
            current_function = line[3:].strip()
        elif current_function is not None:
            # Collect lines within the current function
            current_function += line

            # Check for the end of the function block
            if line.startswith("@@"):
                function_changes.append(current_function)
                current_function = None

    return function_changes

def get_git_diff_with_functions(repo_path, commit_hash1, commit_hash2, file_extension=".cpp"):
    # Get the list of changed files between the two commits
    changed_files_cmd = f"git diff --name-only {commit_hash1} {commit_hash2}"
    changed_files_output = subprocess.check_output(changed_files_cmd, shell=True).decode("utf-8")
    changed_files = changed_files_output.strip().split('\n')
    
    # Filter files based on the specified file extension (e.g., .cpp)
    cpp_files = [file for file in changed_files if file.endswith(file_extension)]
    
    # Get the diff for each C++ file along with function-level changes
    file_diffs = {}
    for cpp_file in cpp_files:
        diff_content_cmd = f"git diff {commit_hash1} {commit_hash2} {cpp_file}"
        diff_content_output = subprocess.check_output(diff_content_cmd, shell=True).decode("utf-8")
        diff_content = diff_content_output.strip().split('\n')
        function_changes = get_function_changes(diff_content)
        file_diffs[cpp_file] = function_changes
    
    return file_diffs

def print_function_changes(file_diffs):
    for cpp_file, function_changes in file_diffs.items():
        print(f"Function-level changes for {cpp_file}:")
        for change in function_changes:
            print("\n".join(change.split("\n")[2:]))

# Example usage
repo_path = "C:\\Users\\Dell\\Documents\\qtcc\\GitHub\\impact_qt_test"
commit_hash1 = "a647b7501523c048926b27382ae636bdee623434"
commit_hash2 = "be909fa7ea7f33a222a52867fa7a8808c7b3a358"

cpp_file_diffs = get_git_diff_with_functions(repo_path, commit_hash1, commit_hash2)

# Print the detailed function-level changes for each C++ file
print_function_changes(cpp_file_diffs)



