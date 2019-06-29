try: # For pip 10 +
    from pip._internal.req import parse_requirements
except ImportError: 
    from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt')

setup(
    name='samuha',
    version='0.1',
    author='Shishira R Maiya',
    author_email='shishira.maiya96@gmail.com',
    description='samūhā: The clustering library for relatively unknown clustering methods.',
    license='MIT',
    url='http://github.com/abhyantrika/samuha',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_reqs=install_reqs
)
