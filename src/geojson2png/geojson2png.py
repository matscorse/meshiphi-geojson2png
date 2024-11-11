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

_XSIZE = 40
_YSIZE = 30
_DPI = 180

def check_input_filenames(input_filenames: list):
    """
    from the cli arguments create a list of which files
    actually exist.
    """
    list_of_filenames_that_actually_exist = []

    for a_filename in input_filenames:
        if not os.path.isfile(a_filename):
            print("Filename %s is not a file (or doesn't exist): Ignoring", a_filename)
        else:
            list_of_filenames_that_actually_exist.append(os.path.abspath(a_filename))
            print("Including filename: %s", a_filename)

    return list_of_filenames_that_actually_exist



def convert_to_png(geojson_filepath: os.path, xsize, ysize, dpi):

    df = gpd.read_file(geojson_filepath)
    bounds = df.geometry.total_bounds
    fig, ax = plt.subplots(figsize = (xsize, ysize))
    
    df.to_crs(epsg=4326).plot(column='SIC', ax=ax, edgecolor='grey', linewidth=0.5, cmap = 'coolwarm')
    df.to_crs(epsg=4326).plot(column='land', ax=ax, edgecolor='brown', linewidth=0.5, cmap = 'copper')

    plt.savefig(os.path.join(geojson_filepath, '.png'), dpi=dpi)

    return


def main():
    """
    script entry point
    """
    
    parser = argparse.ArgumentParser(description='Generate PNG summary image from Meshiphi GEOJSON output')
    parser.add_argument("-w", "--widthscale", help="WidthScale in inches", action="store", dest='xsize', default=_XSIZE)
    parser.add_argument("-h", "--heightscale", help="HeightScale in inches", action="store", dest='ysize', default=_YSIZE)
    parser.add_argument("-d", "--dpi", help="Output resolution DPI", action="store", dest='dpi', default=_DPI)
    parser.add_argument("files", help="One or more Meshiphi GEOJSON mesh file path(s)", type=str, nargs='+')
    args = parser.parse_args()


    # Now kick off main

    checked_files = check_input_filenames(args.files)

    for geojson_filepath in checked_files:
        convert_to_png(geojson_filepath, args.xsize, args.ysize, args.dpi)



if __name__ == "__main__":
    main()