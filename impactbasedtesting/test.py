import os, database, re


def extract_tags(directory_path):
    def remove_prefix(prefix, folders):
        return [folder[len(prefix):] if folder.startswith(prefix) else folder for folder in folders]

    all_items = os.listdir(directory_path)
    folders = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))]
    pattern = re.compile(r'^tst_')
    selected_folders = [folder for folder in folders if pattern.match(folder)]

    if "tst_":
        selected_folders = remove_prefix("tst_", selected_folders)
    print('sss',selected_folders)
    return selected_folders


s= extract_tags(database.TEST_SCRIPTS_PATH)
for i in s:
    print(i)