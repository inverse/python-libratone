from libratone import __version__
from distutils.core import setup

setup(
    name='libratone-client',
    version=__version__,
    description='A Libratone Python library',
    author='Malachi Soord',
    license='MIT',
    url='https://github.com/inverse/libratone-client',
    py_modules=['libratone'],
)
