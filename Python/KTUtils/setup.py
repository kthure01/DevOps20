from setuptools import setup

# python3 setup.py develop
setup(
    name='ktutils',
    version='0.0.1',
    author='Kent Thureson',
    tests_require=['pytest'],
    install_requires=[],
    author_email='kent.ho.thureson@gmail.com',
    description='Template',
    long_description='A longer description',
    packages=[],
    extras_require={
        'testing': ['pytest'],
    }
)
