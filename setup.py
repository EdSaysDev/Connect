from distutils.core import setup

setup(name='connect',
      version='0.1',
      description='Simple module to connect to a serial device',
      url='https://github.com/ed-raspberrypi/connect',
      author='Edward Lancaster',
      author_email='ed.raspberrypi@gmail.com',
      license='None',
      packages=['connect'],
      install_requires=['pyserial','setuptools'],
      )
