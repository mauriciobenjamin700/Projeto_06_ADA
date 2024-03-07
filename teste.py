# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

#definindo a base de dados
df = pd.read_csv("dataset.csv")

produtos = list(df["article"].unique())
produtos.append("Todos os Produtos")
default = "CROISSANT"

#criando o gráfico
fig = px.bar(df, x="article", y="Quantity", color="article", barmode="group")

# preparando a página 
app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children="Gráfico com o faturamente de todos os produtos separados por loja"),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produto vendidos, não o faturamento.
    '''),
    html.Div(id="texto"),

    dcc.Dropdown(options=produtos, value=default,id="Lista_Produtos"),
    dcc.Graph(
        id='Grafico-Quantidade_Venda',
        figure=fig
    )
])

#chamadas de função sempre no final do projeto

@app.callback(
    Output("texto", "children"),
    Input("Lista_Produtos","value")
)

def update_output(value):
    return "you have selected {value}"

if __name__ == '__main__':
    app.run(debug=True)
