# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, make_response)
from flask_login import login_user, login_required, logout_user

from TALE_Toolbox.extensions import login_manager
from TALE_Toolbox.user.models import User
from TALE_Toolbox.public.forms import LoginForm
from TALE_Toolbox.user.forms import RegisterForm
from TALE_Toolbox.utils import flash_errors
from TALE_Toolbox.database import db

from TALE_Toolbox.computations import generate_genbank

blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User.create(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        active=True)
        flash("Thank you for registering. You can now log in.", 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)

@blueprint.route("/generate/")
def generate():
    sequence = request.args.get('sequence')
    g_monomer = request.args.get('g_monomer')
    backbone = request.args.get('backbone')
    genbank = generate_genbank(sequence, g_monomer, backbone)
    response = make_response(genbank)
    response.headers["Content-Disposition"] = "attachment; filename=reference_seq.gb"
    response.status_code = 200
    return response
