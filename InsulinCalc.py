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

    def calculate_bolus(self):
        self.bolus = self.total_carbs / self.ratio

    def calculate_correction(self):
        self.correction_dose = (self.current_blood_sugar - self.target_blood_sugar) / self.correction_factor
        if self.correction_dose < 0:
            self.correction_dose = 0

    def calculate_total_dose(self):
        self.calculate_bolus()
        self.calculate_correction()
        self.total_insulin_dose = self.bolus + self.correction_dose

    def get_calc_info(self):
        self.calculate_total_dose()
        # Total dose should be rounded to the nearest whole unit
        round(self.total_insulin_dose)
        if self.current_blood_sugar is None or self.target_blood_sugar is None or self.correction_factor is None or self.ratio is None or self.total_carbs is None:
            raise ValueError

        else:
            return {'current_blood_sugar': self.current_blood_sugar,
                    'target_blood_sugar': self.current_blood_sugar,
                    'correction_factor': self.correction_factor,
                    'ratio': self.ratio,
                    'total_carbs': self.total_carbs,
                    'bolus': self.bolus,
                    'correction_dose': self.correction_dose,
                    'total_insulin_dose': self.total_insulin_dose}

    def __str__(self):
        return f'Current Blood Sugar = {self.current_blood_sugar} ' \
               f'\nTarget Blood Sugar = {self.target_blood_sugar} ' \
               f'\nCorrection Factor = {self.correction_factor} ' \
               f'\nRatio = {self.ratio} ' \
               f'\nTotal Carbs = {self.total_carbs} ' \
               f'\nBolus = {self.bolus} ' \
               f'\nCorrection Dose = {self.correction_dose} ' \
               f'\n ' \
               f'\nTotal Dose (Bolus + Correction) = {self.total_insulin_dose:.0f} Units'


def main():
    calculate = InsulinCalc()
    calculate.get_calc_info()
    print(calculate)


if __name__ == '__main__':
    main()
