# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    redirect(URL('home'))
    return dict(message=T('Welcome to web2py!'))

def recetas():
    return dict()
# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if not(request.args):
        if auth.is_logged_in():
            redirect(URL('default','home'))
        else:
            redirect(URL('default', 'login'))
    else:
        if request.args[0] == 'login':
            if auth.is_logged_in():
                redirect(URL('default','home'))
            else:
                redirect(URL('default', 'login'))
    return dict(form=auth())

# ---- login ----
def login():
    if auth.is_logged_in():
        redirect(URL('default', 'user', args='logout')) # Si ya hay un usuario conectado, desconectarlo
    return dict(form=auth.login())

@auth.requires_membership('Administrador')
@auth.requires_login()
# ---- Registro ----
def registro():
    registro = SQLFORM(db.usuario)
    if registro.process().accepted:
        response.flash = 'registro Exitoso'
        id = registro.vars.id
        if request.vars.rol == "Cuidador":
            db.auth_membership.insert(user_id = id, group_id=1)
        elif request.vars.rol == "Maestro":
            db.auth_membership.insert(user_id = id, group_id=2)
        elif request.vars.rol == "Representante":
            db.auth_membership.insert(user_id = id, group_id=3)
    elif registro.errors:
        if registro.errors.email:
            response.flash = registro.errors.email
        elif registro.errors.password:
            response.flash = registro.errors.password
        elif registro.errors.first_name:
            response.flash = registro.errors.first_name
        elif registro.errors.last_name:
            response.flash = registro.errors.last_name
        else:
            response.flash = "Error al llenar el formulario"
    else:
        response.flash = 'Por favor complete el formulario'
    return dict(registro=registro)

@auth.requires_login()
def redericcionando():
    if auth.is_logged_in():
        if 'Administrador' in auth.user_groups.values():
            redirect(URL('default', 'home'))
        elif 'Cuidador' in auth.user_groups.values():
            redirect(URL('default', 'homeCuidador'))
        elif 'Maestro' in auth.user_groups.values():
            redirect(URL('default', 'homeMaestro'))
        elif 'Representante' in auth.user_groups.values():
            redirect(URL('default', 'homeNinio'))
    return dict()

@auth.requires_login()
def agregarninio():

    id_usuario = auth.user.id
    usuario = db(db.usuario.id==id_usuario).select().first()
    print(request.vars)
    insertar = SQLFORM(db.kid)
    if insertar.process().accepted:
        response.flash = 'Niño agregado exitosamente'
    elif insertar.errors:
        if insertar.errors.nombre:
            response.flash = insertar.errors.nombre
        elif insertar.errors.apellido:
            response.flash = insertar.errors.apellido
        elif insertar.errors.fecha:
            response.flash = insertar.errors.fecha
        elif insertar.errors.edad:
            response.flash = insertar.errors.edad
        elif insertar.errors.medicamento_alergia:
            response.flash = insertar.errors.medicamento_alergia
        elif insertar.errors.otra_enfermedad:
            response.flash = insertar.errors.otra_enfermedad
        elif insertar.errors.tlf_rep:
            response.flash = insertar.errors.tlf_rep
        elif insertar.errors.direccion:
            response.flash = insertar.errors.direccion
        elif insertar.errors.observacion:
            response.flash = insertar.observacion
        else:
            response.flash = "Error al llenar el formulario"
    else:
        response.flash = 'Por favor complete el formulario'

    return dict(insertar=insertar, usuario=usuario)

@auth.requires_login()
def cambiarninio():
    modificar = FORM()
    if modificar.accepts(request.vars, formname="modificarNinio"):
        if db(db.kid.id == request.vars.Identificador).select():
            session.Identificador = request.vars.Identificador
            redirect(URL('cambiardatosninio'))
        else:
            response.flash = "No existe este indentificador en la Base de datos"
    listaNinios = db(db.kid.representante == auth.user.id).select(db.kid.ALL)
    return dict(listaNinios=listaNinios)

@auth.requires_login()
def cambiardatosninio():
    if request.vars:
        if db(db.kid.id==session.Identificador).update(nombre=request.vars.nuevoNombre,
            apellido=request.vars.nuevoApellido, fecha=request.vars.nuevaFecha, edad=request.vars.nuevaEdad, medicamento_alergia=request.vars.nuevoMedicamento, otra_enfermedad=request.vars.nuevaEnfermedad, tlf_rep=request.vars.nuevoTlf, direccion=request.vars.nuevaDireccion, observacion=request.vars.nuevaObservacion):
            response.flash = "Datos modificados con exito"
        else:
            response.flash = "Los datos no pudieron ser actualizados"
    else:
        response.flash = "Complete el formulario"
    usuario = db(db.kid.id==session.Identificador).select(db.kid.ALL).first()
    return dict(usuario=usuario)

# ---- Home principal ----
def home():
    return dict()

# ---- Home para interaccion del ninio ----
@auth.requires_membership('Representante')
@auth.requires_login()
def homeNinio():
    return dict()

@auth.requires_login()
@auth.requires_membership('Maestro')
def homeMaestro():
    return dict()

@auth.requires_login()
@auth.requires_membership('Cuidador')
def homeCuidador():
    return dict()

@auth.requires_login()
def mostrarCalendario():
    return dict()

@auth.requires_login()
def modificarCalendario():
    return dict()

@auth.requires_login()
def actividadesA():
    return dict()

@auth.requires_login()
def actividadesM():
    return dict()

@auth.requires_login()
def actividadesL():
    return dict()

@auth.requires_login()
def actividadesV():
    return dict()

@auth.requires_login()
def calendario():
    return dict()

@auth.requires_login()
def estadisticas():
    return dict()

@auth.requires_login()
def administrar_usuario():
    grid = SQLFORM.grid(db.usuario)
    return dict(grid=grid)
