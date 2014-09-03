#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cqlsh',
    version='2.2.0',
    description="CQL Shell for Apache Cassandra",
    long_description="CQL Shell for Apache Cassandra",
    keywords='python cql cassandra cqlsh',
    url='https://github.com/apache/cassandra',
    platforms=['any'],
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=['cqlshlib'],
    scripts = [
        'cqlsh',
    ]
)
