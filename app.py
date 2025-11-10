from flask import Flask, jsonify
import psutil
import os
import platform

# Inicializa o Flask
APP = Flask(__name__)

# Pega o objeto do processo atual para consultar métricas
# [cite: 19, 20]
process = psutil.Process(os.getpid())

@APP.get("/info")
def info():
    """
    Rota /info: Retorna o nome dos integrantes da equipe. [cite: 32]
    """
    integrantes = [
        'Seu Nome Completo Aqui',
        'Nome Colega 2 (se houver)',
        'Nome Colega 3 (se houver)'
    ]
    # Retorna os nomes em formato JSON 
    return jsonify({'integrantes': integrantes})

@APP.get("/metricas")
def metricas():
    """
    Rota /metricas: Retorna as métricas do sistema/processo. [cite: 33]
    """
    
    # (c) Memória usada pelo processo em MB 
    # Usamos o .rss (Resident Set Size)
    memoria_mb = process.memory_info().rss / (1024 * 1024)
    
    # (d) Uso de CPU (do processo) [cite: 22]
    # Usamos um intervalo pequeno para conseguir medir o uso da CPU
    # A primeira chamada sem intervalo sempre retorna 0.0
    cpu_percent = process.cpu_percent(interval=0.1)

    return jsonify({
        # (b) PID do processo 
        'pid': process.pid,
        
        # (c) Memória 
        'memoria_utilizada_mb': memoria_mb,
        
        # (d) CPU [cite: 22]
        'uso_cpu_percent': cpu_percent,
        
        # (e) Sistema Operacional 
        'sistema_operacional': platform.platform()
    })

if __name__ == '__main__':
    APP.run(debug=True)
