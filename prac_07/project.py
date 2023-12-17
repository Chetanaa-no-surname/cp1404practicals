"""
CP1404/CP5632 Practical
Estimated: 1hr
Actual:
"""
import datetime

class Project:

    def __init__(self, name, date, priority, cost, completion):
        """Initialise"""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def update_data(self, new_completion,new_priority):
        """Updating data"""
        self.completion = new_completion
        self.priority = new_priority

    def __lt__(self, other):
        """Comparison for priority"""
        return self.priority < other.priority

    def __str__(self):
        """Printing"""
        return "{0}, start: {1}, priority {2}, estimate: ${3}, completion: {4}%".format(self.name,self.date.strftime("%d/%m/%Y"),self.priority,self.cost,self.completion)



