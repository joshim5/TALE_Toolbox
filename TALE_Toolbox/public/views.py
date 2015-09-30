# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, make_response)
from TALE_Toolbox.utils import flash_errors
from TALE_Toolbox.computations import ReferenceSequenceGenerator

#from TALE_Toolbox.computations import generate_genbank

blueprint = Blueprint('public', __name__, static_folder="../static")

@blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("public/home.html")

@blueprint.route("/about/")
def about():
    return render_template("public/about.html")

@blueprint.route("/generate/")
def generate():
    sequence = request.args.get('sequence')
    g_monomer = request.args.get('g_monomer')
    backbone = request.args.get('backbone')
    generator = ReferenceSequenceGenerator(sequence, g_monomer, backbone)
    genbank = generator.generate_genbank()
    response = make_response(genbank)
    response.headers["Content-Disposition"] = "attachment; filename=reference_seq.gb"
    response.status_code = 200
    return response
