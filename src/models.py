from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    manager = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='project')

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_id, status):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.status = status

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    assigned_user = Column(String)
    status = Column(String, default='pending')
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', back_populates='tasks')
