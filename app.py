import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from select_agol import Recommend


# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.GRID])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id = 'webtoon-memo', storage_type='session'),
    dcc.Store(id = 'genre-memo', storage_type='session'),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('메인화면', href='/main'),
    html.Br(),
    dcc.Link('추천', href='/recommend'),

])

totoal = pd.read_csv('output.csv')
totoal.drop_duplicates('name', inplace=True)
temp = totoal.iloc[:,:1]
temp['label'] = temp.name
temp.columns = ['value', 'label']
web_toon_options = temp.to_dict('records')

main_page = html.Div([

    dbc.Row(dbc.Col(html.H1(children='네이버 웹툰 추천'),style={'text-align':'center','background-color':'rgba(67, 216, 171, 0.466)'},)),
    dbc.Row(
        [
            dbc.Col(html.Div()),
            dbc.Col(html.Div(children='웹툰을 선택하세요'),style={'text-align':'center'}),
            dbc.Col(html.Div()),
        ],style = {'background-color':'rgba(113, 230, 97, 0.445)'}
    ),
           dbc.Row(
        [
            dbc.Col(html.Div()),
            dbc.Col(
                dcc.Dropdown(id = 'webtoon', options=web_toon_options
                ,multi = True,),
                ),
            dbc.Col(html.Div()),
            
        ],style = {'background-color':'rgba(113, 230, 97, 0.445)'}
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(children='장르를 선택하세요'),style={'text-align':'center'}),
        ],
        style = {'background-color': '#eca46080'}
    ),
       dbc.Row(
        [
            dbc.Col(html.Div()),
            dbc.Col(
                dcc.Dropdown(id = 'genre', options=[
                {'label': '무관', 'value' : '무관'},
                ],
                value=['무관'],multi = True,),
                ),
            dbc.Col(html.Div()),
        ],style = {'background-color': '#eca46080',}
    ),
    html.Br(),
    dcc.Link('추천', href='/recommend'),
    html.Br(),
])

@app.callback(dash.dependencies.Output('webtoon-memo', 'data'),
              dash.dependencies.Input('webtoon', 'value'))
def filter_countries(webtoon):
    if not webtoon:
        # Return all the rows on initial load/no country selected.
        return []

    return webtoon

@app.callback(dash.dependencies.Output('genre-memo', 'data'),
              dash.dependencies.Input('genre', 'value'))
def filter_countries(genre):
    if not genre:
        # Return all the rows on initial load/no country selected.
        return []

    return genre


page_recommend_layout = html.Div([
    # dbc.Row(
    #     html.Div(id='webtoon-content'),
    # ),
    # dbc.Row(
    #     html.Div(id='genre-content'),
    # ),
    dbc.Row(
        dbc.Col(html.Div('메인 추천',style={'text-align':'center','background-color': '#d9ffb3'})),
    ),
    html.Br(),
    dbc.Row([
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-1',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-1',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-1'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-1'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-2',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-2',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-2'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-2'),
                    ],style={'text-align':'center'}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-3', src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-3',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-3'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-3'),
                    ],style={'text-align':'center'}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-4', src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-4',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-4'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-4'),
                    ],style={'text-align':'center'}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        
         ]),
    html.Br(),
    dbc.Row(
        dbc.Col(html.Div('그림체 취향저격',style={'text-align':'center','background-color': '#d9ffb3'})),
    ),
    html.Br(),
    dbc.Row([
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-5', src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-5',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-5'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-5'),
                    ],style={'text-align':'center'}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-6',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-6',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-6'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-6'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-7',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-7',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-7'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-7'),
                    ],style={'text-align':'center'}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-8',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-8',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-8'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-8'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
    ]),
    html.Br(),
    dbc.Row(
        dbc.Col(html.Div('감상평 연관추천',style={'text-align':'center','background-color': '#d9ffb3'})),
    ),
    html.Br(),
    dbc.Row([
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-9',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-9',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-9'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-9'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
         dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-10',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-10',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-10'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-10'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-11',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-11',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-11'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-11'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.CardImg(id= 'Webtoon-img-12',src='', top=True, style={'width': '20rem','height':'12rem','display':'block','margin-left':'auto','margin-right':'auto'}),
                dbc.CardBody(
                    [
                        html.H4("", className="card-title",id = 'Webtoon-name-12',style = {'background-color': '#59b300'}),
                        html.P([
                            "", ],
                            className="card-text", id = 'Webtoon-context-12'
                        ),
                        dcc.Link('해당웹툰 보러가기', href='', id = 'Webtoon-link-12'),
                    ],style={'text-align':'center',}
                ),
            ],style = {'background-color': '#ccff99','border-style':'solid','border-color':'#ffffff','width':'22rem'}
            ),
        ),
    ]),
    dcc.Link('메인 페이지', href='/main'),
])

