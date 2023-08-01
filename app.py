from flask import Flask, request, render_template, redirect
from currency import Currency


#from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

#debug = DebugToolbarExtension(app)


c = Currency()

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/submit')
def handle_submit():
    frm = request.args['frm']
    frm = frm.upper()
    to = request.args['to']
    to = to.upper()
    amount = request.args['amount']
    conv = c.check_valid_code(frm, to, amount)
    if conv == 'error':
        return redirect('/')
    else: 
        return render_template('result.html', conv = conv)
