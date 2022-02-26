# fastfood.py
# Description: This file contains methods regarding routing orders.  

### python-packages
from flask import Blueprint, render_template, Flask, request, render_template, Response, flash, send_file, make_response, jsonify, redirect
from flask_login import login_required, current_user

### local-packages
from project.utilities.controls import AppControls
from project.utilities.logger import LoggerSetup

log = LoggerSetup().get_logger()
control = AppControls()
fastfood = Blueprint('fastfood', __name__)

@fastfood.route('/')
@login_required
def index():
    """
        Returns the order page.
    """
    return render_template('fastfood.html', name=current_user.username)

@fastfood.route('/submit_order', methods=['POST'])
@login_required
def submit_order():
    """
        Processes the Order
    """
    return redirect('/')