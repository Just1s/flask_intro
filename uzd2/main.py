from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<name>')
def antras(name):
    return render_template('antras.html', vardas=name)


if __name__ == '__main__':
    app.run(debug=True)
