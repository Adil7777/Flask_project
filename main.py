from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        print(request.form['sellist1'])
        print(request.form['sellist2'])
        print(request.form['amount'])
        return render_template('test.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/currency_rate')
def currency_rate():
    return render_template('currency_rate.html')


@app.route('/graphs')
def graphs():
    return render_template('graphs.html')


@app.route('/dol_graphs')
def dol_graphs():
    return render_template('dol_graphs.html')


@app.route('/eur_graphs')
def eur_graphs():
    return render_template('eur_graphs.html')


@app.route('/rub_graphs')
def rub_graphs():
    return render_template('rub_graphs.html')


if __name__ == '__main__':
    app.run(debug=True)
