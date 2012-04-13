#About

Python script to generate a graticule that will project cleanly (with smooth arcs) at world scale. The graticule should have a dense distribution of internal nodes along it's line, especially along the ±180, ±90 WGS84 bounding box.

Output format is geojson, because it's easy to write as a text file in python. Use ogr2ogr to convert to a SHP file.

By **Alex Mandel** Copyright 2012. 
Modifications by Nathaniel Vaughn KELSO.

#Usage

`python pygraticule.py -s 1 -o outfile.geojson`

There are two script arguments for controlling the density of nodes and the output file name: 

* **s** is the step interval is measured in decimal degrees: generally 69 miles at the equator, but varies at higher latitudes.
* **o** is the outfile. If none is provided, file is auto named in this format: "graticule_1dd.geojson" where the number is the step interval.

## Limitations

* The output is lines, not polygons feature classes.

* The output is a GeoJSON format file, not a SHP format Esri Shapefile.

## Examples

When we project out of WGS84 to another coordinate system that is not cylindrical, we need to have enough intermediate nodes
on the paths so the GIS application shows a "curve". Most GIS do not auto-densify stright lines during the projection
so we need to add these extra nodes in the raw geodata.

Here we see Robinson using enough nodes:

![Zoom previews](https://github.com/nvkelso/pygraticule/raw/master/images/robinson.png)

Box results when nodes are sparse:

![Zoom previews](https://github.com/nvkelso/pygraticule/raw/master/images/box_no_densification.png)

The two superimposed:

![Zoom previews](https://github.com/nvkelso/pygraticule/raw/master/images/robinson_plus_box.png)