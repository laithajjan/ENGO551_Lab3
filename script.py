from flask import Flask, render_template, request
import requests as r

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
