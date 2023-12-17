"""
CP1404/CP5632 Practical
Estimated: 1hr
Actual:
"""


class Project:

    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def update_completion(self, new_completion):
        self.completion = new_completion

    def update_priority(self,new_priority):
        self.priority = new_priority



