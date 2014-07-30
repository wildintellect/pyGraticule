PyGraticule
================

#About

Python script to generate a graticule that will project cleanly (with smooth arcs) at world scale. The graticule should have a dense distribution of internal nodes along it's line, especially along the ±180, ±90 WGS84 bounding box.

##History

Script was originally written as a demonstration for students in Intro to GIS programming with python. Output format is geojson, because it's easy to write as a text file in python. Use ogr2ogr to convert to a SHP file.

##License

By **Alex Mandel** Copyright 2012. 
Modifications by Nathaniel Vaughn KELSO.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.


#Usage

`python pygraticule.py -s 1 -o outfile.geojson`

There are two script arguments for controlling the density of nodes and the output file name: 

* **s** is the step interval is measured in decimal degrees: generally 69 miles at the equator, but varies at higher latitudes.
* **o** is the outfile. If none is provided, file is auto named in this format: "graticule_1dd.geojson" where the number is the step interval.

## Limitations

* The output is lines, not polygons feature classes.

* The output is a GeoJSON format file, not a SHP format Esri Shapefile. (You can easily convert it with OGR, QGIS, etc...)

* Graticule is created in local coordinates (purely numeric).

## Examples

When we project out of WGS84 to another coordinate system that is not cylindrical, we need to have enough intermediate nodes
on the paths so the GIS application shows a "curve". Most GIS do not auto-densify straight lines during the projection
so we need to add these extra nodes in the raw geodata.

Here we see Robinson Projection using enough nodes:

![Zoom previews](https://github.com/wildintellect/pygraticule/raw/master/images/robinson.png)

Box results when nodes are sparse:

![Zoom previews](https://github.com/wildintellect/pygraticule/raw/master/images/box_no_densification.png)

The two superimposed:

![Zoom previews](https://github.com/wildintellect/pygraticule/raw/master/images/robinson_plus_box.png)

Comparison to QGIS graticule creator which only makes nodes where lines intersect:
![Zoom previews](https://github.com/wildintellect/pygraticule/raw/master/images/robinson_30d_compare.png)
