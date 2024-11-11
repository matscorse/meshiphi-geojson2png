# py-meshiphi-geojson2png
Package to generate PNG summary plots from meshiphi GEOJSON meshes

##  

### Installation
It is recommended that the py-meshiphi-geojson2png package is installed and used within a Python virtual environment. The Python version must be >= 3.9.x .  

To create a Python virtual environment:  
```
python -m venv path_to_new_virtual_env
```
  
Then activate the python virtual environment:  
```
source path_to_new_virtual_env/bin/activate
```  

Once activated, install the py-meshiphi-geojson2png package and it's dependencies into the python virtual environment:  
```
git clone https://github.com/matscorse/py-meshiphi-geojson2png.git geojson2png
cd ./geojson2png
pip install -e .
```  

You may wish to create a symbolic link to the virtual python environment for using this package:  
```
ln -s <path-to-python-venv>/activate <cloned-directory>/activate
```
This way you can easily locate and activate the virtual environment to use this package.

##  

### Usage