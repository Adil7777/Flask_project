from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
def index():
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


# @app.route('dol_graphs')
# def dol_graphs():
#     return render_template('dol_graphs.html')
#

if __name__ == '__main__':
    app.run(debug=True)
