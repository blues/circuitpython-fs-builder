from setuptools import setup

setup(
   name='cpy-fs',
   version='1.0',
   description='Create FAT filesystem images for use with CircuitPython.',
   author='Matthew McGowan',
   author_email='mat@blues.com',
   install_requires=['wheel',
                     'appdirs>=1.4.4',
                     'fs>=2.4.15',
                     'pyfatfs>=1.0.5'
                     ],
   packages=['cpyfs'],
   package_data={'cpyfs': ['seed.bin']},
   entry_points={
       'console_scripts': [
         'cpy-fs = cpyfs.makefs:main',
         'cpy-fs-dir = cpyfs.tree:main',
         'uf2conv = cpyfs.uf2conv:main'
      ],
   },
)
