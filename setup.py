#!/usr/bin/env python
from setuptools import setup, find_packages

test_deps = [
    'coverage',
    'pytest-cov',
    'pytest-timeout',
    'pytest',
]

extras = {
    'testing': test_deps,
}

setup(
    name='know',
    version='0.1',
    description='Tool for manicuring a digital garden',
    author='Ryan Harter',
    author_email='harterrt@gmail.com',
    url='https://github.com/harterrt/know-cli.git',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'know = know.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=[
        'click',
    ],
    tests_require=test_deps,
    extras_require=extras,
)
