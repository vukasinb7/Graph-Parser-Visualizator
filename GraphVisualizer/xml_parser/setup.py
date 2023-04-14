from setuptools import setup, find_packages

setup(
    name="xml_parser",
    version="0.1",
    packages=find_packages(),
    install_requires=['app-core>=0.1'],
    entry_points={
        'parser_plugins.load':
            ['parser=xml_parser.xml_to_graph_parser:XmlParser', 'name=XML', 'type=text', 'ext=xml'],
        'apps.load':
            ['app=xml_parser.apps.XMLParserConfig'],
        'urls.load':
            ['path=xml_parser.urls']
    },
    zip_safe=False
)
