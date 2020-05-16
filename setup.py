import setuptools
from glob import glob


with open('README.md', 'r') as f:
    long_description = f.read()


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
     package_data={'opensets': ['*']},
     data_files=[('', glob('opensets/**/*', recursive=True))],
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )


