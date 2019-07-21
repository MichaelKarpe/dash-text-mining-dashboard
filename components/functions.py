import pandas as pd
from plotly import graph_objs, subplots

from mining import LEXIQUE, df, url_name_to_lexical_field

pd.options.mode.chained_assignment = None


def get_lexicon_from_pathname(pathname):
    """Link the webpage pathname to the corresponding lexicon."""

    if pathname == "/":
        return {
            lexicon_name: {word for field in lexicon.values() for word in field}
            for lexicon_name, lexicon in LEXIQUE.items()
        }
    else:
        return LEXIQUE[url_name_to_lexical_field[pathname]]


def build_datatable(pathname, field, words, and_or):
    """Update datatable depending on the activated filters."""

    data_frame = df

    if pathname:
        data_frame = data_frame[data_frame["intent"] == pathname]

    if field:
        data_frame = data_frame[(data_frame["intent"] == field) | (data_frame["subintent"] == field)]

    if words:
        word_filter = data_frame["QT_" + words[0]] > 0
        if len(words) >= 2:
            for word in words[1:]:
                if and_or == "AND":
                    word_filter = word_filter & (data_frame["QT_" + word] > 0)
                elif and_or == "OR":
                    word_filter = word_filter | (data_frame["QT_" + word] > 0)
        data_frame = data_frame[word_filter]

    return data_frame.to_dict("rows")


def build_graphs(data_frame, lexicon):
    """Update graphs depending on the activated filters."""

    intents = [
        field for field in lexicon.keys() if field in set(data_frame["intent"]) or field in set(data_frame["subintent"])
    ]

    fig = subplots.make_subplots(rows=len(intents), cols=1, shared_xaxes=False, subplot_titles=(tuple(intents)))

    for ind, field in enumerate(intents):

        data = data_frame[(data_frame["intent"] == field) | (data_frame["subintent"] == field)]

        sessions_bar = graph_objs.Histogram(
            x=data["number of words"].values,
            text="number of words",
            xbins=dict(start=1, end=max(data["number of words"]) + 1, size=1),
        )

        fig.append_trace(sessions_bar, ind + 1, 1)

    for i in fig["layout"]["annotations"]:
        i["font"] = dict(size=12)

    fig["layout"].update(height=min(200 + 200 * len(intents), 2500), showlegend=False)
    updated_fig = fig
    return updated_fig
