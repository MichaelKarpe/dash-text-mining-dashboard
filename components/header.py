import dash_core_components as dcc
import dash_html_components as html

from mining import df, lexical_field_to_url_name


def Header():
    return html.Div([get_logo(), get_header(), html.Br([]), get_menu()])


def get_logo():
    logo = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src="https://smalltalk.ams3.cdn.digitaloceanspaces.com/static/images/logos/smalltalk.svg",
                        height="133",
                        width="485",
                    )
                ],
                className="ten columns padded",
                style={"width": "100%", "textAlign": "center", "marginBottom": 30},
            )
        ],
        className="row gs-header",
    )
    return logo


def get_header():
    header = html.Div(
        [
            html.Div(
                [html.H5("Small talk benchmark")],
                className="twelve columns padded",
                style={"width": "100%", "textAlign": "center"},
            )
        ],
        className="row gs-header gs-text-header",
    )
    return header


def get_menu():
    menu = html.Div(
        [dcc.Link("Overview", href="/", className="tab first")]
        + [
            dcc.Link(field[0].upper() + field[1:], href=lexical_field_to_url_name[field], className="tab")
            for field in sorted(set(df["intent"]))
        ],
        className="row",
        style={"width": "100%", "textAlign": "center", "marginTop": 0, "marginBottom": 15},
    )
    return menu
