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

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

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


# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
    
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

def completarDatos():
    return dict()

# ---- Home principal ----
def home():
    return dict()

# ---- Home para interaccion del ninio ----
def homeNinio():
    return dict()

def homeMaestro():
    return dict()

def homeCuidador():
    return dict()

def mostrarCalendario():
    return dict()

def modificarCalendario():
    return dict()

def actividades():
    return dict()

def calendario():
    return dict()