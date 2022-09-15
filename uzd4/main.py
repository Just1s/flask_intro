from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/metai', methods=['GET', 'POST'])
def ar_keliamieji():
    if request.method == 'POST':
        metai = request.form['metai']
        return render_template('tikrinimas.html', metai=int(metai))
    else:
        return render_template('ivedimas.html')


if __name__ == '__main__':
    app.run(debug=True)
