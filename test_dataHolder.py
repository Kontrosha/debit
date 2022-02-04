import unittest
import dataHolder


class TestCalc(unittest.TestCase):
	def setUp(self):
		self.calc = dataHolder.Calc()
		self.errors_table = {}

	def test_too_many_values(self):
		row = "12.12.2001 6 10000 7.5 15 16"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": "Данные введены некорректно"}
		self.assertEqual(self.calc.answer(), err)

	def test_too_few_values(self):
		row = "12.12.2001 6 10000"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": "Данные введены некорректно"}
		self.assertEqual(self.calc.answer(), err)

	def test_forget_to_unpack(self):
		data = []
		self.calc.calc(data)
		err = {"Ошибка": "Пустая таблица"}
		self.assertEqual(self.calc.answer(), err)

	def test_empty_data(self):
		data = []
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": "Данные введены некорректно"}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_day(self):
		row = "64.12.2001 6 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная дата. Введите дату в формате dd.mm.yyyy"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_month(self):
		row = "4.15.2001 6 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная дата. Введите дату в формате dd.mm.yyyy"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_year(self):
		row = "12.12.1 6 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная дата. Введите дату в формате dd.mm.yyyy"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_data_letters(self):
		row = "06.Jan.2021 6 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная дата. Введите дату в формате dd.mm.yyyy"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_period_lower_bound(self):
		row = "12.12.2001 -5 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный период. Период должен быть целым числом в диапазоне от 1 до 60."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_period_higher_bound(self):
		row = "12.12.2001 600 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный период. Период должен быть целым числом в диапазоне от 1 до 60."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_period_incorr_data(self):
		row = "12.12.2001 kek 10000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный период. Период должен быть целым числом в диапазоне от 1 до 60."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_amount_lower_bound(self):
		row = "12.12.2001 10 100 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная сумма. Введите сумму в диапазоне 10000 до 3000000."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_amount_higher_bound(self):
		row = "12.12.2001 10 10000000000 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная сумма. Введите сумму в диапазоне 10000 до 3000000."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_amount_incorr_data(self):
		row = "12.12.2001 10 adbca 7.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректная сумма. Введите сумму в диапазоне 10000 до 3000000."]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_rate_incorrect_point(self):
		row = "12.12.2001 10 101530 7,5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный процент. Введите процент в диапазоне от 1 до 8. Используйте точку (пример 1.23)"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_rate_lower_bound(self):
		row = "12.12.2001 10 101530 0.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный процент. Введите процент в диапазоне от 1 до 8. Используйте точку (пример 1.23)"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_rate_higher_bound(self):
		row = "12.12.2001 10 101530 10.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный процент. Введите процент в диапазоне от 1 до 8. Используйте точку (пример 1.23)"]}
		self.assertEqual(self.calc.answer(), err)

	def test_wrong_rate_incorr_data(self):
		row = "12.12.2001 10 101530 0.b"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {"Ошибка": ["Некорректный процент. Введите процент в диапазоне от 1 до 8. Используйте точку (пример 1.23)"]}
		self.assertEqual(self.calc.answer(), err)

	def test_calc_1_period(self):
		row = "31.01.2021 1 10000 6"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {
			"31.01.2021": 10050.00}
		self.assertEqual(self.calc.answer(), err)

	def test_calc_10_period(self):
		row = "29.10.1997 10 10000 3.5"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {
			"29.10.1997": 10029.17,
			"29.11.1997":	10058.42,
			"29.12.1997":	10087.76,
			"29.01.1998":	10117.18,
			"28.02.1998":	10146.69,
			"29.03.1998":	10176.28,
			"29.04.1998":	10205.96,
			"29.05.1998":	10235.73,
			"29.06.1998":	10265.58,
			"29.07.1998":	10295.52
		}
		self.assertDictEqual(self.calc.answer(), err)

	def test_calc_12_period(self):
		row = "29.06.2004 10 101520 8"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {
			"29.06.2004":	102196.80,
			"29.07.2004":	102878.11,
			"29.08.2004":	103563.97,
			"29.09.2004":	104254.39,
			"29.10.2004":	104949.42,
			"29.11.2004":	105649.08,
			"29.12.2004":	106353.41,
			"29.01.2005":	107062.43,
			"28.02.2005":	107776.18,
			"29.03.2005":	108494.69
		}
		self.assertDictEqual(self.calc.answer(), err)

	def test_calc_30_period(self):
		row = "29.06.2004 30 101520 8"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {
			"29.06.2004":	102196.80,
			"29.07.2004":	102878.11,
			"29.08.2004":	103563.97,
			"29.09.2004":	104254.39,
			"29.10.2004":	104949.42,
			"29.11.2004":	105649.08,
			"29.12.2004":	106353.41,
			"29.01.2005":	107062.43,
			"28.02.2005":	107776.18,
			"29.03.2005":	108494.69,
			"29.04.2005":	109217.99,
			"29.05.2005":	109946.11,
			"29.06.2005":	110679.08,
			"29.07.2005":	111416.94,
			"29.08.2005":	112159.72,
			"29.09.2005":	112907.46,
			"29.10.2005":	113660.17,
			"29.11.2005":	114417.91,
			"29.12.2005":	115180.69,
			"29.01.2006":	115948.56,
			"28.02.2006":	116721.55,
			"29.03.2006":	117499.70,
			"29.04.2006":	118283.03,
			"29.05.2006":	119071.58,
			"29.06.2006":	119865.39,
			"29.07.2006":	120664.50,
			"29.08.2006":	121468.93,
			"29.09.2006":	122278.72,
			"29.10.2006":	123093.91,
			"29.11.2006":	123914.54
			}
		self.assertDictEqual(self.calc.answer(), err)

	def test_calc_60_period(self):
		row = "08.08.2008 60 15000 4.56"
		data = list(map(str, row.split()))
		self.calc.check_to_unpack(data)
		self.calc.calc(data)
		err = {
			"08.08.2008": 15057.00,
			"08.09.2008": 15114.22,
			"08.10.2008": 15171.65,
			"08.11.2008": 15229.30,
			"08.12.2008": 15287.17,
			"08.01.2009": 15345.27,
			"08.02.2009": 15403.58,
			"08.03.2009": 15462.11,
			"08.04.2009": 15520.87,
			"08.05.2009": 15579.85,
			"08.06.2009": 15639.05,
			"08.07.2009": 15698.48,
			"08.08.2009": 15758.13,
			"08.09.2009": 15818.01,
			"08.10.2009": 15878.12,
			"08.11.2009": 15938.46,
			"08.12.2009": 15999.02,
			"08.01.2010": 16059.82,
			"08.02.2010": 16120.85,
			"08.03.2010": 16182.11,
			"08.04.2010": 16243.60,
			"08.05.2010": 16305.33,
			"08.06.2010": 16367.29,
			"08.07.2010": 16429.48,
			"08.08.2010": 16491.91,
			"08.09.2010": 16554.58,
			"08.10.2010": 16617.49,
			"08.11.2010": 16680.64,
			"08.12.2010": 16744.02,
			"08.01.2011": 16807.65,
			"08.02.2011": 16871.52,
			"08.03.2011": 16935.63,
			"08.04.2011": 16999.99,
			"08.05.2011": 17064.59,
			"08.06.2011": 17129.43,
			"08.07.2011": 17194.52,
			"08.08.2011": 17259.86,
			"08.09.2011": 17325.45,
			"08.10.2011": 17391.29,
			"08.11.2011": 17457.37,
			"08.12.2011": 17523.71,
			"08.01.2012": 17590.30,
			"08.02.2012": 17657.15,
			"08.03.2012": 17724.24,
			"08.04.2012": 17791.59,
			"08.05.2012": 17859.20,
			"08.06.2012": 17927.07,
			"08.07.2012": 17995.19,
			"08.08.2012": 18063.57,
			"08.09.2012": 18132.21,
			"08.10.2012": 18201.12,
			"08.11.2012": 18270.28,
			"08.12.2012": 18339.71,
			"08.01.2013": 18409.40,
			"08.02.2013": 18479.35,
			"08.03.2013": 18549.58,
			"08.04.2013": 18620.06,
			"08.05.2013": 18690.82,
			"08.06.2013": 18761.85,
			"08.07.2013": 18833.14
		}
		self.assertDictEqual(self.calc.answer(), err)
