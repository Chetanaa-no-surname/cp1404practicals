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

    def update_data(self, new_completion,new_priority):
        self.completion = new_completion
        self.priority = new_priority




