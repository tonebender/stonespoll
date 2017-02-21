/* Main Javascript for stonespoll web app */

'use strict';

/**
 * Shorthand for document.getElementById()
 */
function byId(elementId) {
    return document.getElementById(elementId);
}

/**
 * Put an error message where the poll question otherwise should be.
 */
function applyError(msg) {
    console.log("Applyng error: " + msg);
    byId('question').innerHTML = '<p>' + msg + '</p>';
}

/**
 * Fetch question numbered qNumber from the backend via Ajax/JSON
 */
function getQuestion(qNumber) {
    var qobject, xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200) {
                qobject = JSON.parse(this.responseText);
                console.log(this.responseText); 
                applyQuestion(qobject);
            } else
                applyError('Error fetching poll question via ajax: ' + xmlhttp.status);
        }
    }
    xmlhttp.open('GET', '/question/' + qNumber, true);
    xmlhttp.send();
}

/**
 * Parse the question object from getQuestion() and put it on the page.
 */
function applyQuestion(qobject) {
    
    // Put the question on the page as a form or something
    var i;
    byId('question').innerHTML = '<p>' + qobject.number + '</p>';
    byId('question').innerHTML += '<p>' + qobject.qtext + '</p>';
    byId('question').innerHTML += '<p>' + qobject.answers + '</p>';
    for (i in qobject.results) {
        byId('question').innerHTML += '<p>' + qobject.results[i] + '</p>';
    }
}


/**
 * Get the user's answer (form data) to the question in question and 
 * record it for later analysis.
 */
function handleAnswer() {
    
}

/**
 * Show startlink (if this executes it means JS is enabled in the browser).
 */
window.onload = function() {
    byId('startlink').style.visibility = 'visible';
};
