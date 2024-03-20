# -*- coding: utf-8 -*-

import names

def main():
    startApplication("textedit")
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Format"))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Format_QMenu, "Italic"))
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Underline_QToolButton))
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))