class Date:
   
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def string_to_Date(cls, string_Date):
        day, month, year = map(int, string_Date.split('-'))
        return cls(day, month, year)

dt = Date.string_to_Date('31-12-2018')
print(dt.day)
print(dt.month)
print(dt.year)