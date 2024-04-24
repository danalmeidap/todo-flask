from datetime import datetime

from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required
from wtforms import fields, form, validators

from app.database import mongo

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)


class TasksForm(form.Form):
    user = fields.StringField("User", [validators.data_required()])
    title = fields.StringField("Title", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    content = fields.TextAreaField("Content")
    active = fields.BooleanField("Active", default=True)


class AdminTasks(ModelView):
    column_list = ["user", "title", "slug", "content", "active"]
    form = TasksForm

    def on_model_change(self, form, task, is_created):
        task["slug"] = task["slug"].replace("_", "-").replace(" ", "-").lower()
        if is_created:
            task["date"] = datetime.now()


def configure(app):
    app.admin = Admin(
        app,
        name=app.config.get("TITLE"),
        template_mode=app.config.get(
            "FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3"
        ),
    )
    app.admin.add_view(AdminTasks(mongo.db.tasks, "Task"))
