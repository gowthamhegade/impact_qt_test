# -*- coding: utf-8 -*-

import names

def main():
    startApplication("textedit")
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
