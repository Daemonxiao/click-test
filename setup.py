from setuptools import setup

setup(
    name='typer-test-demo',
    version='1.0',
    packages=['cli'],
    include_package_data=True,
    install_requires=[
        'typer'
    ],
    entry_points='''
        [console_scripts]
        clickctl=cli.main:main
    ''',
)