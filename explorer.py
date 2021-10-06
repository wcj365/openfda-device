from dash import html

from app import app

import layout

application = app.server      ## For deployment to AWS Elastic Beanstalk

app.layout = html.Div([
    html.Br(),
    html.H2("Medical Device Classfication Explorer"),
    html.Br(),
    layout.main

], className="container")


if __name__ ==  "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)