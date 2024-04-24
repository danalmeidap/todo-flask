import click
from flask import Flask

from app.tasks import (
    get_all_tasks,
    get_task_by_slug,
    get_tasks_by_user,
    new_task
)


@click.group()
def task():
    """Manage posts"""


@task.command("list")
def _list():
    """List all tasks"""
    for task in get_all_tasks():
        click.echo(task)


@task.command()
@click.option("--user")
@click.option("--title")
@click.option("--content")
def new(user, title, content):
    """Creates a new task"""
    new = new_task(user, title, content)
    click.echo(f"New task {new} created!")


@task.command()
@click.argument("slug")
def get(slug):
    """Get task by slug"""
    task = get_task_by_slug(slug)
    click.echo(task or "task nor found")


@task.command()
@click.option("--user")
def tasks(user):
    """Get user tasks"""
    for task in get_tasks_by_user(user):
        click.echo(task)


def configure(app: Flask):
    app.cli.add_command(task)
