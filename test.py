import rhk_stmpy.rhk_sm4 as rhk
import xarray as xr
import matplotlib.pyplot as plt

f = rhk.load_sm4("test_files/2020-06-03_010_V_map1_0001_alyson.sm4")
f.info()


# pg = f[2]
# print("page count: ", f.page_count)
# print("page attributes: ", pg.attrs)
# print("data shape: ", pg.data.shape)
# print("data:")
# print(pg.data)
# plt.scatter(pg.data[0], pg.data[1])
# plt.show()






