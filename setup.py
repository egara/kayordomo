import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kayordomo",
    version="1.0",
    author="Eloy García Almadén",
    author_email="eloy.garcia.pca@gmail.com",
    description="This is a very small web service to interact with Kodi locally. When it is up and running you can "
                "tell kodi's addons to do elaborated things via JSONRPC Kodi's protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/egara/kayordomo",
    packages=setuptools.find_packages(),
    install_requires=[
        'unidecode>=1.1.1',
        'requests>=2.22.0',
        'PyYAML>=4.2b1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Utilities"
    ],
)
