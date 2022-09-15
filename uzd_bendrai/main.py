from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/metai', methods=['GET', 'POST'])
def ar_keliamieji():
    if request.method == 'POST':
        metai = request.form['metai']
        return render_template('tikrinimas.html', metai=int(metai))
    else:
        return render_template('ivedimas.html')


@app.route('/keliamieji')
def keliamieji():
    return render_template('trecias.html')


@app.route('/<name>')
def antras(name):
    return render_template('antras.html', vardas=name)


if __name__ == '__main__':
    app.run(debug=True)
