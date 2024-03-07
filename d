[1mdiff --cc .gitattributes[m
[1mindex 1d3953f,1d3953f..b81595d[m
[1m--- a/.gitattributes[m
[1m+++ b/.gitattributes[m
[36m@@@ -1,1 -1,1 +1,3 @@@[m
[31m--*.cpp diff=cpp[m
[32m++*.cpp diff=cpp[m
[32m++*.c diff=cpp[m
[32m++*.h diff=cpp[m
[1mdiff --cc .gitignore[m
[1mindex 24b331e,24b331e..47b8806[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@@ -3,3 -3,3 +3,5 @@@[m [mtextedit/build-textedit_v1-Desktop_Qt_6[m
  impactbasedtesting/ScriptGeneration_202401191029/*[m
  impactbasedtesting/results/git_changes/changes.xlsx[m
  dummy.ipynb[m
[32m++*.xlsx[m
[32m++impactbasedtesting/database.py[m
[1mdiff --cc .ipynb_checkpoints/dummy-checkpoint.ipynb[m
[1mindex 0000000,0000000..7e0f7b5[m
[1mnew file mode 100644[m
[1m--- /dev/null[m
[1m+++ b/.ipynb_checkpoints/dummy-checkpoint.ipynb[m
[36m@@@ -1,0 -1,0 +1,153 @@@[m
[32m++{[m
[32m++ "cells": [[m
[32m++  {[m
[32m++   "cell_type": "code",[m
[32m++   "execution_count": 5,[m
[32m++   "metadata": {},[m
[32m++   "outputs": [[m
[32m++    {[m
[32m++     "name": "stdout",[m
[32m++     "output_type": "stream",[m
[32m++     "text": [[m
[32m++      "testting diff --git a/textedit/textedit_v1/textedit.cpp b/textedit/textedit_v1/textedit.cpp\n",[m
[32m++      "index 9e0893d..71f525e 100644\n",[m
[32m++      "--- a/textedit/textedit_v1/textedit.cpp\n",[m
[32m++      "+++ b/textedit/textedit_v1/textedit.cpp\n",[m
[32m++      "@@ -58,6 +58,7 @@ const QString rsrcPath = \":/images\";\n",[m
[32m++      "    setCentralWidget(textEdit);\n",[m
[32m++      "    textEdit->setFocus();\n",[m
[32m++      "    setCurrentFileName(QString());\n",[m
[32m++      "+   cout<<\"hello\";\n",[m
[32m++      " \n",[m
[32m++      "    fontChanged(textEdit->font());\n",[m
[32m++      "    colorChanged(textEdit->textColor());\n",[m
[32m++      "\n"[m
[32m++     ][m
[32m++    },[m
[32m++    {[m
[32m++     "data": {[m
[32m++      "text/plain": [[m
[32m++       "{'textedit.cpp': ['\":/images\";']}"[m
[32m++      ][m
[32m++     },[m
[32m++     "execution_count": 5,[m
[32m++     "metadata": {},[m
[32m++     "output_type": "execute_result"[m
[32m++    }[m
[32m++   ],[m
[32m++   "source": [[m
[32m++    "\n",[m
[32m++    "\n",[m
[32m++    "def git_diff(repo_path, path, start_commit):\n",[m
[32m++    "    \n",[m
[32m++    "    repo = git.Repo(repo_path)\n",[m
[32m++    "    # end_commit = repo.head.object.hexsha\n",[m
[32m++    "    end_commit = 'be909fa7ea7f33a222a52867fa7a8808c7b3a358'\n",[m
[32m++    "    commit_a = repo.commit(start_commit)\n",[m
[32m++    "    commit_b = repo.commit(end_commit)\n",[m
[32m++    "    \n",[m
[32m++    "    diff_output = ''\n",[m
[32m++    "    command = ['git','diff',f'{commit_a}', f'{commit_b}']\n",[m
[32m++    "\n",[m
[32m++    "    try:\n",[m
[32m++    "        diff_output = subprocess.run(command, cwd=repo_path, capture_output=True, text=True, check=True).stdout\n",[m
[32m++    "    except subprocess.CalledProcessError as e:\n",[m
[32m++    "        print(f\"Error executing git diff: {e}\")\n",[m
[32m++    "    print('testting', diff_output)\n",[m
[32m++    "    diff_info = diff_output.split(\"\\ndiff --git\")\n",[m
[32m++    "    diff_info = [part.strip() for part in diff_info if part.strip()]\n",[m
[32m++    "\n",[m
[32m++    "    def git_changes(git_diff_output):\n",[m
[32m++    "        changes={}\n",[m
[32m++    "        diff_line = git_diff_output.splitlines()\n",[m
[32m++    "        for line in diff_line:\n",[m
[32m++    "            if line.startswith('diff --git') or line.startswith('a/'):\n",[m
[32m++    "                start_index = line.find('a/') \n",[m
[32m++    "                end_index = line.find(' b/', start_index)\n",[m
[32m++    "                file_name = line[start_index:end_index].split('/')[-1]\n",[m
[32m++    "                chunk_headers = [line for line in diff_line if line.startswith(\"@@\")]\n",[m
[32m++    "                method_names = set()\n",[m
[32m++    "                for header in chunk_headers:\n",[m
[32m++    "                    parts = header.split(\"@@\")[-1].strip().split(\"(\")[0]\n",[m
[32m++    "                    method_names.add(parts.split(' ')[-1])\n",[m
[32m++    "                changes[file_name] = list(method_names)\n",[m
[32m++    "        return changes\n",[m
[32m++    "\n",[m
[32m++    "    final_changes = {}\n",[m
[32m++    "    \n",[m
[32m++    "    for ele in diff_info:\n",[m
[32m++    "        changes = git_changes(ele)\n",[m
[32m++    "        final_changes.update(changes)\n",[m
[32m++    "    df_changes = pd.DataFrame([(file,method) for file, methods in final_changes.items() for method in methods], columns=['File_Name','Methods'])\n",[m
[32m++    "    git_changes_path = os.path.join(path,\"git_changes\")\n",[m
[32m++    "    if not os.path.exists(git_changes_path):\n",[m
[32m++    "        os.makedirs(git_changes_path)\n",[m
[32m++    "    with pd.ExcelWriter(os.path.join(git_changes_path,\"changes.xlsx\")) as w:\n",[m
[32m++    "        df_changes.to_excel(w)\n",[m
[32m++    "    \n",[m
[32m++    "    return final_changes\n",[m
[32m++    "\n",[m
[32m++    "# import impa/database\n",[m
[32m++    "repo_path               = \"C:\\\\Users\\\\Dell\\\\Documents\\\\qtcc\\\\GitHub\\\\impact_qt_test\"\n",[m
[32m++    "#executable_path         = database.EXECUTABLE_PATH\n",[m
[32m++    "#test_scripts_path       = database.TEST_SCRIPTS_PATH\n",[m
[32m++    "result_path             = repo_path + \"\\\\impactbasedtesting\\\\results\"\n",[m
[32m++    "start_commit            = \"a647b7501523c048926b27382ae636bdee623434\"\n",[m
[32m++    "(git_diff(repo_path, result_path, start_commit))\n"[m
[32m++   ][m
[32m++  },[m
[32m++  {[m
[32m++   "cell_type": "code",[m
[32m++   "execution_count": 2,[m
[32m++   "metadata": {},[m
[32m++   "outputs": [],[m
[32m++   "source": [[m
[32m++    "import git\n",[m
[32m++    "import subprocess\n",[m
[32m++    "import os\n",[m
[32m++    "import glob\n",[m
[32m++    "import pandas as pd"[m
[32m++   ][m
[32m++  },[m
[32m++  {[m
[32m++   "cell_type": "code",[m
[32m++   "execution_count": 1,[m
[32m++   "metadata": {},[m
[32m++   "outputs": [[m
[32m++    {[m
[32m++     "name": "stdout",[m
[32m++     "output_type": "stream",[m
[32m++     "text": [[m
[32m++      "Requirement already satisfied: GitPython in c:\\users\\dell\\documents\\qtcc\\github\\impact_qt_test\\impactbasedtesting\\impact\\lib\\site-packages (3.1.42)\n",[m
[32m++      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\dell\\documents\\qtcc\\github\\impact_qt_test\\impactbasedtesting\\impact\\lib\\site-packages (from GitPython) (4.0.11)\n",[m
[32m++      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\dell\\documents\\qtcc\\github\\impact_qt_test\\impactbasedtesting\\impact\\lib\\site-packages (from gitdb<5,>=4.0.1->GitPython) (5.0.1)\n"[m
[32m++     ][m
[32m++    }[m
[32m++   ],[m
[32m++   "source": [[m
[32m++    "!pip install GitPython"[m
[32m++   ][m
[32m++  }[m
[32m++ ],[m
[32m++ "metadata": {[m
[32m++  "kernelspec": {[m
[32m++   "display_name": "Python 3 (ipykernel)",[m
[32m++   "language": "python",[m
[32m++   "name": "python3"[m
[32m++  },[m
[32m++  "language_info": {[m
[32m++   "codemirror_mode": {[m
[32m++    "name": "ipython",[m
[32m++    "version": 3[m
[32m++   },[m
[32m++   "file_extension": ".py",[m
[32m++   "mimetype": "text/x-python",[m
[32m++   "name": "python",[m
[32m++   "nbconvert_exporter": "python",[m
[32m++   "pygments_lexer": "ipython3",[m
[32m++   "version": "3.12.2"[m
[32m++  }[m
[32m++ },[m
[32m++ "nbformat": 4,[m
[32m++ "nbformat_minor": 4[m
[32m++}[m
[1mdiff --cc impactbasedtesting/database.py[m
[1mindex 256943a,256943a..b8e031b[m
[1m--- a/impactbasedtesting/database.py[m
[1m+++ b/impactbasedtesting/database.py[m
[36m@@@ -3,4 -3,4 +3,4 @@@[m [mRESULT_PATH = REPO_PATH + "\\impactbase[m
  EXECUTABLE_PATH = REPO_PATH + "\\textedit\\textedit_v1\\textedit.exe"[m
  # TEST_SCRIPTS_PATH = REPO_PATH + "\\impactbasedtesting\\ScriptGeneration_202401191029\\AlgoAFScript_202401191029"[m
  TEST_SCRIPTS_PATH = REPO_PATH + "\\textedit\\suite_TextEditSuite"[m
[31m--START_COMMIT = "2f8276d3df9e305b0a09fdce4927ba886335b6b8"[m
[32m++START_COMMIT = "a647b7501523c048926b27382ae636bdee623434"[m
[1mdiff --cc impactbasedtesting/results/git_changes/changes.xlsx[m
[1mindex 283fd68,283fd68..8eeca90[m
Binary files differ
[1mdiff --cc impactbasedtesting/test.py[m
[1mindex 95046bb,95046bb..d816042[m
[1m--- a/impactbasedtesting/test.py[m
[1m+++ b/impactbasedtesting/test.py[m
[36m@@@ -1,23 -1,23 +1,44 @@@[m
[31m--import os[m
[31m--import re[m
[32m++import pygit2[m
[32m++from difflib import unified_diff[m
  [m
[31m--def extract_tags(directory_path):[m
[31m--    def remove_prefix(prefix, folders):[m
[31m--        return [folder[len(prefix):] if folder.startswith(prefix) else folder for folder in folders][m
[32m++def get_function_diff(repo_path, old_commit, new_commit):[m
[32m++    repo = pygit2.Repository(repo_path)[m
  [m
[31m--    all_items = os.listdir(directory_path)[m
[31m--    folders = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))][m
[31m--    pattern = re.compile(r'^tst_')[m
[31m--    selected_folders = [folder for folder in folders if pattern.match(folder)][m
[32m++    function_diff = [][m
  [m
[31m--    if "tst_":[m
[31m--        selected_folders = remove_prefix("tst_", selected_folders)[m
[32m++    for entry in repo.walk(repo.revparse_single(old_commit).oid, pygit2.GIT_SORT_TOPOLOGICAL):[m
[32m++        old_blob = entry.tree[m
[32m++        new_blob = repo[new_commit].tree[m
  [m
[31m--    return selected_folders[m
[32m++        for old_entry, new_entry in zip(old_blob, new_blob):[m
[32m++            if old_entry.type == pygit2.GIT_OBJ_BLOB and old_entry.name.endswith('.cpp'):[m
[32m++                old_content = repo[old_entry.id].data.decode('utf-8')[m
[32m++                new_content = repo[new_entry.id].data.decode('utf-8')[m
  [m
[31m--# Example usage:[m
[31m--directory_path = "C:/Users/Dell/Documents/qtcc/GitHub/impact_qt_test/textedit/suite_TextEditSuite"[m
[32m++                # Compute unified diff[m
[32m++                diff = unified_diff(old_content.splitlines(), new_content.splitlines(), lineterm='')[m
  [m
[31m--selected_folders = extract_tags(directory_path)[m
[32m++                # Extract function-level changes[m
[32m++                in_function = False[m
[32m++                for line in diff:[m
[32m++                    if line.startswith("@@"):[m
[32m++                        in_function = True[m
[32m++                        function_diff.append(line)[m
[32m++                    elif in_function and (line.startswith("-") or line.startswith("+")):[m
[32m++                        function_diff.append(line)[m
[32m++                    elif in_function and line.startswith(" "):[m
[32m++                        break[m
[32m++                    elif in_function and not line.startswith("@@"):[m
[32m++                        in_function = False[m
  [m
[31m--print(selected_folders)[m
[32m++    return '\n'.join(function_diff)[m
[32m++[m
[32m++[m
[32m++# Example usage[m
[32m++repo_path = "C:\\Users\\Dell\\Documents\\qtcc\\GitHub\\impact_qt_test"[m
[32m++old_commit = 'a647b7501523c048926b27382ae636bdee623434'[m
[32m++new_commit = 'be909fa7ea7f33a222a52867fa7a8808c7b3a358'[m
[32m++file_path = 'path/to/your/file.cpp'[m
[32m++[m
[32m++result = get_function_diff(repo_path, old_commit, new_commit)[m
[32m++print(result)[m
