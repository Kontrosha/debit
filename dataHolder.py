class Data:
	data = ""
	period = 0
	amount = 0
	rate = 0
	day = 0
	month = 0
	year = 0
	errors = []
	month_range = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

	def __init__(self, data, period, amount, rate):
		self.data = data
		self.period = period
		self.amount = amount
		self.rate = rate
		self.get_data()
		self.is_valid()

	def get_data(self):
		self.day, self.month, self.year = map(str, self.data.split('.'))

	def isvalid_data(self):
		if len(self.day) > 2:
			return False
		if len(self.month) > 2:
			return False
		if len(self.year) != 4:
			return False
		else:
			if not (1 <= int(self.day) <= 31):
				return False
			if not (1 <= int(self.month) <= 12):
				return False
			return True

	def isvalid_period(self):
		if self.period.isdigit() and 1 <= int(self.period) <= 60:
			return True
		return False

	def isvalid_amount(self):
		if self.amount.isdigit() and 10000 <= int(self.amount) <= 3000000:
			return True
		return False

	def isvalid_rate(self):
		if ',' in str(self.rate):
			return False
		for digit in self.rate:
			if not digit.isdigit() and digit != '.':
				return False
		if  1 <= float(self.rate) <= 8:
			return True
		return False

	def is_valid(self):
		err_codes = []
		if not self.isvalid_data():
			err_codes.append(-1)
		if not self.isvalid_period():
			err_codes.append(-2)
		if not self.isvalid_amount():
			err_codes.append(-3)
		if not self.isvalid_rate():
			err_codes.append(-4)
		self.errors = err_codes

	def catch_errors(self):
		whats_wrong = []
		for code in self.errors:
			if code == -1:
				whats_wrong.append('Некорректная дата. Введите дату в формате dd.mm.yyyy')
			if code == -2:
				whats_wrong.append("Некорректный период. Период должен быть целым числом в диапазоне от 1 до 60.")
			if code == -3:
				whats_wrong.append("Некорректная сумма. Введите сумму в диапазоне 10000 до 3000000.")
			if code == -4:
				whats_wrong.append(
					"Некорректный процент. Введите процент в диапазоне от 1 до 8. Используйте точку (пример 1.23)")
		return whats_wrong

	@staticmethod
	def is_special_year(y):
		if (int(y) % 4 == 0 and int(y) % 100 != 0) or int(y) % 400 == 0:
			return True
		return False

	def last_day(self, month, year):
		all_days = self.month_range[month]
		if month == 2 and self.is_special_year(year):
			return 29
		else:
			return all_days


class Calc:
	res = {}
	days = []
	sums = []
	input_data = None
	status = ""

	def __init__(self):
		self.res = {}
		self.days = []
		self.sums = []
		self.input_data = None
		self.status = "empty"

	def get_values(self, data):
		self.input_data = Data(data[0], data[1], data[2], data[3])

	def new_sum(self):
		period = int(self.input_data.period)
		new_sum = int(self.input_data.amount)
		rate = float(self.input_data.rate)
		for i in range(1, period + 1):
			new_sum *= (1 + (rate / 12 / 100))
			self.sums.append(round(new_sum, 2))

	def new_data(self, n):
		m = int(self.input_data.month)
		d = int(self.input_data.day)
		y = int(self.input_data.year)
		m += n
		if m > 12:
			y += (m-1) // 12
			m = (m-1) % 12 + 1
		l_d = self.input_data.last_day(m, y)
		if d > l_d:
			d = l_d
		if int(m) < 10:
			m = "0" + str(m)
		if int(d) < 10:
			d = "0" + str(d)
		return str(d) + '.' + str(m) + '.' + str(y)

	def calc(self, data):
		if self.status == "to_parse":
			self.get_values(data)
			if len(self.input_data.catch_errors()) == 0:
				self.new_sum()
				for i in range(int(self.input_data.period) + 1):
					self.days.append(self.new_data(i))
				for i in range(len(self.sums)):
					self.res[self.days[i]] = self.sums[i]
				self.status = "parsed"
			else:
				self.status = "errors"

	def answer(self):
		if self.status == "empty":
			self.res["Ошибка"] = "Пустая таблица"
		elif self.status == "errors":
			self.res["Ошибка"] = self.input_data.catch_errors()
		elif self.status == "unparsed":
			self.res["Ошибка"] = "Данные введены некорректно"
		return self.res

	def check_to_unpack(self, inp_list):
		if len(inp_list) != 4:
			self.status = "unparsed"
		else:
			self.status = "to_parse"

	def code_status(self):
		if self.status == "parsed":
			return 200
		else:
			return 400
