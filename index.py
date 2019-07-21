import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import callbacks  # NOQA
from app import app, server  # NOQA
from layouts import build_layout, noPage
from mining import lexical_field_to_url_name

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Small talk benchmark</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Small talk benchmark</div>
    </body>
</html>
"""

app.layout = html.Div([dcc.Location(id="url", refresh=False), html.Div(id="page-content")])


# Update page callback
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """Update the lexicon page to display."""

    if pathname in ["/"] + [url_name for url_name in lexical_field_to_url_name.values()]:
        return build_layout(pathname)
    else:
        return noPage


external_css = [
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
    "//fonts.googleapis.com/css?family=Raleway:400,300,600",
    "https://codepen.io/bcd/pen/KQrXdb.css",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://codepen.io/dmcomfort/pen/JzdzEZ.css",
]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js", "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == "__main__":
    app.run_server(debug=False)
