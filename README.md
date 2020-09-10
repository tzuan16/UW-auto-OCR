*UW-auto-OCR USER INSTRUCTIONS*

1. This program requires Firefox to be downloaded on your computer for now, but it should be able to work with different web browsers with some simple code changes.
2. Download the correct version of the Firefox Driver for your computer from https://github.com/mozilla/geckodriver/releases
Note: If you ended up using a different web browser that is not Firefox, please download the corresponding Driver from: https://github.com/SeleniumHQ/selenium/blob/trunk/py/docs/source/index.rst
3. upzip or untar the downloaded driver and move it to where your PATH is pointed to.
To do this, first try ``echo $PATH`` to see where your PATH is pointed to (not sure how this works but there might be multiple, but I ended up using ``/user/bin/``).  Then, you move the file move the file into the directory PATH is pointed to.
4. Clone this project to your local box and you will see a file named setUp.sh. To give this file an executable, we run ``chmod +rwx setUp.sh`` in the directory that setUp.sh is in.
5. (This part is not tested yet, might need to download more packages) In the same directory as above,  run ``./setUp.sh`` to download the packages.
6. run ``python CourseFull.py``
