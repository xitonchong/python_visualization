# %%  linear fit trendlines with Plotly Express '''


''' add linear ordinary Least Squares (OLS) regression trendlines 
or non-linear locally weighted scatterplot smoothing (LOWESS)
trendlines to scatterplots in python. Options for moving averages
(rolling means) as well as exponentially-weighted and expanding
functions.'''


import plotly.express as px 

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", trednline="ols")
fig.show()
# %% Fitting multiple lines and retrieving the model parameters

import plotly.express as px 

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", 
                 color="sex", trendline="ols")
fig.show()

results = px.get_trendline_results(fig) 
print(results)

results.query("sex == 'Male' and smoker  == 'Yes'").px_fit_results.iloc[0].summary()

# %% Displaying a sigle trendline with multiple traces 
''' to display a single trendline using the entire dataset, set the
trendline_scope argument to "overall". the same trendline will be 
overlaid on all facets and animation frames. the trendline color can be 
overridden with trednline_color_override.'''


import plotly.express as px 
df = px.data.tips() 
fig = px.scatter(df, x="total_bill", y="tip",  symbol="smoker", 
                 color="sex", trendline="ols", trendline_scope="overall")
fig.show()

# %%
import plotly.express as px 
df = px.data.tips() 
fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", 
                color="sex", trendline="ols",
                trendline_scope="overall",
                trendline_color_override="black")
fig.show()
# %% OLS Parameters

import plotly.express as px 
df = px.data.gapminder(year=2007)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols", trendline_options=dict(log_x=True), 
                 title="Log-transformed fit on linear axes")
fig.show()

# %%  locally weighted scatterplot smoothing (LOWESS)

import plotly.express as px 

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG",  trendline="lowess")
fig.show()

# %%  

''' the level of smoothing can be controlled vai the frac trendline option, 
which indicates the fraction of the data that the LOWESS smoother should include. 
the default is a fairly smooth line with frac=0.666 and lowering this fraction will give
a line that more closely follows the data. '''


import plotly.express as px 
df = px.data.stocks(datetimes=True) 
fig = px.scatter(df, x="date", y="GOOG", trendline="lowess", 
                trendline_options=dict(frac=0.4)) # this control the variance
fig.show()

# %%  Moving averages'''

'''plotly express can leverage pandas' rolling, ewm, and expanding functions
in trendlines as well, for example to display moving averages. Values passed 
to trendline_options are passed directly to the underlying pandas function 
(with the exception of the funtion and function_options keys, see below)'''

import plotly.express as px 
df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", 
                 trendline_options=dict(window=5),  # window arg is exclusive to rolling
                 title="5-point moving average")

fig.show()

# %%  exponentially-weighted moving average (halflife of 2 points) 

fig = px.scatter(df, x="date", y="GOOG", trendline="ewm", 
                 trendline_options=dict(halflife=2), 
                 title="exponentially-weighted moving average (halflife of 2 points)")

fig.show()

# %%


import plotly.express as px 
df = px.data.stocks(datetimes=True) 
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", title="expanding mean")
fig.show()
# %% Other functions 
''' the rolling, expanding, and ewm trendlines support other functions than the default mean, 
enabling, for example, a moving-median trendline, or an expanding-max trendline'''


fig = px.scatter(df, x='date', y='GOOG', trendline="rolling", 
                trendline_options=dict(function='median', window=5), 
                title="rolling median")

fig.show()
# %%
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", 
                 trendline_options=dict(function="max"), 
                 title="expanding maximum")
fig.show()
# %%
''' in some cases,  it is necessary to pass options into the underlying Pandas function, 
for example the std parameter must be provided if the win_type argument to rolling
is "gaussian". this is possible with the function_args trendline option'''

fig = px.scatter(df, x="date", y="GOOG", trendline="rolling",
                 trendline_options=dict(window=5, 
                 win_type="gaussian", 
                 function_args=dict(std=2)),
                 title="rolling mean with Gaussian Window")
fig.show()
# %% displaying only the trendlines


df = px.data.stocks(indexed=True, datetimes=True) 
fig = px.scatter(df, trendline="rolling", trendline_options=dict(window=5), 
                 title="5-point moving average")
fig.data = [t for t in fig.data if t.mode == "lines"]
fig.update_traces(showlegend=True) # trendlines have showlegend=False by default 
fig.show()

# %%
import plotly.express as px 

df = px.data.gapminder().query("continent == 'Oceania'") 
fig = px.line(df, x='year', y='lifeExp', color='country', 
              symbol='country')
fig.show()


# %%
