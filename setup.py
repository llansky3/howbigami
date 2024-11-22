# To create a distribution relase: 
# python3 setup.py sdist
# git tag $(cat version.txt)

from setuptools import setup, find_packages

with open('version.txt') as f:
    version = f.read()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='howbigami',
    version=version,
    description='Treemap visualization of component sizes',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Lukas Lansky',
    author_email='lukas.lansky@suse.com',
    url='https://github.com/llansky3/howbigami',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)



