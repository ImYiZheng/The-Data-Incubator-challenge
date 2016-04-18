from datetime import datetime
import csv
import numpy
import math
i = 0
dataset = {}
filenames = ['Calls_for_Service_2011.csv','Calls_for_Service_2012.csv','Calls_for_Service_2013.csv','Calls_for_Service_2014.csv','Calls_for_Service_2015.csv']
for filename in filenames:
    csvfile = file(filename, 'rb')
    reader = csv.reader(csvfile)    
    for line in reader:
        ident = line[0]
        type_text = line[2]
        priority = line[3]
        time_created = line[6]
        try:
            time_created = datetime.strptime(time_created,'%m/%d/%Y %I:%M:%S %p')
        except:
            time_created = None        
        time_dispatch = line[7]
        try:
            time_dispatch = datetime.strptime(time_dispatch,'%m/%d/%Y %I:%M:%S %p')
        except:
            time_dispatch = None    
        time_arrive = line[8]
        try:
            time_arrive = datetime.strptime(time_arrive,'%m/%d/%Y %I:%M:%S %p')
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
        dataset[ident] = {'type_text':type_text, 'priority':priority,
                          'time_created':time_created, 'time_dispatch':time_dispatch,
                          'time_arrive':time_arrive, 'disposition':disposition,
                          'district':district, 'location_x':location_x,
                          'location_y':location_y}
    csvfile.close() 
print "Data loaded"

# Q1 - fraction of calls are of the most common type
call_type = {}
for key in dataset.keys():
    if dataset[key]['type_text'] not in call_type.keys():
        call_type[dataset[key]['type_text']] = 1
    else:
        call_type[dataset[key]['type_text']] = call_type[dataset[key]['type_text']] + 1
call_type_num = []
for key in call_type.keys():
    call_type_num.append(call_type[key])
print '*'*15
print 'Q1'
print max(call_type_num)
print sum(call_type_num)
print max(call_type_num)/float(sum(call_type_num))

# Q2 - get median response time
print '*'*15
print 'Q2'
response_time = []
for key in dataset.keys():
    if dataset[key]['time_arrive'] != None and dataset[key]['time_dispatch'] != None:
        val = (dataset[key]['time_arrive'] - dataset[key]['time_dispatch']).seconds
        response_time.append(val)
sorted_response_time = sorted(response_time)
if len(sorted_response_time) % 2 == 0:
    pos = (len(sorted_response_time))/2
    print (sorted_response_time[pos-1] + sorted_response_time[pos])/float(2)
else:
    pos = (len(sorted_response_time) + 1)/2
    print sorted_response_time[pos-1]

# Q3 - get difference of mean response of different districts
districts = ['0','1','2','3','4','5','6','7','8']
district_mean_response = []
for district in districts:
    response_time = []
    for key in dataset.keys():
        if dataset[key]['district'] == district and dataset[key]['time_arrive'] != None and dataset[key]['time_dispatch'] != None:
            val = (dataset[key]['time_arrive'] - dataset[key]['time_dispatch']).seconds
            response_time.append(val)
    district_mean_response.append(sum(response_time)/float(len(response_time)))
sorted_district_mean_response = sorted(district_mean_response)
print '*'*15
print 'Q3'
print sorted_district_mean_response
print sorted_district_mean_response[8] - sorted_district_mean_response[0]

# Q4 - surprising event
type_table = []
call_type = {}
for key in dataset.keys():
    if dataset[key]['district'] != '0':
        if dataset[key]['type_text'] not in call_type.keys():
            call_type[dataset[key]['type_text']] = 1
        else:
            call_type[dataset[key]['type_text']] = call_type[dataset[key]['type_text']] + 1
for key in call_type.keys():
    if call_type[key] < 100:
        type_table.append(key)
        del call_type[key]

call_type_num = []
for key in call_type.keys():
    call_type_num.append(call_type[key])
sum_events = sum(call_type_num)
call_type_pro = {}
for key in call_type.keys():
    call_type_pro[key] = call_type[key]/float(sum_events)

totol_district = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for key in dataset.keys():
    if dataset[key]['type_text'] not in type_table and dataset[key]['district'] != '0':
        totol_district[dataset[key]['district']] = totol_district[dataset[key]['district']] + 1

