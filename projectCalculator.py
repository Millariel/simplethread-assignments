import datetime

class Project:
    
    #start_date
    #end_date
    #totalcost

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.totalcost = 0

    def __repr__(self):
        return "start date: " + str(self.start_date) + "\nend date: " + str(self.end_date) + "\ntotal cost: " + str(self.totalcost)
        
        

project1 = Project(datetime.datetime(2015, 9, 1), datetime.datetime(2015, 9, 3))



print(project1)

