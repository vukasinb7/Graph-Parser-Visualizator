from django.apps.registry import apps
from django.shortcuts import redirect


def parser_xml(request, name):
    parser_plugins = apps.get_app_config('app_core').parser_plugins
    parser = parser_plugins['XML']['plugin']
    parser.load_graph(name)
    return redirect('/layout/simple')
