# -*- coding: utf-8 -*-
# http://nedbatchelder.com/text/unipain.html

from flask import Flask
import conf

from modules.questions import questions

app = Flask(__name__)
app.config.from_object(__name__)

# Main app settings
app.config.update(dict(
    QUESTIONS_DB="",
    RESULT_DB=""
))
app.config.from_object('conf.DevelopmentConfig')
app.config.from_envvar('STONESPOLL_SETTINGS', silent=True)

app.register_blueprint(questions)
    
if __name__ == '__main__':
    app.run()
