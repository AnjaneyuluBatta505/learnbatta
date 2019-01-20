class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.day, self.month, self.year)

d = Date.from_string('01-12-2019')
print(d)
# Output: Date(1, 12, 2019)
