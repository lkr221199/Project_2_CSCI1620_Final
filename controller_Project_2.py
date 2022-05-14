from PyQt5.QtWidgets import *
from view_Project_2 import Ui_MainWindow
from InsulinCalc import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args: object, **kwargs: object) -> None:
        """
        Constructor to create initial state of a controller object.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculation = InsulinCalc()
        self.button_calculate.clicked.connect(lambda: self.update_calc())

    def update_calc(self) -> None:
        """
        Method to get data from GUI and populate calculation
        """
        if self.input_is_valid():
            self.calculation.current_blood_sugar = int(self.textEnter_current_blood_sugar.text())
            self.calculation.target_blood_sugar = int(self.textEnter_target_blood_sugar.text())
            self.calculation.correction_factor = int(self.textEnter_correction_factor.text())
            self.calculation.ratio = int(self.textEnter_ratio.text())
            self.calculation.total_carbs = int(self.textEnter_total_carbs.text())
            calc_info = self.calculation.get_calc_info()
            self.update_display(calc_info)

    def input_is_valid(self) -> bool:
        """
        Method to validate user input and prompt if out-of-bounds value is entered or field left blank
        :return: True or False
        """
        fields = [(self.textEnter_current_blood_sugar.text(), 1, 1000),
                  (self.textEnter_target_blood_sugar.text(), 1, 1000),
                  (self.textEnter_correction_factor.text(), 1, 1000),
                  (self.textEnter_ratio.text(), 1, 1000),
                  (self.textEnter_total_carbs.text(), 1, 1000)
                  ]

        for field, min_val, max_val in fields:
            if field == "" or (int(field) < min_val) or (int(field) > max_val):
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setText('Please enter all fields with values between 1 and 10000')
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_()
                return False
        return True

    def update_display(self, calc_info: dict) -> None:
        """
        Method to update GUI display
        :param calc_info:
        """
        # update label to display all info
        self.label_update_display_insulin_dose.setText(f"{self.calculation}")
        # clear form inputs
        self.textEnter_current_blood_sugar.clear()
        self.textEnter_target_blood_sugar.clear()
        self.textEnter_correction_factor.clear()
        self.textEnter_ratio.clear()
        self.textEnter_total_carbs.clear()




