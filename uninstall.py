import os

ENV = "venv"        # virtual environment name
PLUGINS = [
    "xml_parser",
    "json_parser",
    "simple_graph_renderer",
    "detailed_graph_renderer",
    "app_core"
]

def main():
    for plugin in PLUGINS:
        os.system("pip uninstall {}".format(plugin))

if __name__ == "__main__":
    main()