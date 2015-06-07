# By Alex Mandel Copyright 2012
# Modifications by Nathaniel Vaughn KELSO
#
# Script to generate a graticule that will reproject cleanly(smooth arcs) at world scale
# Output format is geojson, because it's easy to write as a text file python.
# Use ogr2ogr to convert to a SHP format "Esri Shapefile"
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# The following double # section makes this script compatible with QGIS Processing Toolbox
##minX=number -180
##maxX=number 180
##minY=number -90
##maxY=number 90
##step=number 10
##density=number 1
##outfile=output file


#import sys, math, stat
import os
from optparse import OptionParser

def make_graticule(outfile,minX=-180, minY=-90, maxX=180, maxY=90, step=10,density=1):
    if outfile:
        # remember the directory that file is contained by
        outdir = os.path.dirname( os.path.abspath(outfile) )
        outname = os.path.basename( os.path.abspath(outfile) )
    else:
        outdir = 'output/'
        # destination file
        outextension = 'geojson'
        # for the demo, we put the results in an "output dir for prettier results    
        outname = ('graticule_%ddd') % (step)
        outfile = outdir + outname + '.' + outextension
    
    # If the output directory doesn't exist, make it so we don't error later on file open()
    if not os.path.exists(outdir):
        print 'making dir...'
        os.makedirs(outdir)
    
    grid = open(outfile,"w")
    
    # Stub out the GeoJSON format wrapper
    header = ['{ "type": "FeatureCollection",','"features": [']
    footer = [']','}']
    
    grid.writelines(header)
        
    # Create Geojson lines horizontal, latitude
    for y in range(minY,maxY+1,step):
        featstart = '''{ "type": "Feature",
          "geometry": {
            "type": "LineString",
            "coordinates": ['''
        grid.write(featstart)
        for x in range(minX,maxX+1,density):
            if x == minX:
                grid.write("[")
            else:
                grid.write(",[")
            #print y,x
            grid.write(",".join([str(x),str(y)]))
            grid.write("]")
        # Figure out if it's North or South
        if y >= 0:
            direction = "N"
        else:
            direction = "S"
        label = " ".join([str(abs(y)),direction])
        featend = ''']},
          "properties": {
            "degrees": %d,
            "direction": "%s",
          "display":"%s",
          "dd":%d,
            }
          },\n''' % (abs(y),direction,label,y)
        grid.write(featend)
    
    # Create lines vertical
    for x in range(minX,maxX+1,step):
        featstart = '''{ "type": "Feature",
          "geometry": {
            "type": "LineString",
            "coordinates": ['''
        grid.write(featstart)
        for y in range(minY,maxY+1,density):
            if y == minY:
                grid.write("[")
            else:
                grid.write(",[")
            #print y,x
            grid.write(",".join([str(x),str(y)]))
            grid.write("]")
            
        # Figure out if it's East or West
        if x >= 0:
            direction = "E"
        else:
            direction = "W"
        label = " ".join([str(abs(x)),direction])
        featend = ''']},
          "properties": {
            "degrees": %d,
            "direction": "%s",
          "display":"%s",
          "dd":%d,
            }
          },\n''' % (abs(x),direction,label,x)
        grid.write(featend)
    
    grid.writelines(footer)
    grid.close()

#if shapefile:
#    try:
#        ogr2ogr -f "ESRI Shapefile" out_file  out_file
#    except:
#        pass

if __name__ == '__main__':
    #TODO: Take bounding box as arg for setting range
 
    parser = OptionParser(usage="""%prog [options]
    
    Generates a GeoJSON file with graticules spaced at specified interval.""")
    
    parser.add_option('-s', '--step_interval', dest='step_interval', default=1, type='int',
                      help='Step interval in decimal degrees, defaults to 1.')
    
    parser.add_option('-o', dest='outfilename', default='',
                      help='Output filename (with or without path), defaults to "graticule_1dd.geojson".')
    
    #TODO: Implement python OGR writing for multiple output format support.
    #parser.add_option('-p', '--shp', dest='shapefile', default=False, type='boolean",
    #                  help='Output a SHP file, defaults to False and requires ORG/GDAL.')
    
    
    (options, args) = parser.parse_args()
    
    
    #set the stepping of the increment, converting from string to interger
    #TODO: Calculate a node density based on the bounding box and interval defined by the user
    step = options.step_interval
    # destination file
    outfile = options.outfilename
    density = 1
    #make_graticule(outfile, -180, -90, 180, 90, step, density)


if __name__ != '__main__':
    make_graticule(outfile, minX, minY, maxX, maxY, step, density)