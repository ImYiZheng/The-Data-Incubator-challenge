from build_dataset import *
from query_dataset import *
from datetime import *
import json

f = open('pp-2015.txt')
lines = f.readlines()
data = Build_dataset()


for line in lines:
    record = data.get_record(line)
    data.add_record(record)
f.close()



query = Query_dataset(data.dataset)
a,b = query.get_avg_year(year = '2015', outcode_1 = 'CB', age = 'N', property_type = 'F',duration = 'L')
print a,b


#year = '2016', outcode_1 = 'CB', outcode_2 = '6'
#age = 'Y' or 'N' , property_type = 'D', 'S', 'T', 'F', 'O'
#duration = 'F' or 'L' 


