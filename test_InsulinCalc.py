import pytest
import InsulinCalc


test_bolus_calc_outcomes = [[55, 15, 3.6666],
                            [1, 20, 0.05],
                            ]

test_correction_calc_outcomes = [[50, 120, 60, 0],
                                 [176, 110, 50, 1.32],
                                 ]

test_total_dose_calc_outcomes = [[1, 1, 1, 1, 1, 1],
                                 [100, 120, 50, 20, 1, 0]
                                 ]



class TestInsulinCalc:
    def setup_method(self):
        self.calc = InsulinCalc.InsulinCalc()

    def teardown_method(self):
        del self.calc

    @pytest.mark.parametrize('total_carbs, ratio, bolus', test_bolus_calc_outcomes)
    def test_calculate_bolus(self, total_carbs, ratio, bolus):
        self.calc.total_carbs = total_carbs
        self.calc.ratio = ratio
        self.calc.calculate_bolus()
        assert self.calc.bolus == pytest.approx(bolus, abs=0.001)

    @pytest.mark.parametrize('current_blood_sugar, target_blood_sugar, correction_factor, correction_dose', test_correction_calc_outcomes)
    def test_calculate_correction(self, current_blood_sugar, target_blood_sugar, correction_factor, correction_dose):
        self.calc.current_blood_sugar = current_blood_sugar
        self.calc.target_blood_sugar = target_blood_sugar
        self.calc.correction_factor = correction_factor
        self.calc.calculate_correction()
        assert self.calc.correction_dose == pytest.approx(correction_dose, abs=0.001)

    @pytest.mark.parametrize('current_blood_sugar, target_blood_sugar, correction_factor, ratio, total_carbs, total_insulin_dose', test_total_dose_calc_outcomes)
    def test_calculate_total_dose(self, current_blood_sugar, target_blood_sugar, correction_factor, ratio, total_carbs, total_insulin_dose):
        self.calc.current_blood_sugar = current_blood_sugar
        self.calc.target_blood_sugar = target_blood_sugar
        self.calc.correction_factor = correction_factor
        self.calc.ratio = ratio
        self.calc.total_carbs = total_carbs
        self.calc.calculate_total_dose()
        self.calc.total_insulin_dose = round(self.calc.total_insulin_dose)
        assert self.calc.total_insulin_dose == pytest.approx(total_insulin_dose, abs=0.001)


