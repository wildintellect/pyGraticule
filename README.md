#About

Python script to generate a graticule that will project cleanly (with smooth arcs) at world scale.

Output format is geojson, because it's easy to write as a text file python. Use ogr2ogr to convert to a SHP file.

By **Alex Mandel** 2012.

#Usage

`python geojson-graticule.py`

* **step** interval is measured in decimal degrees: generally 69 miles at the equator, but varies at higher latitudes.
* **outfile** is somewhat hard coded as "graticule_1dd.geojson" where the number is the step interval.

## Limitations

Both **step** interval and the **outfile** name should be parameters. 