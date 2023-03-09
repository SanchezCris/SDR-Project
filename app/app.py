from aiohttp import request
from flask import Flask, render_template, request
from sqlalchemy import true


app = Flask(__name__)
app.debug = true


@app.route('/')
def index():

    texto_out = "Aquí va el texto de gnuradio"
    
    data = {
        'titulo': "index123",
        'bienvenida': 'Saludos Cris'
    }
    return render_template('index.html', data = texto_out)


def query_string():
    print(request)

if __name__ == '__main__':
    app.add_url_rule('/queryu_string', view_func=query_string)
    app.run()

#<h2>{{ data.bienvenida }}</h2>
#<h3>{{ data.titulo }}</h3>
