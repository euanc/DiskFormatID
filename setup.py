import os
import warnings

from setuptools import setup

with open(os.path.join('DiskFormatID', '__init__.py')) as init_:
    for line in init_:
        if '__version__' in line:
            version = line.split('=')[-1].strip().replace('"','')
            break
    else:
        version = 'unknown'
        warnings.warn('Unable to find version, using "%s"' % version)
        input("Continue?")


setup(name='DiskFormatID',
      version=version,
      description='Disk Format Identification for KryoFlux',
      author='Euan Cochrane',
      author_email='euanc@foobar.com',
      maintainer = "Euan Cochrane",
      maintainer_email = "euanc@foobar.com",
      url="https://github.com/euanc/DiskFormatID",

      py_modules = ['chooseFormatsGUI', 'chooseFormats', 'diskIDMainGUI'],

      scripts = ['diskIDMain'],

      classifiers = ['Development Status :: 2 - Pre-Alpha'
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Programming Language :: Python",
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.6'
                     "Operating System :: OS Independent",
                     "Topic :: Software Development :: Libraries :: Python Modules"],
      keywords="DiskFormatID")

