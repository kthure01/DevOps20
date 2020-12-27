from setuptools import setup, find_packages

setup(
    name='',
    version='',install_requires=[
        'pytest',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)

# $ python3 setup.py develop
# $ virtualenv -p /usr/bin/python3.9 ./venv
# $ source ./venv/bin/activate
# $ python3 setup.py develop
# $ pytest
