import math


class User:
    def __init__(self, name, age, weight, ratio, correction_factor, target_blood_sugar):
        self.name = name
        self.age = age
        self.weight = weight
        self.correction_factor = correction_factor
        self.target_blood_sugar = target_blood_sugar

    def __str__(self):
        return f'Name = {self.name} \nAge = {self.age} \nWeight = {self.weight} \nRatio = {self.ratio} \nCorrection Factor = {self.correction_factor}'


class Food:
    def __init__(self, food_type, serving_size, carbs_per_serving):
        self.food_type = food_type
        self.serving_size = serving_size
        self.carbs_per_serving = carbs_per_serving

    def __str__(self):
        return f'Food: {self.food_type} \nServing Size: {self.serving_size} \n Carbs/Serving: {self.carbs_per_serving}'


class InsulinDose:
    def __init__(self, current_blood_sugar, total_carbs, ratio):
        self.current_blood_sugar = current_blood_sugar
        self.total_carbs = total_carbs
        self.ratio = ratio

    def calculate_total_dose(self):
        pass
