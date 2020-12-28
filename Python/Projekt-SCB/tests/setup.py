from setuptools import setup, find_packages

setup(
    name='',
    description='',
    version='',install_requires=[
        'pytest',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'do_something = folder.fileName:method_to_run
            '
        ]
    }
)

# $ python3 setup.py develop
# $ virtualenv -p /usr/bin/python3.9 ./venv
# $ source ./venv/bin/activate
# $ python3 setup.py develop
# $ pytest
