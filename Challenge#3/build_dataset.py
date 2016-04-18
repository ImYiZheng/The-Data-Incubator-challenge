from datetime import datetime
import re

class Build_dataset:

    class val:
        def __init__(self, price, time, outcode_1, outcode_2, incode, age, property_type, duration):
            self.price = price  
            self.time = time  
            self.outcode_1 = outcode_1
            self.outcode_2 = outcode_2
            self.incode = incode
            self.age = age
            self.property_type = property_type
            self.duration = duration

    def __init__(self):
        self.dataset = {} 
    
    def get_record(self, line):
        record =list(line.strip().split(','))
        return record

    def add_record(self, record):
        ident = record[0].strip('"')
        price = record[1].strip('"')
        time = datetime.strptime(record[2],'%Y-%m-%d %H:%M')
        postcode = list(record[3].strip().split(' '))
        try:
            outcode_2 = (re.findall("\d+\.?\d*",postcode[0]))[0]
            outcode_1 = postcode[0].strip(outcode_2)
            outcode_1 = outcode_1.strip('"')
            incode = (re.findall("\d+\.?\d*",postcode[1]))[0]
        except:
            outcode_1 = ''
            outcode_2 = ''
            incode = ''
        age = record[5].strip('"')
        property_type = record[4].strip('"')
        duration = record[6].strip('"')
        record_val = self.val(price, time, outcode_1, outcode_2, incode, age, property_type, duration)

        if ident == 'D':
            del self.dataset[ident]
        if ident == 'A' or 'C':
            self.dataset[ident] = record_val
        
