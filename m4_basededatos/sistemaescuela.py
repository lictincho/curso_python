"""
Sistema para una escuela. Permite registrar nuevos alumnos, profesores y cursos.

Se crean clases para una tabla alumno, una profesor, una curso y una horario.

Cada alumno es asignado a un curso unico.
Cada curso puede tener asociado más de un profesor y más de un alumno.
Cada profesores tienen un horario que indica cuando están en cada curso.
El horario asociará un curso y un profesor para un día de la semana, 
una hora desde y una hora hasta.

El sistema permitirá exportar los alumnos que pertenecen a un curso, 
el horario de cada profesor y el horario del curso.
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import ForeignKey

# creacion de base de datos en memoria
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

# Tabla de asociacion para relacion muchos a muchos
association_table = Table('association', Base.metadata,
                          Column('curso_id', Integer, ForeignKey('curso.id')),
                          Column('profesor_id', Integer, ForeignKey('profesor.id'))
)

# crea clase para definir la tabla y las columnas
class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre = Column(String)

    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso", back_populates="alumnos")

    def __repr__(self):
        return f"Alumno({self.nombre})"

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)

    curso = relationship("Curso",
                         secondary = association_table,
                         back_populates="profesores")

    def __repr__(self):
        return f"Profesor({self.nombre})"
    
class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)

    alumnos = relationship("Alumno", back_populates="curso")
    profesores = relationship("Profesor",
                         secondary = association_table,
                         back_populates="curso")
    horarios = relationship("Horario", back_populates="curso")

    def __repr__(self):
        return f"Curso({self.nombre})"
    
class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horarios_id_seq'), primary_key=True)
    dia_semana = Column(String)
    hora_desde = Column(String)
    hora_hasta = Column(String)
    
    curso_id = Column (Integer, ForeignKey("curso.id"))
    profesor_id = Column(Integer, ForeignKey("profesor.id"))

    curso = relationship("Curso", back_populates="horarios")
    profesor = relationship("Profesor")
    
    def __repr__(self):
        return f"Horario({self.dia_semana} {self.hora_desde}-{self.hora_hasta})"
    
Base.metadata.create_all(engine)

# Inicia una sesion
Session = sessionmaker(bind=engine)
session = Session()

"""
Ejemplo que crea una base de datos
"""

curso1 = Curso(nombre='Química')
curso2 = Curso(nombre='Programación')
profesor1 = Profesor(nombre='Prof. Ortega Martín')
profesor2 = Profesor(nombre='Prof. Gullino Mauro')
alumno1 = Alumno(nombre='Jordi Polla', curso=curso1)
alumno2 = Alumno(nombre='Mariah Carey', curso=curso2)

horario1 = Horario(dia_semana='Lunes', hora_desde='08:00', hora_hasta='10:00', curso=curso1, profesor=profesor1)
horario2 = Horario(dia_semana='Jueves', hora_desde='11:00', hora_hasta='12:00', curso=curso2, profesor=profesor2)

curso1.profesores.append(profesor1)
curso2.profesores.append(profesor2)

session.add_all([curso1, curso2, profesor1, profesor2, alumno1, alumno2, horario1, horario2])

# Finalizo la sesion
session.commit()

"""
Ejemplo para exportar alumnos que pertenecen a un curso
"""

curso = session.query(Curso).filter_by(nombre='Química').first()
alumnos = curso.alumnos
for alumno in alumnos:
    print(alumno)

"""
Ejemplo para exportar el horario de un curso
"""

horarios = curso.horarios
for horario in horarios:
    print(horario)

"""
Ejemplo para exportar los profesores de un curso
"""

profes = curso.profesores
for profe in profes:
    print (profe)