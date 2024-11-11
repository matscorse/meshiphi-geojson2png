# py-meshiphi-geojson2png
Package to generate PNG summary plots from meshiphi GEOJSON meshes

##  

### Installation
Using Python version 3.8.x or higher.
In a base or virtual python environment:  
```
git clone https://github.com/matscorse/py-meshiphi-geojson2png.git geojson2png
cd ./geojson2png
pip install -e .
```  

##  

### Usage
Provide 1 or more paths to geojson mesh file(s). The output `.png` file will be created in the same directory as the source mesh file.  
  
`geojson2png --help`  
```bash
usage: geojson2png [-h] [-x XSCALE] [-y YSCALE] [-d DPI] files [files ...]

Generate PNG summary image(s) from Meshiphi GEOJSON input file(s)

positional arguments:
  files                             One or more Meshiphi GEOJSON mesh file path(s)

options:
  -h,           --help             show this help message and exit
  -x XSCALE,    --xscale XSCALE    WidthScale in inches, default=40
  -y YSCALE,    --yscale YSCALE    HeightScale in inches, default=30
  -d DPI,       --dpi DPI          Output resolution DPI, default=180
```
