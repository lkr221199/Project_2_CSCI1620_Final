# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_Project_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630, 500))
        MainWindow.setMaximumSize(QtCore.QSize(630, 500))
        MainWindow.setStyleSheet("Fusion")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 494))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_main_calculate_insulin = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_main_calculate_insulin.setMinimumSize(QtCore.QSize(570, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_main_calculate_insulin.setFont(font)
        self.label_main_calculate_insulin.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_main_calculate_insulin.setObjectName("label_main_calculate_insulin")
        self.verticalLayout_2.addWidget(self.label_main_calculate_insulin)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_enter_current_blood_sugar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_enter_current_blood_sugar.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_enter_current_blood_sugar.setFont(font)
        self.label_enter_current_blood_sugar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enter_current_blood_sugar.setObjectName("label_enter_current_blood_sugar")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_enter_current_blood_sugar)
        self.label_enter_target_blood_sugar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_enter_target_blood_sugar.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)

        self.textEnter_current_blood_sugar = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEnter_current_blood_sugar.setMinimumSize(QtCore.QSize(400, 20))
        self.textEnter_current_blood_sugar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEnter_current_blood_sugar.setInputMask("")
        self.textEnter_current_blood_sugar.setObjectName("textEnter_current_blood_sugar")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEnter_current_blood_sugar)

        self.label_enter_target_blood_sugar.setFont(font)
        self.label_enter_target_blood_sugar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enter_target_blood_sugar.setObjectName("label_enter_target_blood_sugar")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_enter_target_blood_sugar)

        self.textEnter_target_blood_sugar = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEnter_target_blood_sugar.setMinimumSize(QtCore.QSize(400, 20))
        self.textEnter_target_blood_sugar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEnter_target_blood_sugar.setInputMask("")
        self.textEnter_target_blood_sugar.setObjectName("textEnter_target_blood_sugar")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEnter_target_blood_sugar)

        self.textEnter_correction_factor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEnter_correction_factor.setMinimumSize(QtCore.QSize(400, 20))
        self.textEnter_correction_factor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEnter_correction_factor.setInputMask("")
        self.textEnter_correction_factor.setText("")
        self.textEnter_correction_factor.setObjectName("textEnter_correction_factor")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEnter_correction_factor)

        self.textEnter_ratio = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEnter_ratio.setMinimumSize(QtCore.QSize(400, 20))
        self.textEnter_ratio.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEnter_ratio.setInputMask("")
        self.textEnter_ratio.setObjectName("textEnter_ratio")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEnter_ratio)

        self.label_enter_correction_factor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_enter_correction_factor.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_enter_correction_factor.setFont(font)
        self.label_enter_correction_factor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enter_correction_factor.setObjectName("label_enter_correction_factor")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_enter_correction_factor)
        self.label_enter_ratio = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_enter_ratio.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_enter_ratio.setFont(font)
        self.label_enter_ratio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enter_ratio.setObjectName("label_enter_ratio")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_enter_ratio)
        self.label_enter_total_carbs = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_enter_total_carbs.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_enter_total_carbs.setFont(font)
        self.label_enter_total_carbs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_enter_total_carbs.setObjectName("label_enter_total_carbs")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_enter_total_carbs)
        self.textEnter_total_carbs = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEnter_total_carbs.setMinimumSize(QtCore.QSize(400, 20))
        self.textEnter_total_carbs.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEnter_total_carbs.setStyleSheet("")
        self.textEnter_total_carbs.setInputMask("")
        self.textEnter_total_carbs.setObjectName("textEnter_total_carbs")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEnter_total_carbs)
        self.button_calculate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_calculate.setMinimumSize(QtCore.QSize(75, 25))
        self.button_calculate.setMaximumSize(QtCore.QSize(75, 25))
        self.button_calculate.setObjectName("button_calculate")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.button_calculate)
        self.label_title_results = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_title_results.setMinimumSize(QtCore.QSize(400, 30))
        self.label_title_results.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_title_results.setFont(font)
        self.label_title_results.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_results.setObjectName("label_title_results")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_title_results)
        self.label_update_display_insulin_dose = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_update_display_insulin_dose.setMinimumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_update_display_insulin_dose.setFont(font)
        self.label_update_display_insulin_dose.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_update_display_insulin_dose.setWordWrap(True)
        self.label_update_display_insulin_dose.setObjectName("label_update_display_insulin_dose")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_update_display_insulin_dose)
        self.verticalLayout_2.addLayout(self.formLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.onlyInt = QIntValidator()
        self.textEnter_current_blood_sugar.setValidator(self.onlyInt)
        self.textEnter_target_blood_sugar.setValidator(self.onlyInt)
        self.textEnter_correction_factor.setValidator(self.onlyInt)
        self.textEnter_ratio.setValidator(self.onlyInt)
        self.textEnter_total_carbs.setValidator(self.onlyInt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_main_calculate_insulin.setText(_translate("MainWindow", "Calculate Insulin Dose"))
        self.label_enter_current_blood_sugar.setText(_translate("MainWindow", "Enter Current Blood Sugar:"))
        self.label_enter_target_blood_sugar.setText(_translate("MainWindow", "Enter Target Blood Sugar:"))
        self.textEnter_target_blood_sugar.setPlaceholderText(_translate("MainWindow", "Enter non-zero number (e.g. 120)"))
        self.textEnter_current_blood_sugar.setPlaceholderText(_translate("MainWindow", "Enter non-zero number (e.g. 150)"))
        self.textEnter_correction_factor.setPlaceholderText(_translate("MainWindow", "Enter non-zero number (e.g. 60)"))
        self.textEnter_ratio.setPlaceholderText(_translate("MainWindow", "Enter a non-zero number (ex: if ratio is 1:15, enter 15 only)"))
        self.label_enter_correction_factor.setText(_translate("MainWindow", "Enter Correction Factor:"))
        self.label_enter_ratio.setText(_translate("MainWindow", "Enter Ratio:"))
        self.label_enter_total_carbs.setText(_translate("MainWindow", "Enter Total Carbs:"))
        self.textEnter_total_carbs.setPlaceholderText(_translate("MainWindow", "Enter number (e.g. 85)"))
        self.button_calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_title_results.setText(_translate("MainWindow", "Results:"))
        self.label_update_display_insulin_dose.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Insulin dose: ()</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
