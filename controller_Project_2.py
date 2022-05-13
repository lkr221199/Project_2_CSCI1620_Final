from PyQt5.QtWidgets import *
from view_Project_2 import Ui_MainWindow
from InsulinCalc import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculation = InsulinCalc()
        self.button_calculate.clicked.connect(lambda: self.update_calc())

    def update_calc(self):
        self.calculation.current_blood_sugar = int(self.textEnter_current_blood_sugar.text())
        self.calculation.target_blood_sugar = int(self.textEnter_target_blood_sugar.text())
        self.calculation.correction_factor = int(self.textEnter_correction_factor.text())
        self.calculation.ratio = int(self.textEnter_ratio.text())
        self.calculation.total_carbs = int(self.textEnter_total_carbs.text())
        calc_info = self.calculation.get_calc_info()
        self.update_display(calc_info)

    def update_display(self, calc_info):
        # update label to display all info
        self.label_update_display_insulin_dose.setText(f"{self.calculation}")
        # clear form inputs
        self.textEnter_current_blood_sugar.clear()
        self.textEnter_target_blood_sugar.clear()
        self.textEnter_correction_factor.clear()
        self.textEnter_ratio.clear()
        self.textEnter_total_carbs.clear()




