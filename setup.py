import runpy
from pathlib import Path

from setuptools import setup, find_packages

classifiers = '''Development Status :: 5 - Production/Stable
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9'''

name = 'pyflubber'
root = Path(__file__).parent
with open(root / 'README.md', encoding='utf-8') as file:
    long_description = file.read()
with open(root / 'requirements.txt', encoding='utf-8') as file:
    requirements = file.read().splitlines()
version = runpy.run_path(root / name / '__version__.py')['__version__']

setup(
    name=name,
    packages=find_packages(include=(name,)),
    include_package_data=True,
    version=version,
    descriprion='Linear interpolation of open and closed lines.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/maxme1/pyflubber',
    download_url='https://github.com/maxme1/pyflubber/v%s.tar.gz' % version,
    keywords=['interpolation', 'curves'],
    classifiers=classifiers.splitlines(),
    install_requires=requirements,
)
