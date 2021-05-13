import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("data/King_County_House_prices_dataset.csv")

df.fillna(0, inplace=True)

# check are there any duplicates id. 
# Choosing id to check duplicates, because it should have unique value for each house

df["id"].duplicated().sum() #we sum how many duplicates id are in "id"

#  drop the duplicate id
df.drop_duplicates(subset = "id", keep="last", inplace=True) 

#removing outliers

var = df[["price", "bedrooms", "bathrooms", "sqft_living",
          "sqft_lot", "floors", "view", "condition" , "grade", 
          "sqft_above", "sqft_living15", "sqft_lot"]]

import numpy as np
from scipy import stats
z = np.abs(stats.zscore(var))
z

df = df[(z < 3).all(axis=1)]


#date column was a string, convert into datetime dtpye, using pd.to_datetime()

df["date"] = pd.to_datetime(df["date"])

# create column month, with string "January to December"
import calendar

df["month"] = df['date'].dt.month #extract month from datetime
df['month'] = df['month'].apply(lambda x: calendar.month_name[x]) #month into string, .month_name()

#create another month column with month in integer
df["month_n"] = df['date'].dt.month

# change orders of index column, moving month next to date
df.columns
df = df[['id', 'date', "month_n", 'month', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15']]

seattle = [98101, 98102, 98103, 98104, 98105,
           98106, 98107, 98108, 98109, 98112, 
           98115, 98116, 98117, 98118, 98119, 
           98121, 98122, 98125, 98126, 98133, 
           98134, 98136, 98144, 98146, 98154, 
           98164, 98174, 98177, 98178, 98195, 98199]

#source zipcode: http://www.city-data.com/zipmaps/Seattle-Washington.html

# filtered only the zipcode in seattle
df.query("zipcode in @seattle", inplace=True)

# map houses concentrated in Seattle


plt.figure(figsize=(20,12))
sns_map = sns.jointplot(x=df.long, y=df.lat, size=9, color= "purple") 
plt.title("The Concentration of Houses in the City Center: Seattle")
sns.despine

#convert values in dataframe df to correlation values
corr_df = df.corr(method="pearson")
print(corr_df.head(3))

# create heatmap plot, to visualize the correlation

import plotly.graph_objects as go

fig_heatmap = go.Figure(go.Heatmap(
        x=corr_df.columns,
        y=corr_df.columns,
        z=corr_df.values.tolist(),
        colorscale='rdylgn', zmin=-1, zmax=1))

fig_heatmap.update_layout(height=600, width=800, #ideally height= 1000, and width=800, it takes the notebook slower
                  title_text="Houses' Features which influence the Price")
#fig_heatmap.show()


# Regression plot 1

sql_bed = df.groupby("id").agg({"sqft_living" : "mean", "bedrooms": "mean", "price": "mean"})

import plotly.express as px
fig_sql_bed = px.scatter(
    sql_bed, x ='sqft_living', y='price', opacity=0.65,
    trendline='ols', hover_data=['bedrooms'], color='bedrooms',
    labels=dict(sqft_living = "House Interior in Squared Feet", price = "Price in Million USD", 
                bedrooms = "Number of Bedrooms")
)
fig_sql_bed.update_layout(title_text="The average of sqft living & bedrooms with the average of price")
#fig_sql_bed.show()


# Regression plot 2

sqabove_floors = df.groupby("id").agg({"sqft_above" : "mean", "floors": "mean", "price": "mean"})

import plotly.express as px
fig_sqabove_floors = px.scatter(
    sqabove_floors, x ='sqft_above', y='price', opacity=0.65,
    trendline='ols', hover_data=['floors'], color='floors',
    labels=dict(sqft_above = "House Size in Squared Feet", price = "Price in Million USD", 
                floors = "Number of Floors")
)
fig_sqabove_floors.update_layout(title_text="The average of sqft above & floors with the average price")
#fig_sqabove_floors.show()


#regression plot 3

sql_grade = df.groupby("id").agg({"sqft_living" : "mean", "grade": "mean", "price": "mean"})

import plotly.express as px
fig_sql_grade = px.scatter(
    sql_grade, x ='sqft_living', y='price', opacity=0.65,
    trendline='ols', hover_data=['grade'], color='grade',
    labels=dict(sqft_living = "House Interior in Squared Feet", price = "Price in Million USD", 
                grade = "House grade")
)
fig_sql_grade.update_layout(title_text="The average of sqft living & grade with average price")
#fig_sql_grade.show()


# Regression plot 4
sqabove_cond = df.groupby("id").agg({"sqft_above" : "mean", "condition": "mean", "price": "mean"})

import plotly.express as px
fig_sqabove_cond = px.scatter(
    sqabove_cond, x ='sqft_above', y='price', opacity=0.65,
    trendline='ols', hover_data=['condition'], color='condition',
     labels=dict(sqft_above = "House Size in Squared Feet", price = "Price in Million USD", 
                condition = "House Condition")
)
fig_sqabove_cond.update_layout(title_text="The average of sqft above & condition with average price")
#fig_sqabove_cond.show()

# sort data values based on month (from January to December)
df_month_sort = df.sort_values(["month_n"])

#Bubble Plot using Plotly
fig_date2 = px.scatter(df_month_sort, x = "sqft_living", y = "price", animation_frame="month", animation_group= "price", 
                       size = "price", color = "zipcode", hover_name= "bedrooms", 
                       labels=dict(month_n= "month", sqft_living= "Size of House Interior", price= "price", 
                                   bedrooms="number of bedrooms", zipcode = "zipcode"))

fig_date2.update_layout(title_text="The Price Transition over the periods based on some parameters", transition = {'duration': 100})
fig_date2.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 3000
#fig_date2.show()


#import plotly go
import plotly.graph_objects as go

# filtered the data based on mid-ranged price
medium_price= df.query("price >= price.quantile(0.3) and price <= price.quantile(0.7)")
plotly_map = go.Figure(data=go.Scattergeo(
        lon = medium_price['long'],
        lat = medium_price['lat'],
        text = medium_price["price"],
        mode = 'markers',
        marker_color = medium_price['zipcode'],
        ))

plotly_map.update_layout(
        title = 'The Houses in the Seattle based on Prices',
        geo_scope='usa',
    )
#plotly_map.show()


# libraries for regression & plots
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import plot_partregress_grid
import statsmodels.formula.api as smf
import base64


# single linear regression for price & Sqft_living (before filtering the mid-ranged price)

ols_model_1 = ols("price ~ sqft_living + 0", data = df).fit()

fig_ols1, ax = plt.subplots()
fig_ols1 = sm.graphics.plot_fit(ols_model_1, 0, ax=ax)
ax.set_ylabel("price")
ax.set_xlabel("Size of House Interior")
ax.set_title("OLS Model for Linear Regression (Price vs Sqlt_Living")

# single linear regression for price & grade (before filtering the mid-ranged price)
ols_model_2 = ols("price ~ grade + 0", data = df).fit()

fig_ols2, ax = plt.subplots()
fig_ols2 = sm.graphics.plot_fit(ols_model_2, 0, ax=ax)
ax.set_ylabel("price")
ax.set_xlabel("Grade")
ax.set_title("OLS Model for Linear Regression (Price vs Grade")


# multiple regression sqft_living & sqft_above

fig_ols_3 = plt.figure(figsize=(8, 6))
results = smf.ols('price ~ sqft_living + grade + 0', data=df).fit()

plot_partregress_grid(results, fig=fig_ols_3)

# Import necessary libraries fo Dash

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
notes=''

server = app.server


def getPlot(plotObject, title, notes="", static=False):
    if static == True:
        image_filename = f"assets/{plotObject}"
        encoded_image = base64.b64encode(open(image_filename, "rb").read())
        card = dbc.CardBody([
            dbc.Col([
                html.Img(src="data:image/png;base64,{}".format(encoded_image.decode()),
                className='img-thumbnail img-fluid p-1',
                style=dict(width='600px')
                ),
            ], width='100%'),
        ])
    else:
        card = dbc.CardBody([
            dcc.Graph(
                figure = plotObject.update_layout(
                    template='plotly',
                    plot_bgcolor= 'white',
                    paper_bgcolor= 'white',
                ),config={
                    'displayModeBar': True
                }
            )
        ])
    return html.Div([
        dbc.Card([
            dbc.CardHeader([
                html.H5(title)
            ]),
            card,
            dbc.CardFooter([
                html.P(notes)
            ])
        ])
    ])


encoded_image = base64.b64encode(open("assets/seattle_foto.png", "rb").read())

# Author info
def getAuthor():
    return html.Div([
        dbc.Card([
            dbc.CardHeader([
                html.H5("Project: Exploratory Data Analysis for King County House Price Dataset.")
            ]),
            dbc.CardBody([
                dbc.Row([
                    # dbc.Col([
                    #     html.Img(src="data:image/png;base64,{}".format(encoded_image.decode())
                    # , width="500px")], width='6'),
                    dbc.Col([
                        html.Div([
                            html.P('Hi, my name is Maria Ulfah.'),
                            html.P("This is my first data science project at neuefische GmbH to find the best house for my Stakeholder: Nicole Johnson"),
                            html.P("Mr. Johnson wants to buy a house in a lively and a centered neighborhood, with a mid-ranged price."),
                            html.P("The Hypotheses are:"),
                            html.P("1. The Houses in centered neighborhood are more expensive than in the country sides"),
                            html.P("2. The larger the house, the higher the price"),
                            html.P("3. The houses in the centered neighborhood with a mid-ranged of price have small to medium size, and with averaged facility"),
                            html.P("In this regard, the objectives of my analysis are:"),
                            html.P("1. To filter the Houses which are located only in the central city of King County"),
                            html.P("2. To find the Houses with price around median, by prioritizing the convenience and functionality. Note: luxury is not that important"), 
                            html.A("You can find a full version of my analysis in my Github.", href="https://github.com/neuefische/EDA-individual-assignment"),
                        ])
                    ], width='12')
                ])
                
                
            ],
            )
        ])
    ])


app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
               dbc.Row([
                dbc.Col([
                    getAuthor()
                ], width=6),
                dbc.Col([
                    getPlot('sns_map.png', "The Map of Houses Concentrated in Seattle", "The central neighborhood areas have the Zipcode between 98101 - 98199, which are located in the Seattle City Center. There are around 7020 houses available for sale in this area", static=True)
                ], width=6),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    getPlot(fig_heatmap, "The Houses' Features: How particular features influence the price?", "Some features have strong positive correlations to the price: sqft_living, sqft_above, bedrooms, and grade")
                ], width=8),
                dbc.Col([
                    getPlot(fig_sql_bed, "The Relationship between Houses' Interior size and the Price", "Bigger houses tend to have more bedrooms, more bedrooms are consecutively more expensive too. With a mid-ranged price, Mr. Johson likely can afford the house with number of Bedrooms no more than three, and has size around 2.000 - 3.000 sq feet")
                ], width=4),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    getPlot(fig_sqabove_floors, "The Relationship between the House size (apart from Basement) and the Price", "The Number of floors are not determined by the size. Some houses with small size have more than one floor.")
                ], width=6),
                dbc.Col([
                    getPlot(fig_sql_grade, "The Relationship between Houses' grade and the Price", "The higher the grade of the house, the more expensive is the price. However, the grade is not a Mr. Johnson's concern.")
                ], width=6),
            ], align='start'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    getPlot(fig_sqabove_cond, "The Relationship between Houses' size (apart from Basement) and the Price, does houses' condition matter?", "The houses' condition does not really influence the price. In his budget, Mr. Johnson can still possibly afford a house in such a good condition.")
                ], width=6),
                dbc.Col([
                    getPlot(fig_date2, "Let's see how the price changing over the periods (within a year)", "The period in a year does not really influence the price. However, Mr.Johson has more possibilities to find a house with his budget in some specific areas, since the location matters.")
                ], width=6),
            ], align='start'),
            dbc.Row([
                dbc.Col([
                    getPlot(plotly_map, "where are the best strategic location for Mr. Johnson?, affordable but connected to the city center", "There are around 2800 Houses in Seattle that suit Mr. Johnson's Budget (500K - 600K), with around 1.500 - 2.500 sqft in the size and has a max 3 numbers of bedrooms")
                ], width=12),
            ], align='start'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    getPlot('fig_ols1.png', "The OLS Regression Model House Interrior Vs Price", "RSquared 90%", static=True)
                ], width=4),
                dbc.Col([
                    getPlot('fig_ols2.png', "The OLS Regression Model House Grade Vs Price", "RSquared 87%", static=True)
                ], width=4),
                dbc.Col([
                    getPlot('fig_ols_3.png', "The OLS Regression Model House Interior & Grade Vs Price", "Rsquared 91%", static=True)
                ], width=4),
            ], align='start'), 
            html.Br(),    
        ]), color = 'white'
    )
])


if __name__ == '__main__':
    app.run_server()
