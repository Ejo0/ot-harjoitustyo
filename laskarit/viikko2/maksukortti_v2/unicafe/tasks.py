from invoke import task

@task
def coverage(ctx) :
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx) :
    ctx.run("coverage report")

@task(coverage)
def coverage_html(ctx) :
    ctx.run("coverage html")