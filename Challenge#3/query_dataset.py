from datetime import *
import re

class Query_dataset:

    def __init__(self, dataset):
        self.dataset = dataset

    def get_avg_last(self,days = '', outcode_1 = '', outcode_2 = '', incode = '', age = '', property_type = '', duration = ''):
        self.prices = []
        current_time = datetime.strptime('2016-04-15 00:00','%Y-%m-%d %H:%M')
        for i in self.dataset:
            if days == '':
                var1 = True
            else:
                time_length = timedelta(int(days))
                var1 = (current_time - self.dataset[i].time) <= time_length
            if outcode_1 == '':
                var2 = True
            else:
                var2 = outcode_1 == self.dataset[i].outcode_1
            if outcode_2 == '':
                var3 = True
            else:
                var3 = outcode_2 == self.dataset[i].outcode_2
            if age == '':
                var4 = True
            else:
                var4 = age == self.dataset[i].age
            if property_type == '':
                var5 = True
            else:
                var5 = property_type == self.dataset[i].property_type
            if duration == '':
                var6 = True
            else:
                var6 = duration == self.dataset[i].duration
            if incode == '':
                var7 = True
            else:
                var7 = incode == self.dataset[i].incode
            if var1 and var2 and var3 and var4 and var5 and var6 and var7:
                self.prices.append(int(self.dataset[i].price))        
        return sum(self.prices)/len(self.prices)
    
    def get_avg_year(self,year = '', outcode_1 = '', outcode_2 = '', incode = '', age = '', property_type = '', duration = ''):
        self.prices = []
        for i in self.dataset:
            if year == '':
                var1 = True
            else:
                var1 = year == str(self.dataset[i].time.year)
            if outcode_1 == '':
                var2 = True
            else:
                var2 = outcode_1 == self.dataset[i].outcode_1
            if outcode_2 == '':
                var3 = True
            else:
                var3 = outcode_2 == self.dataset[i].outcode_2
            if age == '':
                var4 = True
            else:
                var4 = age == self.dataset[i].age
            if property_type == '':
                var5 = True
            else:
                var5 = property_type == self.dataset[i].property_type
            if duration == '':
                var6 = True
            else:
                var6 = duration == self.dataset[i].duration
            if incode == '':
                var7 = True
            else:
                var7 = incode == self.dataset[i].incode
            if var1 and var2 and var3 and var4 and var5 and var6 and var7:
                self.prices.append(int(self.dataset[i].price))        
        if self.prices == []:
            return "No Data"
        else:
            return sum(self.prices)/len(self.prices), len(self.prices)
                
                
