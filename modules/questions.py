# -*- coding: utf-8 -*-
# http://nedbatchelder.com/text/unipain.html

from flask import Flask, request, session, redirect, url_for, abort, \
  render_template, flash, make_response, Blueprint, current_app, json
import conf

questions = Blueprint('questions', __name__)


class Question:
    """The main poll Question class.

    Attributes:
        number (int): The index number of the question
        qtext (string): The question
        answers (list w/ strings): All possible answers to the question
        results (list w/ lists w/ integers): A matrix where the answers (rows)
            are mapped to band members (cols), and each position will hold an
            integer (pos or neg) denoting how much each respective answer 
            affects each member score.
    """
    def __init__(self, number, qtext, answers, numof_members, numof_answers):
        self.number = number
        self.qtext = qtext
        self.answers = answers
        #self.results = [[0 for x in range(numof_members)]  # Matrix!
        #                for y in range(numof_answers)]
        i = 0
        rez = []
        for y in range(numof_answers):
            row = []
            for x in range(numof_members):
                print "y is " + str(y) + " and x is " + str(x)
                row.append(i)
                i += 1
            rez.append(row)
        self.results = rez
        
    def __str__(self):
        qstring = 'Question: ' + str(self.number) + \
                  '\n\"' + self.qtext + '\"\n';
        for y in range(len(self.results)):
            qstring = qstring + self.answers[y] + '  '
            for x in self.results[y]:
                qstring = qstring + str(x) + ' '
            qstring = qstring + '\n'
        return qstring
        
    def to_json(self):
        return {'number': self.number, 'qtext': self.qtext, 
                'answers': self.answers, 'results': self.results}


def fetch_question(qnumber):
    """Fetch poll question number qnumber from database, make it a Question
       object and return it."""
    qobject = Question(qnumber, 'How do you feel?', ['Good', 'Okay', 'Baad'], 7, 3)
    return qobject


@questions.route('/')
def quiz():
    """ Show the main page where we'll put the quiz questions through JS """
    return render_template('questions.html')


@questions.route('/question/<qnumber>', methods=['GET'])
def question(qnumber=None):
    
    """ Get a question number, fetch the question and return it
    as a JSON object. """
    
    if qnumber == None or not qnumber.isdigit():
        abort(404);
    return json.dumps(fetch_question(int(qnumber)).to_json())
