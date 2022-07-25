from flask import Flask, jsonify , request
import time

app = Flask(_name_)
@app.route('/bot', method=['POST'])

#response
def response():
    query = dict([request.form])['query']
    result = query + " " + time.ctime()
    return jsonify({'response' : result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)
