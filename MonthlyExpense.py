import numpy as np

import matplotlib.pyplot as p1
p1.title('Bar Chart')
p1.xlabel('Years')
p1.ylabel(' in Rupees')
y=([40.49,47.51,42.85,45.56,40.62,47.93,63.37,73.18,63.09,71.51,66.29,63.02,65.32,78.43,74.51,75.14])
x=([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
x1 = np.arange(len(x))
p1.bar(x1,y,color='r')
p1.xticks(x1,x,color='Black',rotation=90)
p1.show()