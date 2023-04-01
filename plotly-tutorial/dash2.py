'''
scatter plots can be made using any type of catersian axes, including linear, logarithmic,
categorical or date axis.

scatter plots where one axis is categorical are often known as dot plots.

'''

import plotly.express as px 
df = px.data.medals_long() 

fig = px.scatter(df, y='nation', x='count',
                 color='medal', symbol='medal')

fig.update_traces(marker_size=50)


fig.show() 


# %% grouped scatter points 

''' 
by default, scatter points at the same location are overlayed, we can see this 
in the previous example, with the values for Canada for bronze and silver.
set scattermode='group' to plot scatter points to one another, centered around the
shared location
'''


import plotly.express as px 
df = px.data.medals_long() 

fig = px.scatter(df, y='count', x='nation',  color='medal')
fig.update_traces(marker_size=10) 
fig.update_layout(scattermode='group')
fig.show()


# %%

# you can configure the gap between groups of scatter points using scattergap. here we 
# if to 0.75, which brings the points close together by allocting moe space to the 
# gap between groups. if you don't use scatergap, a default value of 0 is used, unless you have
# bargap set. if you have bargap set, the scattergap defaults to that value. 

df =px.data.medals_long() 
fig = px.scatter(df, y='count', x='nation', color='medal')
fig.update_traces(marker_size=10)
fig.update_layout(scattermode="group", scattergap=0.75)
fig.show() 


# %% Errors bars

# plot supports error bars
'''for functions representing 2D data points such as px.scatter, px.line, px.bar, etc errors bars are given as a column name which is the value of teh error_x (for the rror on x position_ and `error_y` (for the error on y position))'''
df = px.data.iris() 
df = px.data.iris()
df.head()

df['e'] = df['sepal_width'] / 100
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 error_x='e', error_y='e')
fig.show()
# %%  Asymmetric Error Bars with Plotly Express
import plotly.express as px 
df = px.data.iris() 

df["e_plus"] = df['sepal_width']/100
df["e_minus"] =  df['sepal_width']/40
fig = px.scatter(df, x='sepal_width', y="sepal_length", color="species", 
                 error_y="e_plus", error_x='e_minus')


fig.show()


# %%

# Error bars with graph_objects
# basic symmetric error bars

import plotly.graph_objects as go 

fig = go.Figure(data=go.Scatter(
        x=[0,1,2],
        y=[6, 10, 2],
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=[1,2,3],
            visible=True # array is referring to error of y, must set to true to see
        )
    )   
)
fig.show()
# %%

# asymmetric error bars
import plotly.graph_objects as go 
fig = go.Figure(data=go.Scatter(
    x=[1,2,3,4], 
    y=[2,1,3,4],
    error_y=dict(
        type='data',
        symmetric=False, 
        array=[.1, .2, .1, .1], # top array
        arrayminus=[.2, 1, 1, .2] # bottom array
    )
))
fig.show()

# %%  Error bars as percentage of the y Value 
 
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
    x=[0, 1, 2],
    y=[6, 10, 2], 
    error_y=dict(
        type='percent',  # value of error bar give as percent of y value 
        value=50, 
        visible=True
    )
))
fig.show()


# %% Asymmetric errors bars with a constant offset 

fig = go.Figure(data=go.Scatter(
    x = [1,2,3,5], # this is not a categorical representation 
    y = [2,1,3,4],
    error_y = dict(
        type='percent',
        symmetric = False, 
        value = 15, 
        valueminus=25
    )
))

fig.show()

# %% Horizontal Error Bars

import plotly.graph_objects as go 


fig = go.Figure(data=go.Scatter(
    x = [1,2,3,4],
    y = [2,1,3,4],
    error_x = dict(
        type='percent',
        value=10
    ),
    error_y = dict(  # you can actually plot x-y offset in go.Scatter
        type='percent',
        symmetric = False, 
        value = 15, 
        valueminus=25
    )
))
fig.show()



# %%

# bar chart with Error bars
fig = go.Figure() 
fig.add_trace(go.Bar(
    name='control',
    x = ['Trial 1', 'Trial 2', 'Trial 3'], y=[3,6,4],
    error_y = dict(
        type='data',  array=[.5, 1, 2]
    )
))

fig.add_trace(go.Bar(
    name='Experimental',
    x = ['Trial 1', 'Trial 2', 'Trial 3'],  y=[4,7, 3],
    error_y = dict(type='data', array=[.5, 1, 2])
))

fig.update_layout(barmode='group')

fig.show()



# %% Marginal Distribution Plots 

import plotly.express as px
df = px.data.iris() 
fig = px.scatter(df, x="sepal_length",  y="sepal_width", 
                 marginal_x="histogram",  marginal_y="rug")

fig.show()

# %% 
import plotly.express as px
df = px.data.iris() 
fig = px.scatter(df, x="sepal_length",  y="sepal_width", 
                 marginal_x="histogram",  marginal_y="histogram")

fig.show()

# %% facetting




# %% colored and styped error bars

import plotly.graph_objects as go 
import numpy as np 


x_theo = np.linspace(-4, 4, 1000)  # np.ndarray
sincx = np.sinc(x_theo)

x = [-3.8, -3.03, -1.91, -1.46, -0.89, -0.24, -0.0, 0.41, 0.89, 1.01, 1.91, 2.28, 2.79, 3.56]
y = [-0.02, 0.04, -0.01, -0.27, 0.36, 0.75, 1.03, 0.65, 0.28, 0.02, -0.11, 0.16, 0.04, -0.15]


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_theo, y=sincx,
    name='sinc(x)'
))
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='measured',
    error_y=dict(
        type='constant',
        value=0.1,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    error_x=dict(
        type='constant',
        value=0.2,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    marker=dict(color='purple', size=8)
))
fig.show()
# %%


'''
dash is an open-source framework for building analytical applications, with
no javascript required, and it is tightly integrated with the plotly graphing libary 


'''


