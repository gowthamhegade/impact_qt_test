import os, subprocess, database, shutil
tst_folders = [folder for folder in os.listdir(database.TEST_SCRIPTS_PATH) if os.path.isdir(os.path.join(database.TEST_SCRIPTS_PATH, folder)) and folder.startswith("tst_")]
print(tst_folders)
for test_case in tst_folders:
    test_cases_path = database.TEST_SCRIPTS_PATH
    exe_command = f"squishrunner --testsuite {test_cases_path} --testcase {test_case}"
    report_command = f"cmreport --csmes={database.EXECUTABLE_PATH}.csmes --csv-excel={test_case}.csv"
    try:
        subprocess.run(exe_command, shell=True, check=True)
        subprocess.run(report_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running test cases {test_case}: {e}")
for test_case in tst_folders:
    shutil.move(f"{test_case}.csv", f"data/{test_case}.csv")
    