from setuptools import setup
from codecs import open
from os import path

setup(
    name='yt_search',
    packages=['yt_search'],
    version='1.1.0.rev1',
    python_requires='>=3.6',
    license='GPLv3',
    url='https://github.com/jun50/yt-search',
    author='jun50',
    author_email='0001jun50@gmail.com',
    description='Search contents on YouTube.',
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    keywords='YouTube API',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.6',
    ]
)
