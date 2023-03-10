from aiohttp import request
import time
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from threading import Thread
#import zmq.green as zmq
import pmt
from sqlalchemy import true
import pyaudio
import zmq
import numpy as np
import matplotlib.pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:55555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

for i in range(10):
    if socket.poll(10) !=0:
        msg = socket.recv()
        print(len(msg))
        data = np.frombuffer(msg, dtype=np.complex64, count=-1)
        print(data[0:10])
        #plt.plot(np.real(data))
        #plt.plot(np.imag(data))
        #plt.show()
    else:
        time.sleep(0.1)

"""
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2000')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

for i in range(10):
    try:
        message = socket.recv()
        #print (message)
        print ("Recibiendo correctamente")
    except:
        print ("PORT:%d: Error receiving messages")


"""

"""

app = Flask(__name__)
app.debug = true


@app.route('/')
def index():

    texto_out = "Aquí va el texto de gnuradio"
    
    data = {
        'titulo': "index123",
        'bienvenida': 'Saludos'
    }
    return render_template('index.html', data = texto_out)


def query_string():
    print(request)

if __name__ == '__main__':
    app.add_url_rule('/queryu_string', view_func=query_string)
    app.run()

"""


#<h2>{{ data.bienvenida }}</h2>
#<h3>{{ data.titulo }}</h3>
