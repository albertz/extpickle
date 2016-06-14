

from distutils.core import setup
import time


# Usage:
# Registering the project: python setup.py register
# New release: python setup.py sdist upload
# See also MANIFEST.in for included files.


setup(
	name = 'extpickle',
	version = time.strftime("1.%Y%m%d.%H%M%S", time.gmtime()),
	packages = ['extpickle'],
	package_dir = {'extpickle': ''},
	description = 'extended pickle',
	author = 'Albert Zeyer',
	author_email = 'albzey@gmail.com',
	url = 'https://github.com/albertz/extpickle',
	license = '2-clause BSD license',
	long_description = open('README.rst').read(),
	# https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: BSD License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		]
)
