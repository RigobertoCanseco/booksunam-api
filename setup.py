from setuptools import setup


setup(name='Books UNAM API',
      version='1.0',
      description='API for find books of the National Autonomous University of Mexico (UNAM)',
      author='Rigoberto Canseco',
      author_email='rigobertocanseco@gmail.com',
      url='',
      install_requires=[
            'Flask>=0.10.1',
            'sqlalchemy>=1.0.12',
            'Flask-RESTful>=0.3.5',
            'Flask-HTTPAuth>=3.2.3',
            'marshmallow>=3.0.0.b2',
            'beautifulsoup4>=4.6.0'
      ],
     )
