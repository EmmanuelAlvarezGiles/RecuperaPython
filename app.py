"""
Examen Unidad III
Autor: Emmanuel Alvarez Giles
Fecha: 5 de Noviembre de 2025

Descripción:
Objetivo del examen
Desarrollar una API básica con Flask que permita:

Crear un diccionario de dispositivos de red.
Agregar nuevos dispositivos.
Modificar dispositivos existentes.
Mostrar un listado de todos los dispositivos en formato HTML,
donde cada dispositivo se muestre en una <table> con nombre,
descripción y características

Ejemplo:
   
<table>
        <thead>
            <tr>id</tr>
        </thead>

        <tbody>
            <tr>router01</tr>
        </tbody>
</table>
       
Requisitos técnicos

Usar Flask.
Usar un diccionario como estructura principal de almacenamiento.
Implementar al menos tres rutas:

GET /dispositivos_html: muestra todos los dispositivos en HTML.
POST /dispositivos: agrega un nuevo dispositivo.
PUT /dispositivos/<id>: modifica un dispositivo existente.

Ejemplo del Diccionario de dispositivos: (Estos dispositivos no deben estar almecenas en el archivo, necesitas ser agregados usando postman)
{
  "id": "router01",
  "nombre": "Router Principal",
  "descripcion": "Router de borde para salida a Internet",
  "ip": "192.168.1.1",
  "mac": "00:1A:2B:3C:4D:5E",
  "ubicacion": "Sala de servidores",
  "tipo": "Router",
  "otros": ""
}

Recuerda tener al menos 3 commits en tu repositorio.

Para puntos extra
Puedes ocupar css para añadir puntos a tu examen, perzonalizalo con estilos como el siguiente:
<style>
    .dispositivo {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
    }
</style>
También puedes añadir más css de la forma en la que prefieras.

Puntos extra para añador formula en el cmapo de otros
la formula es la siguente:

último octeto de la IP * 3 + longitud del nombre del dispositivo + ":" + nombre (Cambiando los espacios por _)

"""
from flask import Flask, jsonify, render_template_string, request, redirect, url_for
import os
import json

app = Flask(__name__)

ARCHIVO_JSON = "dispositivos.json"

if os.path.exists(ARCHIVO_JSON):
    with open(ARCHIVO_JSON, "r") as archivo:
        dispositivos = json.load(archivo)
else:
    dispositivos = {}

def guardar_datos():
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(dispositivos, archivo, indent=4)

@app.route('/dispositivos_html')
def ver_html():
    pagina_html = """
    <style>
        .dispositivo { border:1px solid #ccc; padding:10px; margin:10px; border-radius:5px; background-color:white; }
        body { font-family: Arial; background-color:#f4f4f4; }
    </style>
    <h1>Listado de Dispositivos</h1>
    """
    
    for dispositivo in dispositivos.values():
        partes_ip = dispositivo['ip'].split('.')
        ultimo_octeto = int(partes_ip[-1]) if len(partes_ip) == 4 else 0
        formula = f"{ultimo_octeto * 3 + len(dispositivo['nombre'])}:{dispositivo['nombre'].replace(' ', '_')}"
        
        pagina_html += f"""
        <div class='dispositivo'>
            <h3>{dispositivo['nombre']}</h3>
            <p><strong>IP:</strong> {dispositivo['ip']}</p>
            <p><strong>Tipo:</strong> {dispositivo['tipo']}</p>
            <p><strong>Fórmula:</strong> {formula}</p>
        </div>
        """
    
    return pagina_html
   
if __name__ == '__main__':
    app.run(debug=True)