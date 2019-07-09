from setuptools import setup

setup(name='imgdif',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['imgdif'],
      zip_safe=False,
      entry_points = {
        'console_scripts': [
            'imgapp=imgdif.command_line:main',
        ]
      }
)
