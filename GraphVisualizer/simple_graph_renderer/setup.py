from setuptools import setup, find_packages
setup(
    name="simple_graph_renderer",
    version="0.1",
    packages=find_packages(),
    package_data={'simple_graph_renderer':['templates/*.html']},
    entry_points={
        'visualization.load':
            ['path=simple','name=Simple'],
        'apps.load':
            ['app=simple_graph_renderer.apps.SimpleGraphRendererConfig'],
        'urls.load':
            ['path=simple_graph_renderer.urls']
    },
    zip_safe=False
)