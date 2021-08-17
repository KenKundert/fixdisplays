from setuptools import setup
from textwrap import dedent
import sys

if sys.version_info < (3,6):
    sys.exit('requires python3.6 or better.')

setup(
    name = 'fixdisplays',
    version = '1.1',
    description = dedent("Controls which screens are used"),
    author = "Ken Kundert",
    author_email = 'theNurd@nurdletech.com',
    scripts = 'fixdisplays'.split(),
    install_requires = 'docopt inform>=1.15 shlib'.split(),
    zip_safe = True,
    download_url = 'https://github.com/kenkundert/fixdisplays/tarball/master',
    license = 'GPLv3',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)

# vim: set sw=4 sts=4 et:
