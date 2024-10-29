from flask import request, jsonify
from src.models import Project, Task
from src.utils import send_email_notification
from src.app import app, db

@app.route('/proyectos', methods=['POST'])
def crear_proyecto():
    data = request.get_json()
    nuevo_proyecto = Project(
        name=data['name'],
        description=data['description'],
        manager=data['manager']
    )
    db.session.add(nuevo_proyecto)
    db.session.commit()
    return jsonify({"mensaje": "Proyecto creado exitosamente"}), 201

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    data = request.get_json()
    proyecto = Project.query.get(data['project_id'])
    if not proyecto:
        return jsonify({"error": "Proyecto no encontrado"}), 404
    nueva_tarea = Task(
        name=data['name'],
        description=data['description'],
        assigned_user=data['assigned_user'],
        project_id=data['project_id']
    )
    proyecto.add_task(nueva_tarea)
    db.session.add(nueva_tarea)
    db.session.commit()
    send_email_notification(nueva_tarea.assigned_user, "Nueva tarea asignada", f"Se te ha asignado una nueva tarea: {nueva_tarea.name}")
    return jsonify({"mensaje": "Tarea agregada exitosamente"}), 201

@app.route('/tareas/<int:task_id>', methods=['PUT'])
def actualizar_estado_tarea(task_id):
    data = request.get_json()
    tarea = Task.query.get(task_id)
    if not tarea:
        return jsonify({"error": "Tarea no encontrada"}), 404
    tarea.status = data['status']
    db.session.commit()
    send_email_notification(tarea.assigned_user, "Estado de tarea actualizado", f"El estado de tu tarea '{tarea.name}' ha sido actualizado a: {tarea.status}")
    return jsonify({"mensaje": "Estado de tarea actualizado exitosamente"}), 200
