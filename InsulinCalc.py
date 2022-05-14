class InsulinCalc:
    def __init__(self) -> None:
        """
        Constructor to create initial state of InsulinCalc object.
        """
        self.current_blood_sugar = None
        self.target_blood_sugar = None
        self.correction_factor = None
        self.ratio = None
        self.total_carbs = None
        self.bolus = None
        self.correction_dose = None
        self.total_insulin_dose = None

    def calculate_bolus(self) -> None:
        """
        Method to calculate bolus dose
        """
        self.bolus = self.total_carbs / self.ratio

    def calculate_correction(self) -> None:
        """
        Method to calculate correction dose
        """
        self.correction_dose = (self.current_blood_sugar - self.target_blood_sugar) / self.correction_factor
        if self.correction_dose < 0:
            self.correction_dose = 0

    def calculate_total_dose(self) -> None:
        """
        Method to calculate total dose. Adds bolus and correction dose
        """
        self.calculate_bolus()
        self.calculate_correction()
        self.total_insulin_dose = self.bolus + self.correction_dose

    def get_calc_info(self) -> dict:
        """
        Method to get all calculation attributes
        :return: Returns dictionary with all calculation attributes
        """
        self.calculate_total_dose()
        return {'current_blood_sugar': self.current_blood_sugar,
                'target_blood_sugar': self.current_blood_sugar,
                'correction_factor': self.correction_factor,
                'ratio': self.ratio,
                'total_carbs': self.total_carbs,
                'bolus': self.bolus,
                'correction_dose': self.correction_dose,
                'total_insulin_dose': round(self.total_insulin_dose)}

    def __str__(self):
        return f'Current Blood Sugar = {self.current_blood_sugar} ' \
               f'\nTarget Blood Sugar = {self.target_blood_sugar} ' \
               f'\nCorrection Factor = {self.correction_factor} ' \
               f'\nRatio = {self.ratio} ' \
               f'\nTotal Carbs = {self.total_carbs} ' \
               f'\nBolus = {self.bolus:.2f} ' \
               f'\nCorrection Dose = {self.correction_dose} ' \
               f'\n ' \
               f'\nTotal Dose (Bolus + Correction) = {self.total_insulin_dose:.0f} Units'


