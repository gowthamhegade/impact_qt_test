import os, database, re, subprocess


def cli_commands():
    test_cases_path = database.TEST_SCRIPTS_PATH
    executable_path = database.EXECUTABLE_PATH
    textedit_path = database.TEXTEDIT_PATH
    tst_folders = [folder for folder in os.listdir(test_cases_path) if os.path.isdir(os.path.join(test_cases_path)) and folder.startswith("tst_")]
    
    for test_case in tst_folders:
        print('tst', test_case)


cli_commands()
