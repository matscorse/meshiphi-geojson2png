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

def convert():
    df = gpd.read_file('amsr_southern_SDA.vessel.geojson')

    bounds = df.geometry.total_bounds

    fig, ax = plt.subplots(figsize = (_XSIZE,_YSIZE))

    df.to_crs(epsg=4326).plot(column='SIC', ax=ax, edgecolor='grey', linewidth=0.5, cmap = 'coolwarm')

    df.to_crs(epsg=4326).plot(column='land', ax=ax, edgecolor='brown', linewidth=0.5, cmap = 'copper')

    plt.savefig('amsr_southern_SDA.vessel.geojson.png', dpi=180)


def main():
    """
    script entry point
    """
    
    parser = argparse.ArgumentParser(description='perform action with simple-action-pipeline by supplying a pipeline directory')
    parser.add_argument("action", help="Action for the pipeline to perform. \
                        options are 'build', 'status', 'execute', 'reset', 'halt'.", \
                            type=str, choices=['build', 'status', 'execute', 'reset', 'halt'])
    parser.add_argument("pipeline_directory", help="Pipeline directory to use", nargs="*", default="./")
    parser.add_argument("-d", "--directory", help="Pipeline directory", action="store", dest='pipedir')
    parser.add_argument("-f", "--force-rebuild", help="Force building the pipeline that is already built.", action="store_true", dest='rebuild', default=False)
    parser.add_argument("-s", "--short", help="Output shortened information where supported", action="store_true", dest='short', default=False)
    args = parser.parse_args()


    # Now kick off main

    # What to do if no pipeline directory was supplied
    if (not args.pipedir) and (not args.pipeline_directory):
        logger.warning("No pipeline directory provided. Attempting to use current directory as pipeline.")

    # Keyword switch takes priority over positional switch
    if (args.pipedir):
        args.pipeline_directory = args.pipedir
    
    perform(args.pipeline_directory, args.action, args.rebuild, args.short)


if __name__ == "__main__":
    main()