import dash_core_components as dcc
import dash_html_components as html
import dash_table

from components import Header, get_lexicon_from_pathname

centered_style = {
    "width": "95%",
    "textAlign": "center",
    "marginLeft": "2.5%",
    "marginRight": "2.5%",
    "marginTop": 0,
    "marginBottom": 15,
}
centered_style_no_margin = {"width": "100%", "textAlign": "center", "marginTop": 0, "marginBottom": 15}
default_style = {"marginTop": 0, "marginBottom": 15}


def build_layout(pathname):
    """Build the main layout."""

    return html.Div(
        [
            html.Div(
                [
                    # Header with logo, title and lexical fields
                    Header(),
                    # Title to introduce Lexical Filtering
                    html.Div(
                        [
                            html.H6(
                                ["Choice of intent"], className="gs-header gs-text-header padded", style=default_style
                            )
                        ]
                    ),
                    # Dropdown for Lexical Field Selector
                    dcc.Dropdown(
                        id="fields-dropdown",
                        options=[
                            {"label": field, "value": field} for field in get_lexicon_from_pathname(pathname).keys()
                        ],
                        clearable=False,
                        style=default_style,
                        placeholder="Choose an intent...",
                    ),
                    # Dropdown for Words of Lexical Field Selector
                    dcc.Dropdown(
                        id="words-dropdown",
                        multi=True,
                        clearable=False,
                        style=default_style,
                        placeholder="Choose some intent words...",
                    ),
                    # Dropdown for all-or-any-word Selector
                    dcc.Dropdown(
                        id="all-any-dropdown",
                        options=[{"label": "All words", "value": "AND"}, {"label": "Any word", "value": "OR"}],
                        value="AND",
                        clearable=False,
                        style=default_style,
                    ),
                    # Datatable component
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="datatable",
                                columns=[
                                    {"name": i, "id": i, "deletable": False}
                                    for i in ["intent", "subintent", "sentence", "number of words"]
                                ],
                                editable=True,
                                sort_mode="multi",
                                style_header={"backgroundColor": "white", "fontWeight": "bold"},
                                style_cell={
                                    "fontFamily": "Arial",
                                    "size": 10,
                                    "textAlign": "left",
                                    "whiteSpace": "no-wrap",
                                    "overflow": "hidden",
                                    "textOverflow": "ellipsis",
                                    "maxWidth": "500px",
                                    "padding": "5px",
                                },
                                style_cell_conditional=[
                                    {"if": {"row_index": ind}, "backgroundColor": "rgb(248, 248, 248)"}
                                    for ind in range(0, 15, 2)
                                ],
                                css=[
                                    {
                                        "selector": ".dash-cell div.dash-cell-value",
                                        "rule": "display: inline; white-space: inherit; "
                                        "overflow: inherit; text-overflow: inherit;",
                                    }
                                ],
                                page_current=0,
                                page_size=15,
                            )
                        ],
                        className="twelve columns",
                    ),
                    html.Div([dcc.Markdown("""...""")], style=centered_style),
                    # Title and text to introduce Graphs
                    html.Div(
                        [
                            html.H6(
                                ["Histogram of the number of words per intent"],
                                className="gs-header gs-text-header padded",
                                style={"marginTop": 15},
                            )
                        ],
                        style=default_style,
                    ),
                    # Graphs component
                    html.Div(
                        [html.Div(id="build_graphs"), html.Div([dcc.Graph(id="graphs")], className="twelve columns")],
                        className="row",
                    ),
                ],
                className="subpage",
            )
        ],
        className="page",
    )


# 404 Error Page
noPage = html.Div([Header(), html.P(["404 Page not found"])], className="no-page")
