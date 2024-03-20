copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_LaunchApplication
cmcsexeimport -m textedit.exe.csmes -t test_case1 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case1.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"

copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_RibbonContents
cmcsexeimport -m textedit.exe.csmes -t test_case2 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case2.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"

copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_SaveFile
cmcsexeimport -m textedit.exe.csmes -t test_case3 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case3.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"

copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_testFour
cmcsexeimport -m textedit.exe.csmes -t test_case4 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case4.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"

copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_testFive
cmcsexeimport -m textedit.exe.csmes -t test_case5 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case5.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"

copy /y "C:\TextEditNew\coco\textedit\cmscexe" "C:\TextEditNew\coco\textedit\textedit_v1"
copy /y "C:\TextEditNew\coco\textedit\release" "C:\TextEditNew\coco\textedit\textedit_v1\release"
squishrunner --testsuite C:\Users\Dell\Documents\qtcc\GitHub\impact_qt_test\textedit\suite_TextEditSuite --testcase tst_testSix
cmcsexeimport -m textedit.exe.csmes -t test_case6 -f 1 textedit.exe.csexe
cmreport --csmes=textedit.exe.csmes --csv-excel=test_case6.csv
del "C:\TextEditNew\coco\textedit\textedit_v1\textedit.exe.csexe"