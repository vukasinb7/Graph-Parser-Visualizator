import os

ENV = "venv"        # virtual environment name
PLUGINS = [
    "core",
    "xml_parser",
    "json_parser",
    "simple_graph_renderer",
    "detailed_graph_renderer"
]

def main():
    os.chdir('./GraphVisualizer')
    for plugin in PLUGINS:
        os.chdir('./{}'.format(plugin))
        os.system('cmd /c "python setup.py install"')
        os.chdir('..')

    

if __name__ == "__main__":
    main()