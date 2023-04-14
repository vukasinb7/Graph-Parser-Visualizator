from setuptools import setup, find_packages

setup(
    name="app-core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1'],
    package_data={'app_core': ['templates/*.html', 'static/*.css', 'static/*.js', 'static/*.html']},
    entry_points={
        'apps.load':
            ['app=app_core.apps.AppCoreConfig'],
        'urls.load':
            ['path=app_core.urls']
    },
    zip_safe=False
)
