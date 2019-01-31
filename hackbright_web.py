"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student
    Begins at /student-search => enter input => routes to /student to display query info
    """

    return render_template("student_search.html")

@app.route("/confirmation")
def display_redirect():

    render_template("student_info.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student
    
    html has form where we ask for (first_name, last_name, github)
    new route to new html to confirm added student

    """

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    # first_name, last_name, github = 

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("confirmation.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

@app.route("/student-info")
def display_newstudent_form():

    return render_template("student_add.html")






if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
