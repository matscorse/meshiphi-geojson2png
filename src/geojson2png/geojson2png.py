#!/usr/bin/env python

# Version: 2024-11-11: First version
#
# Author: matsco@bas.ac.uk
#
# Generate PNG summary image from Meshiphi GEOJSON output

import argparse
import os
import geopandas as gpd
import matplotlib.pyplot as plt

_XSCALE = 40
_YSCALE = 30
_DPI = 180

def check_input_filenames(input_filenames: list):
    """
    from the cli arguments create a list of which files
    actually exist.
    """
    list_of_filenames_that_actually_exist = []

    for a_filename in input_filenames:
        if not os.path.isfile(a_filename):
            print("Filename", a_filename, "is not a file (or doesn't exist): Ignoring")
        else:
            list_of_filenames_that_actually_exist.append(os.path.abspath(a_filename))
            print("Including filename:", a_filename)

    return list_of_filenames_that_actually_exist



def convert_to_png(geojson_filepath: os.path, xscale, yscale, dpi):

    df = gpd.read_file(geojson_filepath)
    bounds = df.geometry.total_bounds
    fig, ax = plt.subplots(figsize = (xscale, yscale))

    df.to_crs(epsg=4326).plot(column='SIC', ax=ax, edgecolor='grey', linewidth=0.5, cmap = 'coolwarm')
    df.to_crs(epsg=4326).plot(column='land', ax=ax, edgecolor='brown', linewidth=0.5, cmap = 'copper')

    plt.savefig(geojson_filepath+'.png', dpi=dpi)

    return


def main():
    """
    script entry point
    """
    
    parser = argparse.ArgumentParser(description='Generate PNG summary image from Meshiphi GEOJSON output')
    parser.add_argument("-x", "--xscale", help="WidthScale in inches, default="+str(_XSCALE), action="store", dest='xscale', default=_XSCALE)
    parser.add_argument("-y", "--yscale", help="HeightScale in inches, default="+str(_YSCALE), action="store", dest='yscale', default=_YSCALE)
    parser.add_argument("-d", "--dpi", help="Output resolution DPI, default="+str(_DPI), action="store", dest='dpi', default=_DPI)
    parser.add_argument("files", help="One or more Meshiphi GEOJSON mesh file path(s)", type=str, nargs='+')
    args = parser.parse_args()


    # Now kick off main

    checked_files = check_input_filenames(args.files)

    for geojson_filepath in checked_files:
        convert_to_png(geojson_filepath, args.xscale, args.yscale, args.dpi)



if __name__ == "__main__":
    main()