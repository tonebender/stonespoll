#!/usr/bin/env python

# Some stuff to externally manage the question database


import sqlite3, time, sys


def connect_to_db(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
    except:
        print "Could not open database:", db_filename
        sys.exit(0)
    else:
        return connection


def create_new_question_db(db_filename):
    connection = connect_to_db(db_filename)
    c = connection.cursor()
    
    # Delete existing
    c.execute("""DROP TABLE IF EXISTS stonesquestions;""")
    
    # Create new database from schema file
    with open('question_db_schema.sql', mode='r') as f:
        c.executescript(f.read())
    connection.commit()
    connection.close()
    return True


# self, number, qtext, answers, numof_members, numof_answers)
def add_question(number, qtext, answers, db_filename):
    connection = connect_to_db(db_filename)
    c = connection.cursor()
    
    format_str = """INSERT INTO stonesquestions (number, qtext, answers)
    VALUES (NULL, "{qtext}", "{answers}");"""
    sql_command = format_str.format(username=username, password=password, \
    first=fname, last=lname, joined=joining)
    c.execute(sql_command)
    connection.commit()
    connection.close()
    return True
    
    
def delete_question(username, db_filename):
    connection = connect_to_db(db_filename)
    c = connection.cursor()
    command = "DELETE FROM stonesquestions WHERE number =?"
    c.execute(command, (number,))
    connection.commit()
    connection.close()
    return True
    
    
def print_db(db_filename):
    connection = connect_to_db(db_filename)
    c = connection.cursor()
    c.execute('SELECT * FROM flaskusers')
    rows = c.fetchall()
    connection.close()
    for r in rows:
        print ""
        print "Question number:", r[0]
        print "Question text:", r[1]
        print "Answers:", r[2]


def show_usage():
    print """Usage: db_manager.py command [question] database_file
          command can be:
          a   add question to database
          d   delete question from database
          c   create new database (existing will be deleted)
          p   print existing database"""
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        show_usage()
    
    # Command c: Create new database
    if sys.argv[1] == 'c':
        if len(sys.argv) != 3:
            print "Too few or too many arguments."
            show_usage()
        if create_new_question_db(sys.argv[2]):
            print "Created new database", sys.argv[2]
        else:
            print "Error creating database", sys.argv[2]
            
    # Command p: Show database
    if sys.argv[1] == 'p':
        if len(sys.argv) != 3:
            print "Too few or too many arguments."
            show_usage()
        print_db(sys.argv[2])
            
    # Command a: Add new question to database
    if sys.argv[1] == 'a':
        if len(sys.argv) != 4:
            print "Incorrect number of arguments after command 'a'"
            sys.exit(0)
        print "Adding question {u} ...".format(u=sys.argv[2])
        #pw = raw_input("Please enter question's new password: ")
        #pa = raw_input("Repeat password: ")
        #if pw != pa:
        #   print "Passwords don't match"
        #    sys.exit(0)
        #hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
        #f = raw_input("User's first name: ")
        #l = raw_input("User's last name: ")
        #j = time.asctime(time.localtime(time.time()))
        
        if add_question(sys.argv[2], hashed_pw, f, l, j, sys.argv[3]):
            print "Successfully added question %s to database %s" % (sys.argv[2],
            sys.argv[3])
        
    # Command d: Delete question
    if sys.argv[1] == 'd':
        if len(sys.argv) != 4:
            print "Incorrect number of arguments after command 'd'"
        if delete_question(sys.argv[2], sys.argv[3]):
            print "Deleted question %s from %s" % (sys.argv[2], sys.argv[3])
