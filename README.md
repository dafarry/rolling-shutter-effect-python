# Rolling Shutter Effect Video generated with Python

I watched the Youtube video 
[Rolling Shutter Explained on the Cheap](https://www.youtube.com/watch?v=nP1elMR5qjc)
by Matt Parker where he shows that you don't need to visit an actual
aeroplane with expensive slow-motion cameras to demonstrate the rolling shutter
effect on aircraft propellors. He shows that you can do it with a model
propellor connected to an electric drill — then some Python code to
process the video to emulate the rolling shutter effect and to add
a green line scanning down the image.

Well, I thought, instead of that, let's do the **whole thing** in Python.

This file is 30 lines of Python, using the Numpy and Pillow libraries and
ffmpeg to create the video:

[rolling-shutter-makevideo.py](rolling-shutter-makevideo.py)

This file is another version that uses Tkinter to display the video to your
screen in real time rather than making a video. It needs a fast(ish) PC to
display smoothly:

[rolling-shutter-tkinter.py](rolling-shutter-tkinter.py)

Installation instructions for the Python libraries are below.

![Rolling Shutter Effect](rolling-shutter-effect-apng.png)

Installation instructions for Python libraries
----------------------------------------------

Windows
-------
Download & install the latest Python from python.org  
Then at the Windows Command Prompt, install the libraries like so:

    python -m pip install --upgrage pip
    python -m pip install --upgrade wheel setuptools
    python -m pip install numpy
    python -m pip install pillow

Download FFMpeg from ffmpeg.org  
Version 4.2.1 of FFMpeg was used at the time of writing.  
Only needed for making the mpeg video with the "makevideo" python script.  
Unzip the file, and put ffmpeg.exe somewhere on your PATH, e.g.: 
in C:\WINDOWS

Ubuntu and Debian
-----------------
Works fine with system Python3, version 3.7.3, at the time of writing  
Install the following packages with `sudo apt install`

    python3-numpy python3-tk python3-pil python3-pil.imagetk ffmpeg

(Unlike PIL in PyPI, the "imagetk" is split off into a separate
package, which is a bit of a "gotcha".)