call_type_district = {}
for key in dataset.keys():
    if dataset[key]['district'] != '0':
        if dataset[key]['type_text'] not in call_type_district.keys():
            call_type_district[dataset[key]['type_text']] = {}
            if dataset[key]['district'] not in call_type_district[dataset[key]['type_text']].keys():
                call_type_district[dataset[key]['type_text']][dataset[key]['district']] = 1
            else:
                call_type_district[dataset[key]['type_text']][dataset[key]['district']] = call_type_district[dataset[key]['type_text']][dataset[key]['district']] + 1
        else:
            if dataset[key]['district'] not in call_type_district[dataset[key]['type_text']].keys():
                call_type_district[dataset[key]['type_text']][dataset[key]['district']] = 1
            else:
                call_type_district[dataset[key]['type_text']][dataset[key]['district']] = call_type_district[dataset[key]['type_text']][dataset[key]['district']] + 1
for key in call_type_district.keys():
    if key in type_table:
        del call_type_district[key]
call_type_district_pro = {}
for type_event in call_type_district.keys():
    type_num = []
    for district in call_type_district[type_event].keys():
        type_num.append(call_type_district[type_event][district]/float(totol_district[district]))
    call_type_district_pro[type_event] = max(type_num)
    
ratio_type = {}
for key in call_type_pro.keys():
    ratio_type[key] = call_type_district_pro[key]/call_type_pro[key]
ratio = []
for key in ratio_type.keys():
    ratio.append(ratio_type[key])
print '*'*15
print 'Q4'
print max(ratio)

# Q6 - get disposition_vary
disposition_2011 = {}
disposition_2012 = {}
disposition_2013 = {}
disposition_2014 = {}
disposition_2015 = {}
for key in dataset.keys():
    if dataset[key]['time_created'].year == 2011:        
        if dataset[key]['time_created'].day not in disposition_2011.keys():
             disposition_2011[dataset[key]['time_created'].day] = {}
             if dataset[key]['time_created'].hour not in disposition_2011[dataset[key]['time_created'].day].keys():
                 disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                 disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
             else:
                 disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
        else:
            if dataset[key]['time_created'].hour not in disposition_2011[dataset[key]['time_created'].day].keys():
                disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
            else:
                disposition_2011[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
                
    if dataset[key]['time_created'].year == 2012:
        if dataset[key]['time_created'].day not in disposition_2012.keys():
             disposition_2012[dataset[key]['time_created'].day] = {}
             if dataset[key]['time_created'].hour not in disposition_2012[dataset[key]['time_created'].day].keys():
                 disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                 disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
             else:
                 disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
        else:
            if dataset[key]['time_created'].hour not in disposition_2012[dataset[key]['time_created'].day].keys():
                disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
            else:
                disposition_2012[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
                
    if dataset[key]['time_created'].year == 2013:
        if dataset[key]['time_created'].day not in disposition_2013.keys():
             disposition_2013[dataset[key]['time_created'].day] = {}
             if dataset[key]['time_created'].hour not in disposition_2013[dataset[key]['time_created'].day].keys():
                 disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                 disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
             else:
                 disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
        else:
            if dataset[key]['time_created'].hour not in disposition_2013[dataset[key]['time_created'].day].keys():
                disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
            else:
                disposition_2013[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
                
    if dataset[key]['time_created'].year == 2014:
        if dataset[key]['time_created'].day not in disposition_2014.keys():
             disposition_2014[dataset[key]['time_created'].day] = {}
             if dataset[key]['time_created'].hour not in disposition_2014[dataset[key]['time_created'].day].keys():
                 disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                 disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
             else:
                 disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
        else:
            if dataset[key]['time_created'].hour not in disposition_2014[dataset[key]['time_created'].day].keys():
                disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
            else:
                disposition_2014[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])

    if dataset[key]['time_created'].year == 2015:
        if dataset[key]['time_created'].day not in disposition_2015.keys():
             disposition_2015[dataset[key]['time_created'].day] = {}
             if dataset[key]['time_created'].hour not in disposition_2015[dataset[key]['time_created'].day].keys():
                 disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                 disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
             else:
                 disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
        else:
            if dataset[key]['time_created'].hour not in disposition_2015[dataset[key]['time_created'].day].keys():
                disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour] = []
                disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])
            else:
                disposition_2015[dataset[key]['time_created'].day][dataset[key]['time_created'].hour].append(dataset[key]['disposition'])

