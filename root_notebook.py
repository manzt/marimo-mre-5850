# root.py
import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell
async def _():
    from other_notebooks import foo

    foo_app = await foo.app.clone().embed()
    foo_app
    return (foo_app,)


@app.cell
def _(foo_app):
    foo_app.defs.get("notebook_location")
    return

@app.cell
def _(foo_app):
    foo_app.defs.get("notebook_file")
    return


if __name__ == "__main__":
    app.run()
