from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='howbigami',
    version='0.1.0',
    description='Treemap visualization of component sizes',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Lukas Lansky',
    author_email='lukas.lansky@suse.com',
    url='https://github.com/llansky3/howbigami',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')
)

