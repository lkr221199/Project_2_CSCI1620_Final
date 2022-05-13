from PyQt5.QtWidgets import *
from view_Project_2 import Ui_MainWindow
from InsulinCalc import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculate = InsulinCalc()
        self.button_calculate.clicked.connect(lambda: self.update_calc())

    def update_calc(self):
        current_blood_sugar = self.textEnter_current_blood_sugar()
        target_blood_sugar = self.textEnter_target_blood_sugar()
        correction_factor = self.textEnter_correction_factor()
        ratio = self.textEnter_ratio()
        total_carbs = self.textEnter_total_carbs()

        self.calculate.current_blood_sugar = int(current_blood_sugar)
        self.calculate.target_blood_sugar = int(target_blood_sugar)
        self.calculate.correction_factor = int(correction_factor)
        self.calculate.ratio = int(ratio)
        self.calculate.total_carbs = int(total_carbs)
        calc_info = self.calculate.get_calc_info()
        self.update_display(calc_info)

    def update_display(self, calc_info):
        # clear form inputs
        self.textEnter_current_blood_sugar.clear()
        self.textEnter_target_blood_sugar.clear()
        self.textEnter_correction_factor.clear()
        self.textEnter_ratio.clear()
        self.textEnter_total_carbs.clear()

        # update label to display total dose
        self.label_update_display_insulin_dose.setText(f"Your total dose is {calc_info['total_insulin_dose']} Units")

