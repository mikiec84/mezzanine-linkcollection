# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup, find_packages

NAME = 'mezzanine-linkcollection'
VERSION = '0.2.2'

DESCR = """\
A fairly basic model for maintaining a link list on your site
"""

AUTHOR = u'Markus Törnqvist'
AUTHOR_EMAIL = 'mjt@fadconsulting.com'

URL = 'https://github.com/mjtorn/mezzanine-linkcollection'

setup(
    name=NAME,
    version=VERSION,
    description=DESCR,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
)

# EOF