# @app.callback(dash.dependencies.Output('webtoon-content', 'children'),
#               dash.dependencies.Input('webtoon-memo', 'data'))
# def filter_countries(webtoon):

#     return 'You have selected "{}"'.format(webtoon)

# @app.callback(dash.dependencies.Output('genre-content', 'children'),
#               dash.dependencies.Input('genre-memo', 'data'))
# def filter_countries(genre):
#     return 'You have selected "{}"'.format(genre)

@app.callback([dash.dependencies.Output('Webtoon-name-1', 'children'),
                dash.dependencies.Output('Webtoon-img-1', 'src'),
                dash.dependencies.Output('Webtoon-context-1', 'children'),
                dash.dependencies.Output('Webtoon-link-1', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select(model.find_cluster()[0],model.find_cluster()[1])[0]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-2', 'children'),
                dash.dependencies.Output('Webtoon-img-2', 'src'),
                dash.dependencies.Output('Webtoon-context-2', 'children'),
                dash.dependencies.Output('Webtoon-link-2', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select(model.find_cluster()[0],model.find_cluster()[1])[1]
    return [name, model.find_thumb(name), model.find_summary(name), model.find_link(name)]

@app.callback([dash.dependencies.Output('Webtoon-name-3', 'children'),
                dash.dependencies.Output('Webtoon-img-3', 'src'),
                dash.dependencies.Output('Webtoon-context-3', 'children'),
                dash.dependencies.Output('Webtoon-link-3', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select(model.find_cluster()[0],model.find_cluster()[1])[2]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-4', 'children'),
                dash.dependencies.Output('Webtoon-img-4', 'src'),
                dash.dependencies.Output('Webtoon-context-4', 'children'),
                dash.dependencies.Output('Webtoon-link-4', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select(model.find_cluster()[0],model.find_cluster()[1])[3]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-5', 'children'),
                dash.dependencies.Output('Webtoon-img-5', 'src'),
                dash.dependencies.Output('Webtoon-context-5', 'children'),
                dash.dependencies.Output('Webtoon-link-5', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_iic()[0]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-6', 'children'),
                dash.dependencies.Output('Webtoon-img-6', 'src'),
                dash.dependencies.Output('Webtoon-context-6', 'children'),
                dash.dependencies.Output('Webtoon-link-6', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_iic()[1]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-7', 'children'),
                dash.dependencies.Output('Webtoon-img-7', 'src'),
                dash.dependencies.Output('Webtoon-context-7', 'children'),
                dash.dependencies.Output('Webtoon-link-7', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_iic()[2]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-8', 'children'),
                dash.dependencies.Output('Webtoon-img-8', 'src'),
                dash.dependencies.Output('Webtoon-context-8', 'children'),
                dash.dependencies.Output('Webtoon-link-8', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_iic()[3]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-9', 'children'),
                dash.dependencies.Output('Webtoon-img-9', 'src'),
                dash.dependencies.Output('Webtoon-context-9', 'children'),
                dash.dependencies.Output('Webtoon-link-9', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_bert()[0]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-10', 'children'),
                dash.dependencies.Output('Webtoon-img-10', 'src'),
                dash.dependencies.Output('Webtoon-context-10', 'children'),
                dash.dependencies.Output('Webtoon-link-10', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_bert()[1]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-11', 'children'),
                dash.dependencies.Output('Webtoon-img-11', 'src'),
                dash.dependencies.Output('Webtoon-context-11', 'children'),
                dash.dependencies.Output('Webtoon-link-11', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_bert()[2]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

@app.callback([dash.dependencies.Output('Webtoon-name-12', 'children'),
                dash.dependencies.Output('Webtoon-img-12', 'src'),
                dash.dependencies.Output('Webtoon-context-12', 'children'),
                dash.dependencies.Output('Webtoon-link-12', 'href'),],
              [dash.dependencies.Input('webtoon-memo', 'data'),
              dash.dependencies.Input('genre-memo', 'data')])
def webtoon_name_test(webtoon_name, genre):
    model = Recommend(webtoon_name, genre)
    name = model.select_bert()[3]
    return name, model.find_thumb(name), model.find_summary(name), model.find_link(name)

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/recommend':
        return page_recommend_layout
    elif pathname == '/main':
        return main_page
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)