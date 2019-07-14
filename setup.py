from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='AX3003P',
      version='0.1',
      author='Krzysztof Adamkiewicz',
      author_email='kadamkiewicz835@gmail.com',
      url='https://github.com/Bill2462/AX3003P',
      description='Package for AX-3003P Programmable DC Power Supply',
      long_description=readme(),
      packages=['AX3003P'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                  ],
     install_requires=[
          'serial',
      ],
     )
