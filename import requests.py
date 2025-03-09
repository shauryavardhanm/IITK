import requests
import netCDF4 as nc
import numpy as np

def fetch_cygnss_data(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def read_netcdf_data(file_path):
    dataset = nc.Dataset(file_path, 'r')
    wind_speed = dataset.variables['wind_speed'][:]
    latitude = dataset.variables['latitude'][:]
    longitude = dataset.variables['longitude'][:]
    dataset.close()
    return wind_speed, latitude, longitude

def cut_area(wind_speed, latitude, longitude, lat_min, lat_max, lon_min, lon_max):
    lat_mask = (latitude >= lat_min) & (latitude <= lat_max)
    lon_mask = (longitude >= lon_min) & (longitude <= lon_max)
    area_mask = lat_mask & lon_mask
    
    wind_speed_cut = wind_speed[area_mask]
    lat_cut = latitude[area_mask]
    lon_cut = longitude[area_mask]
    
    return wind_speed_cut, lat_cut, lon_cut

def main():
    url = 'https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-protected/CYGNSS_L3_SOIL_MOISTURE_V1.0/2021/069/ucar_cu_cygnss_sm_v1_2021_069.nc'
    save_path = 'cygnss_data.nc'
    
    # Fetch
    fetch_cygnss_data(url, save_path)
    
    # Read
    wind_speed, latitude, longitude = read_netcdf_data(save_path)
    
    # Define the area of interest
    lat_min, lat_max = -10, 10  # Example latitude bounds
    lon_min, lon_max = 90, 100  # Example longitude bounds
    
    # Cut the data
    wind_speed_cut, lat_cut, lon_cut = cut_area(wind_speed, latitude, longitude, lat_min, lat_max, lon_min, lon_max)
    
    # Do something with the cut data
    print('Wind Speed Data:', wind_speed_cut)
    print('Latitude Data:', lat_cut)
    print('Longitude Data:', lon_cut)

if __name__ == '__main__':
    main()