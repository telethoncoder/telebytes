from setuptools import setup

setup(
    name='telebytes',
    description='custom Telethon class for working with session on server',
    version='1.0.0',
    install_requires=[
        'telethon == 1.30.3',
        'requests'
    ]
)