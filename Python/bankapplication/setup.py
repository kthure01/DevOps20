from setuptools import setup, find_packages


setup(
    name='bankapp',
    version='1.0.0',
    install_requires=[
        'mongoengine',
        'flask',
        'pymongo',
        'bson',
        'wtforms'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)
