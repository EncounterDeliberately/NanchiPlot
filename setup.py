# -*- coding: utf-8 -*-
import site
import os.path
import glob
from setuptools import setup, find_packages

MODULE_NAME = "nanchi"

#IMAGES_DIR = 'img'
#HELP_DIR = 'help'

GET_IMAGES = glob.glob(os.path.join(MODULE_NAME,"img/*.png"))
GET_IMAGES = [k.replace("nanchi\\","") for k in GET_IMAGES]
GET_DATA_SAMPLES = glob.glob(os.path.join(MODULE_NAME,"data/*.*"))
GET_DATA_SAMPLES = [k.replace("nanchi\\","") for k in GET_DATA_SAMPLES]

PACK_DATA = GET_IMAGES + ['help/about.html', 'help/nanchi_logo.png'] + GET_DATA_SAMPLES

setup(
    name= MODULE_NAME,
    version='0.1.0',
    description='Plotting with wxPython, NumPy and Matplotlib',
    author='Pedro Jorge De Los Santos',
    author_email='delossantosmfq@gmail.com',
    license = "MIT",
    keywords=["Plotting"],
    install_requires=["matplotlib","numpy","wxPython"], # Also required wxPython
    url='https://github.com/JorgeDeLosSantos/NanchiPlot',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'nanchi=nanchi.app:run',
        ]
    },
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Science/Research",
      "Intended Audience :: End Users/Desktop",
      "Environment :: Win32 (MS Windows)",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: Implementation :: CPython",
      "Topic :: Desktop Environment",
      "Topic :: Scientific/Engineering :: Visualization",
      "Topic :: Multimedia :: Graphics",
      "Topic :: Utilities",
    ],
    package_data={"nanchi": PACK_DATA}
)
