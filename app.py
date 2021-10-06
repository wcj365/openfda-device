import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.FLATLY,
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'Medical Device Classification Explorer', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__,  meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls
app.config.external_stylesheets=external_stylesheets
app.title="The K-anonymity Explorer"
app.index_string = '''<!DOCTYPE html>
<html>
<head>
{%metas%}
<title>{%title%}</title>
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
</body>
</html>
'''
