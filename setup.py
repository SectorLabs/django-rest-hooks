import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # if setuptools breaks

# Dynamically calculate the version
version_tuple = __import__('rest_hooks').VERSION
version = '.'.join([str(v) for v in version_tuple]) + '+sl.1'

setup(
    name = 'django-rest-hooks',
    description = 'A powerful mechanism for sending real time API notifications via a new subscription model.',
    version = os.environ.get('VERSION', version),
    author = 'Bryan Helmig',
    author_email = 'bryan@zapier.com',
    url = 'http://github.com/zapier/django-rest-hooks',
    install_requires=['Django>=1.5', 'requests'],
    packages=['rest_hooks'],
    package_data={
        'rest_hooks': [
            'migrations/*.py',
            'south_migrations/*.py'
        ]
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
