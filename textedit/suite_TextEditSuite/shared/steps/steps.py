# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names


@Given("some precondition is met")
def step(context):
    startApplication("textedit")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "hi,")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "<Return>")
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), "bold")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 30, 41, -37, 1, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 79, 41, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), " italic")
    mouseDrag(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 60, 43, -27, 0, 1, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Italic_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 87, 47, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), " underline")
    doubleClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 87, 47, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Underline_QToolButton))
    clickButton(waitForObject(names.untitled_txt_Rich_Text_Bold_QToolButton))
    mouseClick(waitForObject(names.untitled_txt_Rich_Text_Format_Actions_QTextEdit), 281, 101, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
    clickButton(waitForObject(names.application_Discard_QPushButton))

@Given("another precondition")
def step(context):
    startApplication("textedit")
    sendEvent("QCloseEvent", waitForObject(names.untitled_txt_Rich_Text_TextEdit))
