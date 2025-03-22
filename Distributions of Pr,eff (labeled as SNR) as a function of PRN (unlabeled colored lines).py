import xarray as xr
import matplotlib.pyplot as plt
import dask  
import time
data_path = r'C:\Users\91705\Downloads\ncg iitk\DATASET\*.nc'


try:
  # Prefer explicit chunking control (optional)
  dataset = xr.open_mfdataset(data_path, chunks=None)  # No chunking by default


except ValueError as e:
  print(f"Error opening netCDF files: {e}")
  dataset = None  # Set dataset to None to indicate error

# Check if dataset was opened successfully
if dataset is not None:
  # Extract data and plot (adapt based on your previous code)
  data = dataset['SM_daily'][:]
  
plt.plot(data[0, :])   
plt.xlabel('Time')
plt.ylabel('SNR')
plt.title('Distributions of Pr,eff (labeled as SNR) as a function of PRN (unlabeled colored lines)')
plt.show()

# Close the dataset (if opened)
if dataset is not None:
  dataset.close()
