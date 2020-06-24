import rhk_stmpy.rhk_sm4 as rhk
import xarray as xr
import matplotlib as plt

f = rhk.load_sm4("test_files/2020-06-03_010_V_map1_0001_alyson.sm4")
print(f[0].attrs)
print(f[1].attrs)
print(f[2].attrs)
print(f[3].attrs)







