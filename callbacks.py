import pandas as pd
from dash.dependencies import Input, Output

from app import app
from components import build_datatable, build_graphs, get_lexicon_from_pathname

pd.options.mode.chained_assignment = None


# Word Selector callback
@app.callback(Output("words-dropdown", "options"), [Input("url", "pathname"), Input("fields-dropdown", "value")])
def update_words(pathname, field):
    """Update words to display."""

    return [{"label": word, "value": word} for word in get_lexicon_from_pathname(pathname).get(field, [])]


# Datatable data callback
@app.callback(
    Output("datatable", "data"),
    [
        Input("url", "pathname"),
        Input("fields-dropdown", "value"),
        Input("words-dropdown", "value"),
        Input("all-any-dropdown", "value"),
    ],
)
def update_datatable(pathname, field, words, and_or):
    """Update datatable to display."""

    return build_datatable(pathname[1:], field, words, and_or)


# Graphs callback
@app.callback(Output("graphs", "figure"), [Input("datatable", "data"), Input("url", "pathname")])
def update_graphs(data, pathname):
    """Update graphs to display."""

    return build_graphs(pd.DataFrame.from_dict(data), get_lexicon_from_pathname(pathname))
