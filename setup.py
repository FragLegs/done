# -*- coding: utf-8 -*-
import os
import setuptools


setuptools.setup(
    name='done-sns-sns',
    version='0.0.1',
    description='Simple command to notify users when process is done_sns',
    author='Shayne Miel',
    author_email='miel.shayne@gmail.com',
    url='https://github.com/FragLegs/done_sns-sns',
    packages=setuptools.find_packages(exclude=['tests*']),
    scripts=['scripts/done-sns',],
    install_requires=['boto3',]
)
