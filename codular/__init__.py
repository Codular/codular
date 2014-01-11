from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (DBSession, Base)

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
    config.add_static_view('static', 'static', cache_max_Age=3600)

    config.add_route('home', '/')