import requests

def sort_data(server_answer):
	sorted_data = {}
	sorted_key = sorted(server_answer, key=server_answer.get)
	for key in sorted_key:
		sorted_data[key] = server_answer[key]
	return sorted_data
def app():
	url = 'http://127.0.0.1:5001/'
	print("Введите дату, период, сумму, процент")
	to_send = list(map(str, input().split()))
	data = {}
	for i in range(len(to_send)):
		data[i] = to_send[i]
	resp = requests.post(url, json=data)
	get_answ = resp.json()
	get_answ = sort_data(get_answ)
	for key in get_answ:
		print(key, get_answ[key])



if __name__ == "__main__":
	app()

