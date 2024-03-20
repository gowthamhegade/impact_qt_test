# -*- coding: utf-8 -*-

import names


def main():
    startApplication("textedit")
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_QMenuBar, "Format", 30147))
    activateItem(waitForObjectItem(names.untitled_txt_Rich_Text_Format_QMenu, "Bold"))
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
