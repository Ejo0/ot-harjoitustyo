from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def test(ctx) :
    ctx.run("pytest src")

@task
def coverage(ctx) :
    ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(ctx) :
    ctx.run("coverage report -m")

@task
def coverage_report_html(ctx) :
    ctx.run("coverage html")