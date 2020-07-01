import rhk_stmpy.rhk_sm4 as rhk  # Importing the rhk_sm4 module

# initializing
f = rhk.load_sm4("test_files/2020-06-03_010_V_map1_0001_alyson.sm4")  # Loading .sm4 file
pg = f[6]  # assigning 7th page of .sm4 file

# metadata
attrs = pg.attrs  # page/data attributes as a dictionary
pg_count = f.page_count  # number of pages as int
f.print_info()  # print overview of sm4 file pages as pandas dataframe

# data
coords = pg.coords
ramp = coords[1][1]  # x-axis ramping values as numpy array
data = pg.data  # data as numpy array

print(attrs)
print(ramp)
print(data)






