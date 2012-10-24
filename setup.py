try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Create HTML markup with python',
    'author': 'Angel Medrano',
    'url': '',
    'download_url': '',
    'author_email': 'asmedrano@gmail.com',
    'version': '0.1.0',
    'install_requires': [
        'beautifulsoup4>=4.1.3'
        ],
    'packages': ['pylmth','pylmth.tests'],
    'scripts': ['bin/build_dom_classes.py'],
    'name': 'pylmth'
}

setup(**config)
