from distutils.core import setup

setup(name='bulbs_garnish',
      version='0.1',
      description='A set of preprocessors available to process data that comes in from any API. Once processed, it can be stored. Use with matarisvan',
      author='Mahesh Lal',
      author_email='mahesh.2910@gmail.com',
      py_modules=['matarisvan_preprocessors.numeric_preprocessors', 'matarisvan_preprocessors.text_preprocessors']
     )
