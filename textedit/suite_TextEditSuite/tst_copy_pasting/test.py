# -*- coding: utf-8 -*-

import names


def main():
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "hi,")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "this is a ")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Backspace>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "t")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Backspace>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), " test case about copy pasting.")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 207, 63, -207, -4, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Copy_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 242, 56, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Paste_QToolButton))
    sendEvent("QMoveEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit), 49, 61, 314, 87)
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))
