# PlotSeismicity
Plot 3D views of the seismicity


## Step 1: select your region of interest (as well as the magnitude requirements).
Plot by obspy. Not sure why the coordinates went wrong.

 <img src="events.png" width="300" alt="Events Map for RF">

## Set the views

Two parameters can be set:
* azm
* dep
Those parameters control the angles for projection.

## Step 2: run 

```python viewer.py```

In the example, the dep is fixed, and a loop over azimuth (0-360, every 5⁰).
This produces 72 images.
Resolution for coastlines and final images can be adjusted.


<img src="test_3dscatter_30_-90.png" width="300" alt="Events Map for RF">

Step 3: assemble all the 2D images into a gif (to be implemented)

<img src="ezgif-7-fca2f1542377.gif" width="300" alt="Events Map for RF">


@earthinversion , we count on you for some further implementations.
