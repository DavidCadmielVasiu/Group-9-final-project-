#I used the "AlcoholAbuseApp.py" file that we had from our VisualizationLab-Part 3 lab as a foundation to build
#this app, and I used help from the "allCharts.py" file as well.
#font used in certain locations with style={'font-family': 'Montserrat , sans-serif'}: https://fonts.google.com/specimen/Montserrat?query=mon
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('AlcoholDataset.csv')

app = dash.Dash()

# Layout
app.layout = html.Div(children=[
    html.Header([
        html.H1(children='Underage Alcohol Abuse Awareness')
    ], style={'background': '#288a8a', 'textAlign': 'center', 'color': 'white', 'padding': '10px', 'font-family': 'Montserrat , sans-serif'}),
    html.H1('Our Mission', style={'textAlign': 'center','font-family': 'Montserrat , sans-serif'}),
    html.H2('Who we are', style={'textAlign': 'center', 'font-family': 'Montserrat , sans-serif', 'color': '#288a8a'}),
    html.Div('We are a group of students from UNCC who are working on a web-based application. We are working as part of a software engineering group in order to bring useful projects to the public.', style={'textAlign': 'center', 'font-family': 'Montserrat , sans-serif'}),
    html.H2('What is the goal of this application', style={'textAlign': 'center', 'font-family': 'Montserrat , sans-serif', 'color': '#288a8a'}),
    #help with border in CSS, https://www.w3schools.com/css/css_border_width.asp, https://www.w3schools.com/cssref/pr_border-color.asp
    html.Div('The goal of this application is to present data collected by the World Health Organization in a manner that allows for a comparative analysis of alcohol abuse. This information could then be used to foster intelligent discourse both among the worldwide general public and policy makers which could in turn foster targeted and coherent reforms.', style={'textAlign': 'center', 'font-family': 'Montserrat , sans-serif'}),
    html.Br(),
    html.Br(),
    html.Div('**countries that have no restrictions on the blood alcohol content (BAC) while driving will corespond to a BAC limit of 1%, others have a 0% BAC limit because there is a total ban on having any alcohol in your body while driving, '
             'or they have no regualtions in place because they have a total ban on the consumption of alcohol in general', style={'font-family': 'Montserrat , sans-serif', 'font-style': 'italic', 'font-size': '15px'}),
    html.Br(),
    html.Div('**countries with a total ban on alcohol advertising on social media have a value of 1. Countries with a partial ban on alcohol advertising on social media have a value of 0.5, and countries that do not have a total ban '
             'but have more restrictions than a partial ban have a value of .75.'
             ' Countries with no restrictions on alcohol advertising on social media have a value of 0, similarly countries that have voluntary/ self-restricted regulations on alcohol advertising on social media have a '
             'value of 0.', style={'font-family': 'Montserrat , sans-serif', 'font-style': 'italic', 'font-size': '15px'}),
    html.H3('Graphs ordered by highest % of 15-19 year olds that have consumed alcohol', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif', 'border-style': 'solid', 'border-width': '2px 0px 0px 0px', 'border-color': '#288a8a', 'padding': '20px 0px 0px 0px'}),
    html.Div('These bar charts are ordered by the top 30 countries who have the highest percentage of 15-19 year olds that have consumed alcohol. You can choose from the below options to view the top 30 countries based off various factors.', style = {'font-family': 'Montserrat , sans-serif'}),
    html.Br(),
    dcc.Graph(id='graph1'),
    html.Br(),
    dcc.RadioItems(
        id='select_graphType_Top',
        options=[
            {'label': '% of 15-19 year olds that have consumed alcohol', 'value': '% of 15-19 year olds that have consumed alcohol'},
            {'label': 'Blood Alcohol Content limit', 'value': 'BAC limit (while driving)'},
            {'label': 'Bans on alcohol advertisements on social media', 'value': 'Ban on Alcohol Advertisements on social media'}
        ],
        value='% of 15-19 year olds that have consumed alcohol',
        labelStyle={"padding": "10px"}
    ),
    html.Br(),
    html.H3('Graphs ordered by lowest % of 15-19 year olds that have consumed alcohol', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif', 'border-style': 'solid', 'border-width': '2px 0px 0px 0px', 'border-color': '#288a8a', 'padding': '20px 0px 0px 0px'}),
    html.Div('These bar charts are ordered by the bottom 30 countries who have the lowest percentage of 15-19 year olds that have consumed alcohol. You can choose from the below options to view the top 30 countries based off various factors.', style={'font-family': 'Montserrat , sans-serif'}),
    html.Br(),
    dcc.Graph(id='graph2'),
    html.Br(),
    dcc.RadioItems(
        id='select_graphType_Bottom',
        options=[
            {'label': '% of 15-19 year olds that have consumed alcohol', 'value': '% of 15-19 year olds that have consumed alcohol'},
            {'label': 'Blood Alcohol Content limit', 'value': 'BAC limit (while driving)'},
            {'label': 'Bans on alcohol advertisements on social media', 'value': 'Ban on Alcohol Advertisements on social media'}
        ],
        value='% of 15-19 year olds that have consumed alcohol',
        labelStyle={"padding": "10px"}
    ),
    html.Br(),
    html.H3('The problem...', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif', 'border-style': 'solid', 'border-width': '2px 0px 0px 0px', 'border-color': '#288a8a', 'padding': '20px 0px 0px 0px'}),
    html.Div('This data allows us to see the various factors that affect drinking from the ages 15-19. Drinking '
             'under the age (referring to 21) has serious consequences on the user. According to medlineplus.gov '
             '"Drinking during puberty can also change hormones in the body. This can distrupt growth and puberty"'
             '. Alcohol consumption can lead various injuries and even death. According to scramsystems.com, '
             '"Drivers under the age of 21 represent about 10% of licensed drivers in the U.S. but '
             'are responsible for 17% of fatal alcohol-involved crashes.". The U.S. ranks 20 on the list of '
             'the highest percentage of 15-19 year old people who have consumed alcohol at 59.9%. This number'
             'is high, considering that the legal age limit for purchasing alcohol is 21 in the U.S ', style={'font-family': 'Montserrat , sans-serif'}),
    html.H3('What can we do?', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif'}),
    html.Div('The data above can provide good information about what we can do regarding this sad situation. '
             'If we look at the second section of graphs, graphs ordered by lowest % of 15-19 year olds that have consumed alcohol, '
             'we can see a trend. The countries with the least amount of people ages 15-19 years olds that have consumed alcohol have stricter laws '
             'regarding the advertisement of alcohol on social media. They have stricter regulations regarding drinking and driving. And a good amount '
             'of these countries have a complete ban on the consumption of alcohol in general, not just while driving. The data suggests that '
             ' some countries with strict regulations (restrictions on alcohol advertising on social media and lower BAC limits while driving) have low percentages '
             'of young people (ages 15-19) that have consumed alcohol. However, there are opposite examples where countries with strict regulations have high percentages '
             'of young people (ages 15-19) that have consumed alcohol. The reasons might be becuase there is no age limit '
             'on the consumption of alcohol in those countries, take Luxembourg for example. This data should be viewed in the context of each countries specific laws '
             'in order to interprit the data correctly.', style={'font-family': 'Montserrat , sans-serif'}),
    html.H3('Conclusion/ our findings', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif'}),
    html.Div('In conclusion, we can see that countries with stricter regulations on alcohol advertising on social media and lower BAC levels while driving '
             'seem to have smaller percentages of 15-19 year olds that consume alcohol. Even though there are outliers and counter examples for the case above, '
             'countries with high levels of young people consuming alcohol can learn and adopt the regulations and policies that countries with low levels of young people consuming alcohol use. ', style={'font-family': 'Montserrat , sans-serif'}),
    html.H3('Future Work', style={'color': '#288a8a', 'font-family': 'Montserrat , sans-serif'}),
    html.Div(' In the future, we hope to add a feature where users are able to select different countries on a world map and view data for that specific country. '
             'We were only able to provide data for the top and bottom 30 countries on a bar graph, but it would have been more efficient to show data for all countries. '
             'It would also be helpful if users were able to click on a specific country and get data such as percentage of youth drinkers in that country, the BAC limit, and ad restrictions on a single page. '
             'That feature would allow easier navigation through the website while also providing more information.', style={'font-family': 'Montserrat , sans-serif'}),
    html.Br(),
    html.Br(),
    html.H3('References', style={'font-family': 'Montserrat , sans-serif'}),
    html.Div('1. https://medlineplus.gov/ency/patientinstructions/000528.htm', style={'font-family': 'Montserrat , sans-serif'}),
    html.Div('2. https://www.scramsystems.com/blog/2018/02/sobering-statistics-underage-drunk-driving/', style={'font-family': 'Montserrat , sans-serif'})

])

#help with having multiple Outputs https://community.plotly.com/t/multiple-outputs-in-dash-now-available/19437
#help with making figures with go.Figure https://plotly.com/python/creating-and-updating-figures/
@app.callback([Output('graph1', 'figure'),
              Output('graph2', 'figure')],
              [Input('select_graphType_Top', 'value'), Input('select_graphType_Bottom', 'value')])
def update_figure(select_graphType_Top, select_graphType_Bottom):
    new_df = df1.sort_values(by=['% of 15-19 year olds that have consumed alcohol'], ascending=[False]).head(30)
    data_barchart = [go.Bar(x=new_df['First Location'], y=new_df[select_graphType_Top])]

    figure = go.Figure(
        data=data_barchart,
        layout=go.Layout(title= select_graphType_Top + ' from the top 30 countries',
            xaxis={'title': 'Country'},
            yaxis={'title': select_graphType_Top}
        )
    )
    new_df2 = df1.sort_values(by=['% of 15-19 year olds that have consumed alcohol'], ascending=[True]).head(30)
    data_barchart2 = [go.Bar(x=new_df2['First Location'], y=new_df2[select_graphType_Bottom])]

    figure2 = go.Figure(
        data=data_barchart2,
        layout=go.Layout(title=select_graphType_Bottom + ' from the bottom 30 countries',
                  xaxis={'title': 'Country'},
                  yaxis={'title': select_graphType_Bottom})
    )

    return figure, figure2


if __name__ == '__main__':
    app.run_server()