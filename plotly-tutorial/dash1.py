'''scatter plots in dash
dash is the est way to build analytical apps in python using plotly figures. to run the app below, run pip install dash, 

'''

from dash import Dash, dcc, html, Input, Output 
import plotly.express as px 


app = Dash(__name__)

app.layout = html.Div([
    html.H4('interactive scatter plot with iris dataset. '),
    dcc.Graph(id='scatter-plot'), 
    html.P("Filter by petal width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1, 
        marks={0: '0', 2.5: '2.5'}, 
        value=[0.5, 2]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = px.data.iris() 
    low, high = slider_range
    mask = (df['petal_width'] > low) & ( df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length", 
        color="species", size="petal_length", 
        hover_data=['petal_width'])
    return fig 

app.run_server(debug=True)