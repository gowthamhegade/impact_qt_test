# -*- coding: utf-8 -*-

import names


def main():
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "hi,")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "hello how are you?")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Shift+Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "I am good")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 104, 44, -109, 0, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Color_QToolButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray), 38, 78, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.select_Color_OK_QPushButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 241, 167, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 60, 75, -62, -3, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Color_QToolButton))
    mouseClick(waitForObject(names.basic_colors_QtPrivate_QWellArray), 205, 35, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.select_Color_OK_QPushButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 29, 10, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 19, 13, -24, -4, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 236, 101, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))
