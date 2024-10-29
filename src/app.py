from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Rutas para crear proyectos y asignar tareas
@app.route('/proyectos', methods=['POST'])
def crear_proyecto():
    data = request.get_json()
    # Lógica para crear un proyecto
    return jsonify({"mensaje": "Proyecto creado exitosamente"}), 201

@app.route('/tareas', methods=['POST'])
def asignar_tarea():
    data = request.get_json()
    # Lógica para asignar una tarea
    return jsonify({"mensaje": "Tarea asignada exitosamente"}), 201

# Manejo de errores
@app.errorhandler(404)
def recurso_no_encontrado(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def error_interno(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
