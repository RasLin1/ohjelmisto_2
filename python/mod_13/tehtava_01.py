import math
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/isPrime")
def isPrime():
    try:
        args = request.args
        number = int(args.get("num"))
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
        response = {
            "number": number,
            "isPrime": is_prime
        }
    except ValueError:
        response = {
            "result": "Virhe tapahtui ;("
        }
    return jsonify(response)

@app.errorhandler(404)
def page_not_found(virhe):
    response = {
        "result": virhe.result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000) 

