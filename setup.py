from setuptools import setup


setup(name='Books UNAM API',
      version='1.0',
      description='API for find books of the National Autonomous University of Mexico (UNAM)',
      author='Rigoberto Canseco',
      author_email='rigobertocanseco@gmail.com',
      url='',
      install_requires=[
            'Flask>=0.10.1',
            'sqlalchemy>=1.0.12'],
     )
