from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='resthelper',
      version='0.1',
      description='Creating restful services URLs for testing purposes',
      long_description=readme(),
      long_description_content_type='text/x-rst',
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
          'configparser',
          'docopt'
      ],
      entry_points = {
        'console_scripts': ['rest_helper=resthelper.rest_helper:main']
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)