#!/usr/bin/env python
from setuptools import setup, find_packages
import codecs

VERSION = '1.0.0'

entry_points = {

	"nose.plugins.0.10" : [
		"nosetracebackinfo = nti.nose_traceback_info:NoseTracebackInfoPlugin"
	],

}

setup(
    name = 'nti.nose_traceback_info',
    version = VERSION,
    author = 'Jason Madden',
    author_email = 'open-source@nextthought.com',
    description = ('Include __traceback_info__ in tracebacks printed by nose'),
    long_description = codecs.open('README.rst', encoding='utf-8').read(),
    license = 'GNU LGPL',
    keywords = 'nose exceptions zope',
    url = 'https://github.com/NextThought/nti.nose_traceback_info',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
        ],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	install_requires=[
		'nose >= 1.3.0',
		'zope.exceptions >= 4.0.6'
	],
	entry_points=entry_points
)
