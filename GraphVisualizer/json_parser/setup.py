from setuptools import setup, find_packages
setup(
    name="json_parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['app-core>=0.1'],
    entry_points={
        'parser_plugins.load':
            ['parser=json_parser.json_to_graph_parser:JsonParser', 'name=JSON', 'type=application', 'ext=json'],
        'apps.load':
            ['app=json_parser.apps.JSONParserConfig'],
        'urls.load':
            ['path=json_parser.urls']
    },
    zip_safe=False
)