"""Contains classes for lenghts of time in absolute measure and in terms of the week."""
#6:2
HOURS_IN_DAY = 24
"""The day is broken up into 24 hours. """
CHALAKIM_IN_HOUR = 1080
"""The hour is broken up into 1080 chalakim (parts). This is just a number that has many divisors."""

# Defining a time interval and how to calculate with it
class timeInterval:
    """Used for the lenght of a month, year, etc."""

    def __init__(self, days=0, hours=0, chalakim=0):
        self.days = days
        self.hours = hours
        self.chalakim = chalakim
        self.reduce()

    #6:9
    def reduce(self):
        """Reduces the number of chalakim to less than 1080 and the hours to less than 24, adding the whole hours and whole days. Converts fractional parts of days and hours to hours and chalakim. Does not affect the day count."""
        # Convert fractional days into hours
        self.hours += (self.days % 1) * HOURS_IN_DAY
        self.days = int(self.days // 1)
        
        # Convert fractional hours into chalakim
        self.chalakim += (self.hours % 1) * CHALAKIM_IN_HOUR
        self.hours = int(self.hours // 1)

        # Fractional chalakim will be ignored untill the subclass fine time interval
        self.chalakim = int(self.chalakim // 1)

        # Carry the whole hours, then round the remaining chalakim. (This also works for negetive inputs.)
        self.hours += self.chalakim // CHALAKIM_IN_HOUR
        self.chalakim %= CHALAKIM_IN_HOUR
        
        # Carry the whole days, then round the remaining hours.
        self.days += self.hours // HOURS_IN_DAY
        self.hours %= HOURS_IN_DAY

        return self

    # iteration functions
    def __getitem__(self, key) -> int:
        if   key in {0, 'days'}: return self.days
        elif key in {1, 'hours'}: return self.hours
        elif key in {2, 'chalakim'}: return self.chalakim
        else: raise IndexError
    def __setitem__(self, key, value):
        if   key in {0, 'days'}: self.days = value
        elif key in {1, 'hours'}: self.hours = value
        elif key in {2, 'chalakim'}: self.chalakim = value
        else: raise IndexError
    def __iter__(self):
        yield from [self.days, self.hours, self.chalakim]
    
    # String function
    def __str__(self) -> str:
        return f"{self.days} {self.hours:>2} {self.chalakim:>4}"
   
    # Generator for comparing to either timeInterval or tuple
    def compare(this, that):
        if isinstance(that, timeInterval):
            yield this.days, that.days
            yield this.hours, that.hours
            yield this.chalakim, that.chalakim
        elif type(that) is tuple and len(that) == 3:
            yield this.days, that[0]
            yield this.hours, that[1]
            yield this.chalakim, that[2]
        elif type(that) is tuple and len(that) < 3:
            that += (0,0,0)
            yield this.days, that[0]
            yield this.hours, that[1]
            yield this.chalakim, that[2]
        else:
            raise TypeError("Can only compare timeInterval or tuple")
        
    # The following methods should work unchanged in a four item subclass.
    # comparison functions
    def __eq__(self, other) -> bool:
        for x,y in self.compare(other):
            if x == y: continue
            else: return False
        else: return True

    def __gt__(self, other) -> bool:
        for x,y in self.compare(other):
            if   x >  y: return True
            elif x == y: continue
            else: return False
        else: return False

    def __ge__(self, other) -> bool:
        for x,y in self.compare(other):
            if   x >  y: return True
            elif x == y: continue            
            else: return False
        return True

    def __lt__(self, other) -> bool:
        for x,y in self.compare(other):
            if   x <  y: return True
            elif x == y: continue          
            else: return False
        else: return False

    #math functions
    def __add__(self, addend):
        sum = timeInterval()
        for i, (x, y) in enumerate(self.compare(addend)):
            sum[i] = x + y
        return sum.reduce()
 
    def __sub__(self, subtrahend):
        difference = timeInterval()
        for i, (x, y) in enumerate(self.compare(subtrahend)):
            difference[i] = x - y
        return difference.reduce()

    def __mul__(self, factor):
        product = timeInterval()
        for i, x in enumerate(self):
            product[i] = x * factor
        return product.reduce()

    def __floordiv__(self, divisor):
        return self * (1 / divisor)

class timeInWeek (timeInterval):
    """A time of week, or the offset of a time of week."""
    def __init__(self, totalTime):
        totalTime = self.tuple_check(totalTime, "create time from")
        super().__init__(days= totalTime.days, hours= totalTime.hours, chalakim= totalTime.chalakim)

    def reduce(self):
        """Reduces the number of chalakim to less than 1080 and the hours to less than 24, adding the whole hours and whole days. Sets the day to a day of the week 1-7."""

        super().reduce()
        self.days %= 7
        # We want Shabbos to be appear as 7, even though its mod is 0.
        if self.days == 0 : self.days = 7

        return self

    def __add__(self, addend):
        return timeInWeek(super().__add__(addend))
    def __mul__(self, factor):
        return timeInWeek(super().__mul__(factor))
    def __sub__(self, subtrahend):
        return timeInWeek(super().__sub__(subtrahend))
    def __floordiv__(self, divisor):
        return timeInWeek(super().__floordiv__(divisor))