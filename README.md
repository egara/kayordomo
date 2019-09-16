# kayordomo

## Summary ##
This is a very small web service to interact with Kodi locally. When it is up and running you can tell kodi's addons to do complex things via JSONRPC Kodi's protocol.

## Installation ##
You can install Kayordomo following these instructions:

1. Clone the repository (install **git** if it is needed first)

  ```
    git clone https://github.com/egara/kayordomo.git

  ```

2. Install all the dependencies needed (all the packages described below are for **Arch Linux**. Please, check for those packages and their names in you correspondant distribution):
    - Python 3 (python)
    - Setup Tools for Python 3 (python-setuptools)

3. Install the rest of the dependencies:

  ```
    cd kayordomo
    python setup.py install --user

  ```
  Please note that if you have several versions of python installed on your system, maybe you have to run explicity **python3 setup.py install --user** instead.

## Contact ##
If you want to contact me, you can do it using this e-mail address <eloy.garcia.pca@gmail.com>.
