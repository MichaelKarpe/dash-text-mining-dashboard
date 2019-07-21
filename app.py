import dash

# import dash_auth

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, serve_locally=False, url_base_pathname="/")
server = app.server
app.config.suppress_callback_exceptions = True

# Authentification can be deleted by commenting the two following lines
# VALID_USERNAME_PASSWORD_PAIRS = [["smalltalk-user", "xa29ANMtW1dZDGQIQvdGXvpI56H1Emt5"]]
# auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)
