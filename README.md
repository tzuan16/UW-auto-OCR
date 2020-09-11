## UW-auto-OCR USER INSTRUCTIONS

Premise: Python 3 is installed on your machine

### Firefox

1. Download the correct version of the Firefox Driver for your computer from https://github.com/mozilla/geckodriver/releases

2. upzip or untar the downloaded driver and move it to where your PATH is pointed to.
To do this, first try ``echo $PATH`` to see where your PATH is pointed to (e.g. ``/user/bin/`` or ``/user/local/bin/``).  Move it via Finder or by running ``mv geckodriver ~/Downloads /user/local/bin``

3. Clone this project to your local box and in the directory, run ``sh setUp.sh``

4. run ``python3 CourseFullFirefox.py``

### Chrome

1. Download the correct version of the Chrome Driver for your computer from https://chromedriver.chromium.org/downloads

2. upzip or untar the downloaded driver and move it to where your PATH is pointed to.
To do this, first try ``echo $PATH`` to see where your PATH is pointed to (e.g. ``/user/bin/`` or ``/user/local/bin/``).  Move it via Finder or by running ``mv chromedriver ~/Downloads /user/local/bin``

3. For MacOS Catalina, you need to verify the developer by running ``xattr -d com.apple.quarantine chromedriver`` in the directory where chromedriver is stored

3. Clone this project to your local box and in the directory, run ``sh setUp.sh``

4. run ``python3 CourseFullChrome.py``

