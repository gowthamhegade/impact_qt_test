
# -*- coding: utf-8 -*-

import names

def main():
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "Test")
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_File_QMenu, "Open..."))
    clickButton(waitForObject(names.qFileDialog_Cancel_QPushButton))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "File"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_File_QMenu, "Save"))
    clickButton(waitForObject(names.no_file_name_specified_OK_QPushButton))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Edit_QMenu, "Undo"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Edit"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Edit_QMenu, "Redo"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Format"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Format_QMenu, "Bold"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Format"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Format_QMenu, "Italic"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Format"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Format_QMenu, "Underline"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Help"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Help_QMenu, "About"))
    clickButton(waitForObject(names.about_OK_QPushButton))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Help"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Help_QMenu, "About Qt"))
    clickButton(waitForObject(names.about_Qt_OK_QPushButton))
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))
