import altair as alt
from dash import Dash, dcc, html, Input, Output
from vega_datasets import data

    
iris = data.iris()


def plot_iris(xcol):
    chart = alt.Chart(iris).mark_point().encode(
        x=xcol,
        y='sepalWidth',
        tooltip='petalWidth').interactive()
    return chart.to_html()
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server
app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='petalWidth',
            options=[{'label': i, 'value': i} for i in iris.columns]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_iris(xcol='petalWidth'))])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'))
def update_output(xcol):
    return plot_iris(xcol)

if __name__ == '__main__':
    app.run_server(debug=True)