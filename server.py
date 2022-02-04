from flask import request, Flask, make_response
import dataHolder


def open_request(client_resp):
    if client_resp != "":
        data = []
        for key in client_resp:
            data.append(client_resp[key])
        table = dataHolder.Calc()
        table.check_to_unpack(data)
        table.calc(data)
        return table.code_status(), table.answer()


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    client_send = request.get_json()
    answer = open_request(client_send)
    print(answer)
    answer = make_response(answer[1], answer[0])
    return answer


if __name__ == "__main__":
    app.run('127.0.0.1', port=5001)
