'''
scatter plots support faceting 
facet plots, also known as trellis plots or small multiples, are figures
made up of multiple subplots which have the same set of axes, where 
each subplot shows a subset of the data. while it is straighforwward to 
ise plotly's subplot capabilities to make such figures, it's far easier to use the 
built in facet_row and facet_col arguments in teh various plotly 
express function 

'''
# %% 
import plotly.express as px 

df = px.data.tips() 

fig = px.scatter(df, x='total_bill', y="tip", 
                 color='smoker', facet_col="sex",
                 facet_row="time")

fig.show()
# %%  Scatter plot column facets

import plotly.express as px 
df = px.data.tips() 

fig = px.scatter(df, x='total_bill', y='tip', 
                 color='smoker', facet_col='sex')
fig.show()
# %%  Bar chart row facets

fig = px.bar(df, x='size', y='total_bill', color='sex',
             facet_row='smoker')
fig.show()

# %% Wrapping column facets

# when the facet dimension has a large number of unique values, 
# it is possible to wrap columns using the facet_col_wrap argument

df = px.data.gapminder()

fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent',
                size='pop', facet_col='year', 
                facet_col_wrap=4)


fig.show()
# %% Histogram facet grids

import plotly.express as px 
df = px.data.tips() 

fig = px.histogram(df, x='total_bill', y='tip', color='sex',
                   facet_row='time', facet_col='day',
                   category_orders={
                        "day": ["Thur", "Fri", "Sat", "Sun"],
                        "time": ["Lunch", "Dinner"]
                   })
fig.show()

# %% Choropleth Column Facets 

import plotly.express as px 

df = px.data.election() 
print(df.head())
df = df.melt(id_vars='district', 
             value_vars=['Coderre', 'Bergeron', 'Joly'], 
             var_name="candidate",
             value_name='votes')
# stack 3 columns: Coderre, bergeron, Joly in same columns
# valus is votes
geojson = px.data.election_geojson() 

fig = px.choropleth(df, geojson=geojson, color="votes",
                        facet_col="candidate", 
                        locations="district",
                        featureidkey="properties.district", 
                        projection='mercator')

fig.update_geos(fitbounds='locations', visible=False) 
fig.show()
# %% Adding lines and rectangels tofacet plots 

import plotly.express as px 

df = px.data.stocks(indexed=True)

fig = px.line(df, facet_col="company", facet_col_wrap=2) 
fig.add_hline(y=1, line_dash='dot', 
             annotation_text='Jan 1, 2018 baseline', 
             annotation_position='bottom right')

fig.add_vrect(x0="2018-09-24", x1="2018-12-18", col=2,
              annotation_text="decline", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
fig.show()
# %%

import plotly.express as px 
df = px.data.tips() 

fig = px.scatter(df, x='total_bill', y='tip', color='sex', 
                facet_col='day',  facet_row='time')

import statsmodels.api as sm 
import plotly.graph_objects as go 

df = df.sort_values(by='total_bill')
model = sm.OLS(df['tip'], sm.add_constant(df['total_bill'])).fit()

# create the trace to be added to all facets
trace = go.Scatter(x=df['total_bill'], y=model.predict(), 
                line_color='black', name='overall OLS')

# give it a legend group and hide it from the legend
trace.update(legendgroup='trendline', showlegend=False)

# add it to all row/cols, but no to empty subplots
fig.add_trace(trace, row='all', col='all', exclude_empty_subplots=True) 

fig.update_traces(selector=-1, showlegend=True) 
fig.show()


# %% Facets with Independent Axes

''' by default, facet axes are linked together: zooming inside one of the facets will also 
zoom in the other facets. You can disable this behavior when you use facet_row only, by disabling matches on the 
Y aces, or when using facet_col, by disabling matches on the X axes. It is not recommended to use
to use this approach when using facet+row and facet_col together, as in this case 
it becomes very hard to understand the labeling of axes and grid lines. '''


import plotly.express as px 
df = px.data.tips() 

fig = px.scatter(df, x='total_bill',  y='tip', color='sex', facet_row='day')
fig.update_yaxes(matches=None) 
fig.show()

# %%

# disabling matches in xaxes facets
fig = px.scatter(df, x='total_bill', y='tip', color='sex', facet_col='day')
fig.update_xaxes(matches=None) 
fig.show()
# %%

# customizing subplot figure titles 
''' since subplot fiture titles are annotations, you can use the for_each_annotation 
function to customize them, for example to remove the equals0gn (=). 
 In the follow example, we pass a lambda function to for_each_annotation in order
 to change the figure subplot titles from smoker=No to smoker=Yes to ust no and yes

'''

import plotly.express as px 

fig = px.scatter(px.data.tips(), x='total_bill', y='tip', facet_col='smoker')
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.show()
# %%  Controlling Facet Spacing 

''' the facet_row_spacing and facet_col_spacig arguments can be used 
to control the spacing between rows and columns.  These values are specified in fractions of the 
plotting are in paper coordinats and not in pixels, so they will grow or shrink with the width 
and height of the figure.'''

import plotly.express as px 
df = px.data.gapminder().query("continent == 'Africa'")

fig = px.line(df, x='year', y='lifeExp', facet_col='country', facet_col_wrap=7,
              facet_row_spacing=0.04,  # defaultl is 0.07 when facet_col_wrap is used
              facet_col_spacing=0.04, # default s 0.03
              height=600, width=800, 
              title='life expectancy in Africa') 
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.update_yaxes(showticklabels=True) 
fig.show()
# %%  Synchronizing aces in subplots with matches 

'''
Using facet_col from plotly.express let `zoom` and `pan` each facet 
to the same range implicitly. However, if the subplots are createed with
make_subplots, the axis needds tobe updatd with matches parameter to 
update all the sbuplots accordingly.

Zoom in on trace below, to see the other subplots zoomed to the same 
x-axis range. To pan all the subplots, click and drag from the center
of x-axis to the side: 

'''
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import numpy as np 

N = 20 
x = np.linspace(0, 1, N)


fig = make_subplots(1, 3) 
for i in range(1, 4):
    fig.add_trace(go.Scatter(x=x, y=np.random.random(N)), 1, i)
fig.update_xaxes(matches='x')
fig.show()

# %%
