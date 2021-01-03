import flask
from flask_cors import CORS
from flask_cors import cross_origin
import bank as bank
import trade as trade
from flask import render_template,request, make_response
from get_balance import get_balance
import uuid

app = flask.Flask(__name__)
CORS(app, cors_allowed_origins='*')


@app.route('/', methods=['GET','POST'])
def home():
    balance = get_balance(bank)
    tradebalance = get_balance(trade)
    if request.method == "POST":
        if request.values["send"]=="send":
            amount = float(request.values["transfer_amount"])
            bank.transfer_out(amount)
    return render_template("index.html",bankbalance=balance,tradebalance=tradebalance)
def setcookie():
    resp = make_response("setting up")
    resp.set_cookie("UID",uid)
    return resp


if __name__ == '__main__':
    crypto_wallet = {"ETH":0,"BTC":0}  #虛擬貨幣錢包
    bank = bank.bank(10000)
    trade = trade.trade_account(0)
    print(get_balance(bank))
    app.run(host="0.0.0.0", port=8080)
    uid = uuid.uuid4
    resp = make_response("setting up")
    resp.set_cookie("UID",uid)

    