from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticketdict = defaultdict(list)
        for ticket in sorted(tickets, reverse = True):
            ticketdict[ticket[0]].append(ticket[1])
        location = "JFK"
        ans = []
        stack = [location]
        while stack:
            top = stack[-1]
            if ticketdict[top]:
                stack.append(ticketdict[top].pop())
            else:
                ans.append(stack.pop())
        return ans[::-1]
