from flask import Blueprint, render_template,redirect,url_for

billing = Blueprint("billing", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")

@billing.route("billing_pagamento")
def billing_pagamento():
    return render_template("billing/billing_pagamento.html")

@billing.route("billing_cobranca")
def billing_cobranca():
    return render_template("billing/billing_cobranca.html")