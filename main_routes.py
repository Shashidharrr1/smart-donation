from flask import Blueprint, render_template, url_for, request, redirect

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/donate-money', methods=['GET', 'POST'])
def donate_money():
    if request.method == 'POST':
        #  Process donation here (we'll implement this later)
        #  For now, just redirect to a thank you page or back to the form
        return redirect(url_for('main.donate_money'))
    return render_template('donate-money.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #  Process contact form submission (we'll implement this later)
        #  For now, just redirect to a thank you page or back to the form
        return redirect(url_for('main.contact'))
    return render_template('contact.html')