import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    notebook_location = mo.notebook_location()
    notebook_location
    return


@app.cell
def _():
    notebook_file = __file__
    notebook_file
    return


if __name__ == "__main__":
    app.run()
