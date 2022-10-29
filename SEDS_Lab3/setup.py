from setuptools import setup

setup(
   name='<your_package_name>',
   version='1.0.0',
   author='<author_name>',
   author_email='<author_email>',
   packages=['<your_package_name>'],
   url='http://pypi.python.org/pypi/<your_package_name>/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=['<your_package_name>']
)