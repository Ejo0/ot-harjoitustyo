from invoke import task


@task
def initialize(ctx) :
    ctx.run("python3 src/initialize_db.py")

@task
def start(ctx) :
    ctx.run("python3 src/index.py")

@task
def test(ctx) :
    ctx.run("pytest src")

@task
def coverage(ctx) :
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx) :
    ctx.run("coverage report")

@task(coverage)
def coverage_html(ctx) :
    ctx.run("coverage html")