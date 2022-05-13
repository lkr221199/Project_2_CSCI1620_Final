from PyQt5.QtWidgets import *
from view_Project_2 import Ui_MainWindow
from InsulinCalc import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calc = InsulinCalc()
        self.button_calculate.clicked.connect(lambda: self.get_form_data())

    def update_display(self, calc_info):
        # clear form inputs
        self.textEnter_current_blood_sugar.clear()
        self.textEnter_target_blood_sugar.clear()
        self.textEnter_correction_factor.clear()
        self.textEnter_ratio.clear()
        self.textEnter_total_carbs()
        # update label to display total dose
        self.label_update_display_insulin_dose.setText(f'Your total insulin dose is {} Units')

    def get_form_data(self):
        current_blood_sugar = self.textEnter_current_blood_sugar()
        target_blood_sugar = self.textEnter_target_blood_sugar()
        correction_factor = self.textEnter_correction_factor()
        ratio = self.textEnter_ratio()
        total_carbs = self.textEnter_total_carbs()
        form_data = {'current_blood_sugar':current_blood_sugar,
                     'target_blood_sugar':target_blood_sugar,
                     'correction_factor': correction_factor,
                     'ratio':ratio,
                     'total_carbs':total_carbs}
        return form_data

