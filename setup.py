"""Setup for installing Rest Helper"""

from setuptools import setup


setup(name='resthelper',
      version='0.1.0',
      description='Creating restful services URLs for testing purposes',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: DevOps',
          'Topic :: Software Development :: Test Tools',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='rest url build config',
      url='https://github.com/rklonner/resthelper',
      author='Robert Klnner',
      author_email='r.klonner@gmx.at',
      license='MIT',
      packages=['resthelper'],
      install_requires=[
          'configparser>=3.5.0',
          'docopt>=0.6.2'
      ],
      entry_points={
          'console_scripts': ['rest_helper=resthelper.rest_helper:main']
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)