variation = []
for day in disposition_2011.keys():
    day_total_position = []
    num_hour = []
    for hour in disposition_2011[day]:
        disposition_2011[day][hour] = list(set(disposition_2011[day][hour]))
        day_total_position = day_total_position + disposition_2011[day][hour]
        num_hour.append(len(disposition_2011[day][hour]))
    day_total_position = list(set(day_total_position))
    variation.append((max(num_hour) - min(num_hour))/float(len(day_total_position)))
print '*'*15
print 'Q6'
print max(variation)

variation = []
for day in disposition_2012.keys():
    day_total_position = []
    num_hour = []
    for hour in disposition_2012[day]:
        disposition_2012[day][hour] = list(set(disposition_2012[day][hour]))
        day_total_position = day_total_position + disposition_2012[day][hour]
        num_hour.append(len(disposition_2012[day][hour]))
    day_total_position = list(set(day_total_position))
    variation.append((max(num_hour) - min(num_hour))/float(len(day_total_position)))
print max(variation)

variation = []
for day in disposition_2013.keys():
    day_total_position = []
    num_hour = []
    for hour in disposition_2013[day]:
        disposition_2013[day][hour] = list(set(disposition_2013[day][hour]))
        day_total_position = day_total_position + disposition_2013[day][hour]
        num_hour.append(len(disposition_2013[day][hour]))
    day_total_position = list(set(day_total_position))
    variation.append((max(num_hour) - min(num_hour))/float(len(day_total_position)))
print max(variation)

variation = []
for day in disposition_2014.keys():
    day_total_position = []
    num_hour = []
    for hour in disposition_2014[day]:
        disposition_2014[day][hour] = list(set(disposition_2014[day][hour]))
        day_total_position = day_total_position + disposition_2014[day][hour]
        num_hour.append(len(disposition_2014[day][hour]))
    day_total_position = list(set(day_total_position))
    variation.append((max(num_hour) - min(num_hour))/float(len(day_total_position)))
print max(variation)

variation = []
for day in disposition_2015.keys():
    day_total_position = []
    num_hour = []
    for hour in disposition_2015[day]:
        disposition_2015[day][hour] = list(set(disposition_2015[day][hour]))
        day_total_position = day_total_position + disposition_2015[day][hour]
        num_hour.append(len(disposition_2015[day][hour]))
    day_total_position = list(set(day_total_position))
    variation.append((max(num_hour) - min(num_hour))/float(len(day_total_position)))
print max(variation)

# Q7 - calculate the areas
district_area = {}
for key in dataset.keys():
    if dataset[key]['location_x'] != None and dataset[key]['location_y'] != None:
        if dataset[key]['district'] not in district_area.keys():
            district_area[dataset[key]['district']] = [[],[]]
            district_area[dataset[key]['district']][0].append(dataset[key]['location_x'])
            district_area[dataset[key]['district']][1].append(dataset[key]['location_y'])           
        else:
            district_area[dataset[key]['district']][0].append(dataset[key]['location_x'])
            district_area[dataset[key]['district']][1].append(dataset[key]['location_y'])   
areas = []
for key in district_area.keys():
    std_x = numpy.std(district_area[key][0])
    std_y = numpy.std(district_area[key][1])
    area = std_x*std_y*math.pi
    areas.append(area)

print '*'*15
print 'Q7'
print areas
print max(areas)

# Q8 - priority 
call_type_priority = {}
for key in dataset.keys():
    if dataset[key]['type_text'] not in call_type_priority.keys():
        call_type_priority[dataset[key]['type_text']] = {}
        if dataset[key]['priority'] not in call_type_priority[dataset[key]['type_text']].keys():
            call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] = 1
        else:
            call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] = call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] + 1
    else:
        if dataset[key]['priority'] not in call_type_priority[dataset[key]['type_text']].keys():
            call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] = 1
        else:
            call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] = call_type_priority[dataset[key]['type_text']][dataset[key]['priority']] + 1
call_type_priority_pro = []
for type_event in call_type_priority.keys():
    type_num = []
    for priority in call_type_priority[type_event].keys():
        type_num.append(call_type_priority[type_event][priority])
    call_type_priority_pro.append(max(type_num)/float(sum(type_num)))
print '*'*15
print 'Q8'
print min(call_type_priority_pro) 
