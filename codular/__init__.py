from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (DBSession, Base)
from .views import (ViewHome, ViewUsers)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("templates")
    config.include(add_routes)
    config.scan()
    return config.make_wsgi_app()

def add_routes(config):
    # Splitted from main() to be used in unit test and better visibility
    config.add_static_view('static', 'static', cache_max_age=3600)

    """
    /resources          GET / POST      show / create
    /resources/new      GET             new form
    /resources/$id      GET / DELETE    show id / delete id
    /resources/$id/edit GET / POST      edit form / edit
    """

    # View Home
    config.add_route('home',        '/',                        request_method='GET')

    # View Users
    config.add_route('users',       '/users',                   request_method='GET')
    config.add_route('update_user', '/users',                   request_method='POST')
    config.add_route('new_user',    '/users/new',               request_method='GET')
    config.add_route('delete_user', '/users/{id}/delete',       request_method='GET')
    config.add_route('edit_user',   '/users/{id}/edit',         request_method='GET')
    config.add_route('user',        '/users/{id}',              request_method='GET')

