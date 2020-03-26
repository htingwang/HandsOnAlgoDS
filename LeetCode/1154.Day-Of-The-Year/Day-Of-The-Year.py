class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, mon, day = date.split("-")
        #print(year, mon, day)
        if int(year) % 4 == 0 and int(year) % 100 != 0: days[1] = 29
        return sum(days[:int(mon) - 1])  + int(day)        
        
