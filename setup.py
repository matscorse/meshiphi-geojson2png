import setuptools

def get_content(filename):
  with open(filename, "r") as fh:
    return fh.read()

setuptools.setup(
  include_package_data=True,
  name='py-meshiphi-geojson2png',
  version='0.1.0',
  description='meshiphi geojson to PNG python package',
  author='matscorse',
  author_email='matsco@bas.ac.uk',
  package_dir={"": "src"},
  packages=setuptools.find_packages(where='src'),
  install_requires=['geopandas', 'matplotlib'],
  entry_points={
    'console_scripts': ['geojson2png=geojson2png.geojson2png:main']},
  long_description=get_content("README.md"),
  long_description_content_type="text/markdown",
  url="https://www.github.com/matscorse",
  classifiers=[el.lstrip() for el in """Development Status :: Initial
    Intended Audience :: Science/Research
    Intended Audience :: System Administrators
    Intended Audience :: Geo-Spatial
    License :: OSI Approved :: MIT License
    Natural Language :: English
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Topic :: Scientific/Engineering""".split('\n')],
)
