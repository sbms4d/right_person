#!/usr/bin/env python
# -*- coding: utf-8 -*-


BASE_IMAGE = {
    'Owners': ['099720109477'],
    'Filters': [
        {
            'Name': 'name',
            'Values': [
                'ubuntu/images/*ubuntu-bionic-18.04-amd64-server-*'
            ]
        },
        {
            'Name': 'root-device-type',
            'Values': [
                'ebs']
        },
        {
            'Name': 'virtualization-type',
            'Values': [
                'hvm'
            ]
        }
    ]
}


SPARK_DIRECTORY = '/home/ubuntu/spark/'


APT_DEPENDENCIES = [
    'python',
    'htop',
    'python-pip',
    'ntp',
    'pkg-config',
    'rsyslog',
    'strace',
    'tcl',
    'unzip',
    'openjdk-8-jdk',
]

PYTHON_DEPENDENCIES = [
    'pip',
    'wheel',
    'setuptools',
]

PACKAGE_DEPENDENCIES = [
    'future',
    'boto3>=1.9.123',
    'mmh3',
    'numpy',
    'requests',
    'scipy==1.1.0',
    'scikit-learn<0.21; python_version<"3.0"',
    'scikit-learn; python_version>"3.0"',
    'ujson',
    'six',
    'ioteclabs-wrapper',
    'retrying',
    'urllib3<1.25'
]

NAME_FORMAT = 'SPARK_DATA_MINER-{}'
