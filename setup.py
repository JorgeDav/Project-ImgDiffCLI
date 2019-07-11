from setuptools import setup

setup(name='imgdif',
      version='0.2',
      description='Compares two images',
      url='http://github.com/storborg/funniest',
      author='DevOps Academy',
      author_email='devopsacamedy@example.com',
      license='MIT',
      packages=['imgdif'],
      zip_safe=False,
      entry_points = {
        'console_scripts': [
            'imgapp=imgdif.command_line:main',
        ]
      }
)
