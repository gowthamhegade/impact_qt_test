# -*- coding: utf-8 -*-

import names

def main():
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "Test")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "Test")
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Save_QToolButton))
    clickButton(waitForObject(names.no_file_name_specified_OK_QPushButton))
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))
