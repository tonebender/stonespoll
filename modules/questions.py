# -*- coding: utf-8 -*-
# http://nedbatchelder.com/text/unipain.html

from flask import Flask, request, session, redirect, url_for, abort, \
  render_template, flash, make_response, Blueprint, current_app, json
import conf

questions = Blueprint('questions', __name__)

@questions.route('/')
def quiz():
    return render_template('questions.html')
