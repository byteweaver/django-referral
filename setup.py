import os
from setuptools import setup, find_packages

import referral


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-referral',
    version=referral.__version__,
    description='A small django application for marketing using referral links',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='akuryou',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-referral',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
