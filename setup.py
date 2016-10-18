from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pymetamap',
      version='0.11',
      description='Python wrapper around MetaMap',
      long_description=readme(),
      url='https://github.com/justinsowhat/pymetamap',
      author='Anthony Rios, Justin So',
      author_email='anthonymrios@gmail.com, q.justin.so@gmail.com',
      classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English'
      ],
      license='Apache 2.0',
      packages=['pymetamap'],
      zip_safe=False)

