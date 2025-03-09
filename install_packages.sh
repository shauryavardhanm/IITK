#!/bin/bash

# Update pip to the latest version
pip install --upgrade pip

# List of packages to install
packages=(
    gdal
    geographiclib
    lxml
    matplotlib
    netCDF4
    numpy
    openpyxl
    pandas
    pysftp
    requests
    tqdm
    paramiko
    xarray
)

# Install each package
for package in "${packages[@]}"
do
    pip install "$package"
done
