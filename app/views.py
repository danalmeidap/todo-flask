from flask import Blueprint, abort, redirect, render_template, request, url_for
from flask_simplelogin import login_required

from app.tasks import (
    get_all_tasks,
    get_task_by_slug,
    get_tasks_by_user,
    new_task,
    delete_task_by_slug
)

bp = Blueprint("task", __name__, template_folder="templates")


@bp.route("/")
def index():
    tasks = get_all_tasks()
    return render_template("index.html.j2", tasks=tasks)


@bp.route("/<slug>")
def detail(slug):
    task = get_task_by_slug(slug)
    if not task:
        return abort(404, "Task Not Found")
    return render_template("task.html.j2", task=task)


@bp.route("/user/<user>")
def user(user):
    tasks = get_tasks_by_user(user)
    return render_template("index.html.j2", tasks=tasks)


@bp.route("/new", methods=["GET", "POST"])
@login_required()
def new():
    if request.method == "POST":
        user = request.form.get("user")
        title = request.form.get("title")
        content = request.form.get("content")
        slug = new_task(user, title, content)
        return redirect(url_for("task.detail", slug=slug))
    return render_template("form.html.j2")


@bp.route("/tasks/delete/<slug>", methods=["GET","POST","DELETE"])
def delete(slug):
    if delete_task_by_slug(slug):
        return {"msg":"Task deleted"}
    return abort(404, "Task not found")


def configure(app):
    app.register_blueprint(bp)
