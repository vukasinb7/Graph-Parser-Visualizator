from setuptools import setup, find_packages
setup(
    name="detailed_graph_renderer",
    version="0.1",
    packages=find_packages(),
    package_data={'detailed_graph_renderer':['templates/*.html']},
    entry_points={
'visualization.load':
            ['path=detailed','name=Detailed'],
        'apps.load':
            ['app=detailed_graph_renderer.apps.DetailedGraphRendererConfig'],
        'urls.load':
            ['path=detailed_graph_renderer.urls']
    },
    zip_safe=False
)