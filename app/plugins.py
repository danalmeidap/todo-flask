from datetime import datetime

from mistune import markdown


def format_date(date: datetime):
    return date.strftime("%d-%m-%Y")


def configure(app):

    app.add_template_global(markdown)

    app.add_template_filter(format_date)
