# Alex Mandel Copyright 2012
# Script to generate a graticule that will reproject cleanly(smooth arcs) at world scale
# Output format is geojson, because it's easy to write as a text file python.
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

#set the stepping of the increment
step = 30
outfile = "graticule_%ddd.geojson" % (step)

grid = open(outfile,"w")
header = ['{ "type": "FeatureCollection",','"features": [']
footer = [']','}']
grid.writelines(header)

    
#Create Geojson lines horizontal, latitude
for x in range(-90,91,step):
    featstart = '''{ "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": ['''
    grid.write(featstart)
    for y in range(-180,181,1):
        if y == -180:
            grid.write("[")
        else:
            grid.write(",[")
        #print y,x
        grid.write(",".join([str(y),str(x)]))
        grid.write("]")
    #Figure out if it's North or South
    if x >= 0:
        direction = "N"
    else:
        direction = "S"
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

#Create lines vertical
for y in range(-180,181,step):
    featstart = '''{ "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": ['''
    grid.write(featstart)
    for x in range(-90,91,1):
        if x == -90:
            grid.write("[")
        else:
            grid.write(",[")
        #print y,x
        grid.write(",".join([str(y),str(x)]))
        grid.write("]")
        
    #Figure out if it's East or West
    if x >= 0:
        direction = "W"
    else:
        direction = "E"
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

grid.writelines(footer)
grid.close()