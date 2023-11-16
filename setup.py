# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    },
)
