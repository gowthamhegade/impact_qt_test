import git
import subprocess
import os
import glob
import pandas as pd

def git_diff(repo_path, path, start_commit):
    
    repo = git.Repo(repo_path)
    end_commit = repo.head.object.hexsha

    commit_a = repo.commit(start_commit)
    commit_b = repo.commit(end_commit)
    
    diff_output = ''
    command = ['git','diff',f'{commit_a}', f'{commit_b}']

    try:
        diff_output = subprocess.run(command, cwd=repo_path, capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing git diff: {e}")
        
    diff_info = diff_output.split("\ndiff --git")
    diff_info = [part.strip() for part in diff_info if part.strip()]

    def git_changes(git_diff_output):
        changes={}
        diff_line = git_diff_output.splitlines()
        for line in diff_line:
            if line.startswith('diff --git') or line.startswith('a/'):
                start_index = line.find('a/') 
                end_index = line.find(' b/', start_index)
                file_name = line[start_index:end_index].split('/')[-1]
                chunk_headers = [line for line in diff_line if line.startswith("@@")]
                method_names = set()
                for header in chunk_headers:
                    parts = header.split("@@")[-1].strip().split("(")[0]
                    method_names.add(parts.split(' ')[-1])
                changes[file_name] = list(method_names)
        return changes

    final_changes = {}
    
    for ele in diff_info:
        changes = git_changes(ele)
        final_changes.update(changes)
    df_changes = pd.DataFrame([(file,method) for file, methods in final_changes.items() for method in methods], columns=['File_Name','Methods'])
    git_changes_path = os.path.join(path,"git_changes")
    if not os.path.exists(git_changes_path):
        os.makedirs(git_changes_path)
    with pd.ExcelWriter(os.path.join(git_changes_path,"changes.xlsx")) as w:
        df_changes.to_excel(w)
    
    return final_changes

import database
repo_path               = database.REPO_PATH
executable_path         = database.EXECUTABLE_PATH
test_scripts_path       = database.TEST_SCRIPTS_PATH
result_path             = database.RESULT_PATH
start_commit            = database.START_COMMIT
print(git_diff(repo_path, result_path, start_commit))


def recommend_test_cases(coverage_path,final_changes):
    df_temp_list = []
    all_files = os.listdir(coverage_path)
    all_reports = [file for file in all_files if os.path.splitext(file)[1].lower() == '.xlsx']

    for filename in all_reports:
        df_temp_list.append(pd.read_excel(os.path.join(coverage_path, filename)))
    df_coverage = pd.concat(df_temp_list)
    # print(df_coverage['Coverage_Percentage'])
    
    filtered_df = df_coverage[df_coverage.apply(lambda row: row['File_Name'] in final_changes.keys() and row['Method'] in final_changes[row['File_Name']], axis=1)].reset_index(drop=True)
    # print(filtered_df)
    grouped_df = filtered_df.groupby(['Method'])['Coverage_Percentage'].idxmax()
    # print(grouped_df)
    selected_test_cases = filtered_df.loc[grouped_df]['Scenario'].unique()
    print(selected_test_cases)
    
    return list(selected_test_cases)


# coverage_path = 'C:\\Users\\Dell\\Documents\\qtcc\\GitHub\\impact_qt_test\\impactbasedtesting\\results\\coverage_reports'
# final_changes = git_diff(repo_path,result_path,start_commit)
# recommend_test_cases(coverage_path,final_changes)
