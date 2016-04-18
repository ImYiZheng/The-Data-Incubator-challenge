from datetime import datetime
import csv

dataset2011 = {}
csvfile = file('Calls_for_Service_2011.csv', 'rb')
reader = csv.reader(csvfile)    
for line in reader:
    ident = line[0]
    type_text = line[2]
    priority = line[3]
    time_created = line[6]
    try:
        time_created = datetime.strptime(time_created,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_created = None        
    time_dispatch = line[7]
    try:
        time_dispatch = datetime.strptime(time_dispatch,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_dispatch = None    
    time_arrive = line[8]
    try:
        time_arrive = datetime.strptime(time_arrive,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_arrive = None     
    disposition = line[10]
    district = line[14]
    location = line[15]
    if location == '':
        location_x = None
        location_y = None
    else:
        location = list(line[15].strip().split(','))
        location_x = location[0]
        location_x = float(location_x.strip('('))
        location_y = location[1]
        location_y = float(location_y.strip(')'))
    dataset2011[ident] = {'type_text':type_text, 'priority':priority,
                      'time_created':time_created, 'time_dispatch':time_dispatch,
                      'time_arrive':time_arrive, 'disposition':disposition,
                      'district':district, 'location_x':location_x,
                      'location_y':location_y}
csvfile.close() 
print "Data 2011 loaded"

dataset2015 = {}
csvfile = file('Calls_for_Service_2015.csv', 'rb')
reader = csv.reader(csvfile)    
for line in reader:
    ident = line[0]
    type_text = line[2]
    priority = line[3]
    time_created = line[6]
    try:
        time_created = datetime.strptime(time_created,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_created = None        
    time_dispatch = line[7]
    try:
        time_dispatch = datetime.strptime(time_dispatch,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_dispatch = None    
    time_arrive = line[8]
    try:
        time_arrive = datetime.strptime(time_arrive,'%m/%d/%Y %H:%M:%S %p')
    except:
        time_arrive = None     
    disposition = line[10]
    district = line[14]
    location = line[15]
    if location == '':
        location_x = None
        location_y = None
    else:
        location = list(line[15].strip().split(','))
        location_x = location[0]
        location_x = float(location_x.strip('('))
        location_y = location[1]
        location_y = float(location_y.strip(')'))
    dataset2015[ident] = {'type_text':type_text, 'priority':priority,
                      'time_created':time_created, 'time_dispatch':time_dispatch,
                      'time_arrive':time_arrive, 'disposition':disposition,
                      'district':district, 'location_x':location_x,
                      'location_y':location_y}
csvfile.close() 
print "Data 2015 loaded"

# fraction of calls are of the most common type
call_type_2011 = {}
for key in dataset2011.keys():
    if dataset2011[key]['type_text'] not in call_type_2011.keys():
        call_type_2011[dataset2011[key]['type_text']] = 1
    else:
        call_type_2011[dataset2011[key]['type_text']] = call_type_2011[dataset2011[key]['type_text']] + 1

call_type_2015 = {}
for key in dataset2015.keys():
    if dataset2015[key]['type_text'] not in call_type_2015.keys():
        call_type_2015[dataset2015[key]['type_text']] = 1
    else:
        call_type_2015[dataset2015[key]['type_text']] = call_type_2015[dataset2015[key]['type_text']] + 1

percent_decrease = []
for key in call_type_2011.keys():
    if key in call_type_2015.keys():
        val = call_type_2011[key] - call_type_2015[key]
        num = call_type_2011[key]
        percent_decrease.append(val/float(num))
print max(percent_decrease)

