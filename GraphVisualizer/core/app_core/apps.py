import pkg_resources
from django.apps import AppConfig


class AppCoreConfig(AppConfig):
    name = "app_core"
    visualization_plugins = []
    parser_plugins = {}

    def ready(self):
        self.visualization_plugins = load_plugins_visualization("visualization.load")
        self.parser_plugins = load_plugins_parser("parser_plugins.load")


def load_plugins_visualization(identifier):
    names = []
    paths = []
    for ep in pkg_resources.iter_entry_points(group=identifier):
        if str(ep).split('=')[0].strip() == 'path':
            paths.append(str(ep).split('=')[1].strip())
        else:
            names.append(str(ep).split('=')[1].strip())
    result = []
    for i in range(len(names)):
        result.append([paths[i], names[i]])

    return result


def load_plugins_parser(signature):
    plugins = []
    names = []
    types = []
    extensions = []
    for ep in pkg_resources.iter_entry_points(group=signature):
        if str(ep).split('=')[0].strip() == 'parser':
            p = ep.load()
            plugin = p()
            plugins.append(plugin)
        elif str(ep).split('=')[0].strip() == 'name':
            names.append(str(ep).split('=')[1].strip())
        elif str(ep).split('=')[0].strip() == 'type':
            types.append(str(ep).split('=')[1].strip())
        elif str(ep).split('=')[0].strip() == 'ext':
            extensions.append(str(ep).split('=')[1].strip())

    results = {}
    for i in range(len(plugins)):
        result = {"name": names[i], "type": types[i], "ext": extensions[i], "plugin": plugins[i]}
        results[names[i]] = result

    return results
