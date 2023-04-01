

#https://plotly.com/python/marginal-plots/
'''the marginal_x and marginal_y arguments accept on of 'historgram' 
'rug', 'box' or 'violin' (see also how to create histogram, box_plots, and violin_plots as the main figure 
)

marginal plots are linked to the main plot: try zooming or panning
on the main plot. 

marginal plot also support hover, including per-point hover as
with the rug-plot on the right: try hovering over the points on the 
right marginal plot. 
'''

# %% 

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", marginal_x="histogram", marginal_y="rug")
fig.show()
# %%

import plotly.express as px 

df = px.data.iris() 
fig = px.density_heatmap(df, x='sepal_length',  y='sepal_width', 
                    marginal_x='box', marginal_y='violin')
fig.show()

# %% arginal plots and color 

'''
marginal plots respect the color argument as well, and are linked to the respective
legend elemetns. try clicking on the legend items 
'''

import plotly.express as px 

df = px.data.iris() 
fig = px.scatter(df, x="sepal_length", y="sepal_width",  color="specieis",
                 marginal_x="box", marginal_y="violin", 
                 title="Click on the legend items!")
fig.show()


# %% marginal plots on histogram

'''histograms are often used to show the distribution of a variable, and they 
also support marginal plots in plotly.express, with the marginal argument'''


import plotly.express as px 
df = px.data.iris() 
fig = px.histogram(df, x="sepal_length", color="species", marginal="box")
fig.show()
# %%  

'''try hovering over the rug plot points to identify individual country values in 
histogram below:'''

import plotly.express as px 
df = px.data.gapminder().query('year == 2007')
fig = px.histogram(df, x="lifeExp", color="continent", marginal='rug', hover_name='country',
                   title="hover over the rug plot!")
fig.show()
# %%
import plotly.express as px 

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", 
                 color='sex', facet_col="day", marginal_x='box')
fig.show()
# %%

import plotly.express as px 
df = px.data.tips() 
fig = px.scatter(df, x="total_bill", y="tip", 
                facet_col='time', color='sex', marginal_y='tip')
fig.show()
# %%

import plotly.express as px 
df = px.data.tips() 
fig = px.histogram(df, x="total_bill", facet_col="day", color="sex", marginal="box")
fig.show()

# %%
