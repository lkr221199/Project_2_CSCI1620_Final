class InsulinCalc:
    def __init__(self):
        self.current_blood_sugar = None
        self.target_blood_sugar = None
        self.correction_factor = None
        self.ratio = None
        self.total_carbs = None
        self.bolus = None
        self.correction_dose = None
        self.total_insulin_dose = None

    def get_calc_info(self, current_blood_sugar, target_blood_sugar, correction_factor, ratio, total_carbs):
        return

    def calculate_bolus(self, total_carb, ratio):
        self.bolus = self.total_carbs * self.ratio
        return self.bolus

    def calculate_correction(self, current_blood_sugar, target_blood_sugar, correction_factor):
        self.correction_dose = (self.current_blood_sugar - self.target_blood_sugar) / self.correction_factor
        return self.correction_dose

    def calculate_total_dose(self, bolus, correction_dose):
        self.total_insulin_dose = self.bolus + self.correction_dose
        return self.total_insulin_dose

    def __str__(self):
        return f'Current Blood Sugar = {self.current_blood_sugar} ' \
               f'\nTarget Blood Sugar = {self.target_blood_sugar} ' \
               f'\nCorrection Factor = {self.correction_factor} ' \
               f'\nRatio = {self.ratio} ' \
               f'\nTotal Carbs = = {self.total_carbs} ' \
               f'\nBolus = {self.bolus} ' \
               f'\nCorrection Dose = {self.correction_dose} ' \
               f'\nTotal Dose (Bolus + Correction) = {self.total_insulin_dose} Units'
