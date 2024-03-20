import os, database, re, subprocess


def cli_commands():
    test_cases_path = database.TEST_SCRIPTS_PATH
    executable_path = database.EXECUTABLE_PATH
    textedit_path = database.TEXTEDIT_PATH
    tst_folders = [folder for folder in os.listdir(test_cases_path) if os.path.isdir(os.path.join(test_cases_path)) and folder.startswith("tst_")]
    
    for test_case in tst_folders:
        print('tst', tst_folders)
        copy_release_command = f"copy /y {textedit_path}\\release {textedit_path}\\textedit_v1\\release"
        copy_csexe_command = f"copy /y {textedit_path}\\cmscexe {textedit_path}\\textedit_v1"
        exe_command = f"squishrunner --testsuite {test_cases_path} --testcase {test_case}"
        csexe_command = f"cmcsexeimport -m {executable_path}.csmes -t {test_case} -e {executable_path}.csexe"
        report_command = f"cmreport --csmes={executable_path}.csmes --csv-excel={test_case}.csv"
        delete_csexe_command = f"del {executable_path}.csexe"
        try:
            subprocess.run(copy_release_command, shell=True, check=True)
            subprocess.run(copy_csexe_command, shell=True, check=True)
            subprocess.run(exe_command, shell=True, check=True)
            subprocess.run(csexe_command, shell=True, check=True)
            subprocess.run(report_command, shell=True, check=True)
            subprocess.run(delete_csexe_command, shell=True, check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error running test cases {test_case}: {e}")


cli_commands()
