from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def pirmas():
    return render_template('pirmas.html')


if __name__ == '__main__':
    app.run(debug=True)
