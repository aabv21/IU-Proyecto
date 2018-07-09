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

# ---- Registro ----
def registro():
    registro = SQLFORM(db.usuario)
    if registro.process().accepted:
        response.flash = 'registro Exitoso'
        redirect(URL('default', 'login'))
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
    #print(request.vars)
    return dict(registro=registro)

@auth.requires_login()
def completarDatos():
    id_usuario = auth.user.id
    insertar = SQLFORM(db.kid)
    if insertar.process().accepted:
        response.flash = 'Materia agregado exitosamente'
        if not db.usuario.kid:
            db.usuario.kid.insert(insertar.vars.id)
    elif insertar.errors:
        if insertar.errors.nombre:
            response.flash = insertar.errors.nombre
        elif insertar.errors.apellido:
            response.flash = insertar.errors.apellido
        elif insertar.errors.genero:
            response.flash = insertar.errors.genero
        elif insertar.errors.fecha:
            response.flash = insertar.errors.fecha
        elif insertar.errors.edad:
            response.flash = insertar.errors.edad
        elif insertar.errors.medicamento_alergia:
            response.flash = insertar.errors.medicamento_alergia
        elif insertar.errors.otra_enfermedad:
            response.flash = insertar.errors.otra_enfermedad
        elif insertar.errors.correo_rep:
            response.flash = insertar.errors.correo_rep
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

    ninio = db(db.kid.representante == id_usuario).select().first()
    if ninio:
        nombre = ninio.nombre
        apellido = ninio.apellido
        genero = ninio.genero
        fecha = ninio.fecha
        edad = ninio.edad
        medicamento_alergia = ninio.medicamento_alergia
        otra_enfermedad = ninio.otra_enfermedad
        correo_rep = ninio.correo_rep
        tlf_rep = ninio.tlf_rep
        direccion = ninio.direccion
        observacion = ninio.observacion
    else:
        nombre = ""
        apellido = ""
        genero = ""
        fecha = ""
        edad = ""
        medicamento_alergia = ""
        otra_enfermedad = ""
        correo_rep = ""
        tlf_rep = ""
        direccion = ""
        observacion = ""
    print(ninio)

    return dict(insertar=insertar, nombre=nombre, apellido=apellido, genero=genero, fecha=fecha,
            edad=edad, medicamento_alergia=medicamento_alergia, otra_enfermedad=otra_enfermedad,
            correo_rep=correo_rep, tlf_rep=tlf_rep, direccion=direccion, observacion=observacion)

# ---- Home principal ----
def home():
    return dict()

# ---- Home para interaccion del ninio ----
@auth.requires_login()
def homeNinio():
    return dict()

@auth.requires_login()
def homeMaestro():
    return dict()

@auth.requires_login()
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
