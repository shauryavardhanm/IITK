import pygnss
from osgeo import gdal

# Fetch CYGNSS data
files = ["path_to_your_cygnss_data_file"]
cyg = pygnss.orbit.read_cygnss_l2(files[0])

for sat in range(8):
    trl = pygnss.orbit.get_tracks(cyg, sat, verbose=True, eps=2.0)
    print('\\nAdding IMERG to', len(trl), 'tracks')
    trl = pygnss.orbit.add_imerg(trl, ifiles, dt_imerg)
    print('Saving Files')
    pygnss.orbit.write_netcdfs(trl, tr_path + sdate + '/')
cyg.close()

# Define your coordinates
upper_left_x = 699934.584491
upper_left_y = 6169364.0093
lower_right_x = 700160.946739
lower_right_y = 6168703.00544
window = (upper_left_x, upper_left_y, lower_right_x, lower_right_y)

# Crop the data according to the coordinates
gdal.Translate('output_crop_raster.tif', 'input_raster.tif', projWin=window)
