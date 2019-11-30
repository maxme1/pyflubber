from setuptools import setup, find_packages

from pyflubber import __version__

classifiers = '''Development Status :: 5 - Production/Stable
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6'''

with open('README.md', encoding='utf-8') as file:
    long_description = file.read()

with open('requirements.txt', encoding='utf-8') as file:
    requirements = file.read().splitlines()

setup(
    name='pyflubber',
    packages=find_packages(include=('pyflubber',)),
    version=__version__,
    descriprion='Linear interpolation of open and closed lines.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/maxme1/pyflubber',
    download_url='https://github.com/maxme1/pyflubber/v%s.tar.gz' % __version__,
    keywords=[],
    classifiers=classifiers.splitlines(),
    install_requires=requirements,
)
