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
    return dict()

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
def actividades():
    return dict()

@auth.requires_login()
def calendario():
    return dict()