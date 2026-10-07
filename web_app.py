from flask import Flask, render_template, request, redirect, url_for

from database import initialize_database
from crud import (
    create_student,
    get_all_students,
    search_students,
    update_student,
    delete_student,
)

from validators import (
    validate_name,
    validate_age,
    validate_email,
    validate_course,
)

app = Flask(__name__)

initialize_database()


@app.route("/")
def index():
    students = get_all_students()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "")
    age = request.form.get("age", "")
    email = request.form.get("email", "")
    course = request.form.get("course", "")

    valid, name_result = validate_name(name)
    if not valid:
        return redirect(url_for("index"))

    valid, age_result = validate_age(age)
    if not valid:
        return redirect(url_for("index"))

    valid, email_result = validate_email(email)
    if not valid:
        return redirect(url_for("index"))

    valid, course_result = validate_course(course)
    if not valid:
        return redirect(url_for("index"))

    create_student(
        name_result,
        age_result,
        email_result,
        course_result,
    )

    return redirect(url_for("index"))


@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").strip()

    if keyword:
        students = search_students(keyword)
    else:
        students = get_all_students()

    return render_template(
        "index.html",
        students=students,
        keyword=keyword,
    )


@app.route("/update/<int:student_id>", methods=["POST"])
def update(student_id):
    name = request.form.get("name", "")
    age = request.form.get("age", "")
    email = request.form.get("email", "")
    course = request.form.get("course", "")

    valid, name_result = validate_name(name)
    if not valid:
        return redirect(url_for("index"))

    valid, age_result = validate_age(age)
    if not valid:
        return redirect(url_for("index"))

    valid, email_result = validate_email(email)
    if not valid:
        return redirect(url_for("index"))

    valid, course_result = validate_course(course)
    if not valid:
        return redirect(url_for("index"))

    update_student(
        student_id,
        name_result,
        age_result,
        email_result,
        course_result,
    )

    return redirect(url_for("index"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    delete_student(student_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)