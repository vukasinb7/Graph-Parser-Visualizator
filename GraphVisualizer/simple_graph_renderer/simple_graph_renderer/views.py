import pkg_resources
from django.apps.registry import apps
from django.shortcuts import render

from app_core.models import *
from app_core.utils import find_root_nodes


def layout_simple(request):
    g1 = Graph.objects.all()
    pkg_resources.iter_entry_points(group='visualization.load')
    parser_plugins = apps.get_app_config('app_core').parser_plugins
    visualization_plugins = apps.get_app_config('app_core').visualization_plugins
    root_nodes = find_root_nodes(g1[0])
    return render(request, "simple_graph_renderer.html",
                  {'graph': g1[0],
                   "visualization_plugins": visualization_plugins,
                   "parser_plugins": parser_plugins,
                   'root_nodes': root_nodes
                   })