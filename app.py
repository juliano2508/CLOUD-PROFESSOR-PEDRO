from flask import Flask
import json
import psutil
import os
import platform


print(psutil.cpu_percent(percpu=True))

print(psutil.virtual_memory().used / 1024 ** 2)

print(os.getpid())

print(platform.platform())



APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        [{'integrantes': [
            'João das Couves',
            'Gumercindo da Silva',
            'Pedro Rocha Horchulhack'
        ]
        }]
    ])
