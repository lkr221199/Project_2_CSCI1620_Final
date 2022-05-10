from PyQt5.QtWidgets import *
from view_Project_2 import Ui_MainWindow
import Insulin_Calc


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_submit_user_info.clicked.connect(lambda: self.set_user_info())
        self.button_submit_food_info.clicked.connect(lambda: self.set_food_info())
        self.button_calculate_insulin_dose.clicked.connect(lambda: self.calculate())

    def update_display_setup_tab(self):
        pass

    def update_display_main_tab(self):
        pass

    def calculate(self):
        current_blood_sugar = self.textEnter_current_blood_sugar()
        total_carbs = self.textEnter_total_carbs()
        ratio = self.textEnter_ratio()
        insulin_dose = Insulin_Calc.InsulinDose(current_blood_sugar, total_carbs, ratio)

    def set_user_info(self):
        name = self.textEnter_user_name.text()
        age = self.textEnter_user_age.text()
        weight = self.textEnter_user_weight.text()
        correction_factor = self.textEnter_user_correction_factor.text()
        target_blood_sugar = self.textEnter_user_blood_sugar_target.text()
        user = Insulin_Calc.User(name, age, weight, correction_factor, target_blood_sugar)

    def set_food_info(self):
        food = self.textEnter_food.text()
        serv_size = self.textEnter_serv_size.text()
        carbs_per_serv = self.textEnter_carbs_per_serv.text()
        food = Insulin_Calc.Food(food, serv_size, carbs_per_serv)



