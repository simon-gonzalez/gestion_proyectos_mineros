from flask import Blueprint, request, jsonify
from src.controllers import crear_proyecto, agregar_tarea, actualizar_estado_tarea

routes = Blueprint('routes', __name__)

@routes.route('/proyectos', methods=['POST'])
def crear_proyecto_route():
    return crear_proyecto()

@routes.route('/tareas', methods=['POST'])
def agregar_tarea_route():
    return agregar_tarea()

@routes.route('/tareas/<int:task_id>', methods=['PUT'])
def actualizar_estado_tarea_route(task_id):
    return actualizar_estado_tarea(task_id)
