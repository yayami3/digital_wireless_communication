from setuptools import setup, find_packages

setup(
    name='dwcpy',
    version='0.0.1',
    description='Sample package for Digital Wireless Communication',
    #long_description=readme,
    author='yayami3',
    author_email='yayami355@gmail.com',
    install_requires=['numpy'],
    url='https://github.com/yayami3',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite = 'tests'
)
