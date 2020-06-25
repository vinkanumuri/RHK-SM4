# Importing the rhk_sm4 module and other packages.
import rhk_stmpy.rhk_sm4 as rhk
import matplotlib.pyplot as plt

f = rhk.load_sm4("test_files/2020-06-03_010_V_map1_0001_alyson.sm4")  # Loading .sm4 file .

# printing summary of sm4 file pages or number of pages
summary = f.info()
# print(summary)
# print(f.page_count)

# accessing page data as numpy array and page attributes as a dictionary
pg = f[4]
attrs = pg.attrs
#print(attrs)  # printing attributes
data = pg.data

# plotting data
plt.scatter(data[0], data[1])
plt.xlabel(attrs['Xlabel'])
plt.ylabel(attrs['Ylabel'])
plt.show()






