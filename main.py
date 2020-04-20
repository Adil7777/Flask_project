from flask import render_template, Flask, request, url_for
from parcer import Currency
from logins import *
from send_email import send_email
from Currency_converter import currency_converter

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def change():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
                <html lang="en">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/change.css')}" />
                <head>
                    <meta charset="UTF-8">
                    <title>Login</title>
                </head>
                <body>
                <form class="box" method="post">
                    <h1>Login</h1>
                    <input type="text" name="name" placeholder="Username">
                    <input type="password" name="pass" placeholder="Password">
                    <input type="submit" name="" value="Login">
                    <a style="display: inline-block;
                                vertical-align: top;
                                margin: 0 25px;
                                position: relative;
                            
                                color: #A979EE;
                                text-decoration: none;
                                transition: color .2s linear;" 
                                href='create_account'>Don't have an account?</a>
                    <a style="display: inline-block;
                                vertical-align: top;
                                margin: 25px 25px;
                                position: relative;
                            
                                color: #A979EE;
                                text-decoration: none;
                                transition: color .2s linear;" 
                                href='forget_password'>Forget password(?</a>
                </form>
                </body>
                </html>'''
    elif request.method == 'POST':
        if str(request.form['name']) + ":" + str(request.form['pass']) in LOGINS:
            return render_template('test.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                                   eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                                   rub_buy=str(rub_buy), rub_sell=str(rub_sell), naz_dol=str(dol_naz),
                                   naz_eur=str(eur_naz),
                                   naz_rub=str(rub_naz))


currency = Currency()
cur = currency.check_currency()[0]
naz = currency.nazbank()

dol_sell, dol_buy = cur[0], cur[1]
eur_sell, eur_buy = cur[2], cur[3]
rub_sell, rub_buy = cur[4], cur[5]
kgs_sell, kgs_buy = cur[6], cur[7]
fnt_sell, fnt_buy = cur[8], cur[9]
dol_naz = naz[0].split(' ')[-1]
eur_naz = naz[1].split(' ')[-1]
kgs_naz = naz[2].split(' ')[-1]
rub_naz = naz[3].split(' ')[-1]
fnt_naz = naz[4].split(' ')[-1]


@app.route('/main', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('test.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                               eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                               rub_buy=str(rub_buy), rub_sell=str(rub_sell), naz_dol=str(dol_naz), naz_eur=str(eur_naz),
                               naz_rub=str(rub_naz))
    elif request.method == 'POST':
        a = currency_converter(request.form['amount'], request.form['sellist1'], request.form['sellist2'])
        return render_template('test.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                               eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                               rub_buy=str(rub_buy), rub_sell=str(rub_sell), naz_dol=str(dol_naz), naz_eur=str(eur_naz),
                               naz_rub=str(rub_naz), a=str(a))


@app.route('/create_account', methods=['POST', 'GET'])
def create_account():
    if request.method == 'GET':
        return render_template('create_account.html')
    elif request.method == 'POST':
        add_account(request.form['name'], request.form['pass'], request.form['email'])
        return render_template('test.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                               eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                               rub_buy=str(rub_buy), rub_sell=str(rub_sell), naz_dol=str(dol_naz), naz_eur=str(eur_naz),
                               naz_rub=str(rub_naz))


@app.route('/forget_password', methods=['POST', 'GET'])
def forget_password():
    if request.method == 'GET':
        return render_template('forget_password.html')
    elif request.method == 'POST':
        result = send_email(request.form['email'])
        return render_template('send_email.html', result=result)
    print(request.method)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/currency_rate')
def currency_rate():
    return render_template('currency_rate.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                           eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                           rub_buy=str(rub_buy), rub_sell=str(rub_sell))


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


@app.route('/converter', methods=['POST', 'GET'])
def converter():
    if request.method == 'GET':
        return render_template('converter.html')
    elif request.method == 'POST':
        a = currency_converter(request.form['amount'], request.form['sellist1'], request.form['sellist2'])
        return render_template('converter.html', a=str(a))


@app.route('/more_currencies')
def more_currencies():
    return render_template('more_currencies.html', dol_buy=str(dol_buy), dol_sell=str(dol_sell),
                           eur_buy=str(eur_buy), eur_sell=str(eur_sell),
                           rub_buy=str(rub_buy), rub_sell=str(rub_sell),
                           kgs_buy=str(kgs_buy), kgs_sell=str(kgs_sell),
                           fnt_buy=str(fnt_buy), fnt_sell=str(fnt_sell), naz_dol=str(dol_naz), naz_eur=str(eur_naz),
                           naz_rub=str(rub_naz), naz_kgs=str(kgs_naz), naz_fnt=str(fnt_naz))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
