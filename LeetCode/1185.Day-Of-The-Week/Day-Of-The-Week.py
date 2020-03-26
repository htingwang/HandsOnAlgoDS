class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s_days_in_month = [0] * 13

            
        if year % 4 == 0 and year % 4 != 100: days_in_month[1] = 29
        if year % 400 == 0: days_in_month[1] = 29
        for i in range(12):
            s_days_in_month[i + 1] = s_days_in_month[i] + days_in_month[i]
        #print(( year - 1971) // 4)
        res = 5
        res = (res + year - 1971 + ( year - 1968 - 1) // 4 - (year - 1900 - 1) // 100 + (year - 1600 - 1) // 400) % 7
        #print res
        #print s_days_in_month[month - 1]
        #print days_in_month[1]
        res = (res + s_days_in_month[month - 1] + day - 1) % 7
        #print res
        
        return weekday[res]
    #21 43
    #72 ,76 80 84 88 92
        
