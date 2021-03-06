import setuptools
from glob import glob


with open('README.md', 'r') as f:
    long_description = f.read()

data_files = []
directories = glob('cvints\\opensets\\detection\\desktopco\\images\\')
for directory in directories:
    files = glob(directory+'*')
    data_files += files

directories = glob('cvints\\opensets\\detection\\desktopco\\annotations\\')
for directory in directories:
    files = glob(directory+'*')
    data_files += files

directories = glob('cvints\\utils\\fonts\\')
for directory in directories:
    files = glob(directory+'*')
    data_files += files

setuptools.setup(
     name='cvints',
     version='0.1',
     author="Vasily Boychuk at al",
     author_email="vasily.m.boychuk@gmail.com",
     description="A lib to solve cv tasks",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/VasilyBoychuk/cvints",
     packages=setuptools.find_packages(),
     package_data={'cvints': data_files},
     # data_files=data_files,
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )


