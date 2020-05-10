from obspy import read_inventory, read_events, UTCDateTime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from obspy.clients.fdsn import Client
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap



#fig = plt.figure()
client = Client("IRIS")

t1 = UTCDateTime("1950-01-07T00:00:00")
t2 = UTCDateTime("2020-01-07T03:00:00")

### Taiwan
#minlat, maxlat = 20, 30
#minlon, maxlon = 110,130

minlat, maxlat = -90, 90
minlon, maxlon = -180,180

cat = client.get_events(starttime=t1, endtime=t2,minlatitude=minlat,maxlatitude=maxlat,minlongitude=minlon,maxlongitude=maxlon,minmagnitude=6.5,catalog="ISC")
cat.plot(outfile='events.png')

x = []
y = []
z = []
mag = []

for catalog in cat:
    x.append(catalog.origins[0].longitude)
    y.append(catalog.origins[0].latitude)
    mag.append(0.1 * int(catalog.magnitudes[0].mag) * int(catalog.magnitudes[0].mag) * int(catalog.magnitudes[0].mag))
#    print(catalog.magnitudes[0].mag)
    if (catalog.origins[0].depth == None):
        z.append(np.nan)
    else:
        z.append(- catalog.origins[0].depth/1000)

#    print(x,y,z)
#for dep in range(-45,0,15):
for dep in [30]:
    fig = plt.figure()


    ax = fig.add_subplot(111, projection='3d')
    map = Basemap(llcrnrlon=minlon, llcrnrlat=minlat,urcrnrlon=maxlon, urcrnrlat=maxlat, resolution='i',ax=ax)
    ax.add_collection3d(map.drawcoastlines(linewidth=0.2),zs = 10)
    ax.add_collection3d(map.drawcountries(linewidth=0.1),zs = 10)

    x1,y1 = map(x, y)
    ax.scatter3D(x1, y1, z, c=z, s=mag, alpha=0.5, edgecolors='k',linewidths=0.1)

    meridians = np.arange(minlon-1,maxlon+int(np.abs(maxlon - minlon))+1,45)
    parallels = np.arange(minlat-1,maxlat+int(np.abs(maxlat - minlat))+1,45)

    ax.grid(False)
    ax.set_yticks(parallels)
    ax.set_yticklabels(parallels,fontsize=6)
    ax.set_xticks(meridians)
    ax.set_xticklabels(meridians,fontsize=6)

    ax.set_zlim(-700, 11)

    #p = ax.scatter(lons, lats, msl_alt, c=tec_cal, cmap='jet')
    for azm in range(-360,1,5):
        ax.view_init(dep, azm)
        plt.savefig('test_3dscatter_{}_{}.png'.format(azm,dep),dpi=300,bbox_inches='tight')
        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude')
        ax.set_zlabel('Depth')
#        plt.title('Seismicity')
    plt.close('all')


