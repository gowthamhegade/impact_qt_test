# -*- coding: utf-8 -*-

import names


def main():
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "hi,")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "This is test for copy pasting.")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 152, 44, -149, -5, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Copy_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 68, 102, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Paste_QToolButton))
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "Copy paste completed")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 136, 108, -144, -5, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 296, 132, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))
