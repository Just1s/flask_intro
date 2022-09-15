from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/keliamieji')
def keliamieji():
    return render_template('trecias.html')


if __name__ == '__main__':
    app.run(debug=True)
