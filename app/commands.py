import click
from flask import Flask
from datetime import datetime

from app.tasks import (
    get_all_tasks,
    get_task_by_slug,
    get_tasks_by_user,
    new_task,
    update_task_by_slug,
    delete_task_by_slug
)


@click.group()
def task():
    """Manage tasks"""


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


@task.command()
@click.option("--slug")
@click.option("--title")
@click.option("--content")
def update(slug, title, content):
    """Select a task and update"""
    task = get_task_by_slug(slug)
    if task:
        data = {
            "user": task['user'],
            "title": title,
            "content": content,
            "slug": title.replace("_", "-").replace(" ", "-").lower(),
            "active":True,
            "date": datetime.now()            
        }
        updated = update_task_by_slug(slug, data)
        click.echo(f"Task {updated['slug']} updated")
    else:
        click.echo("Task not found")


@task.command()
@click.option("--slug")
def delete(slug):
    """Select a task and delete"""
    if delete_task_by_slug(slug):
        click.echo("Task was deleted")
    else:
        click.echo("task already deleted or doesn't exist")


def configure(app: Flask):
    app.cli.add_command(task)
