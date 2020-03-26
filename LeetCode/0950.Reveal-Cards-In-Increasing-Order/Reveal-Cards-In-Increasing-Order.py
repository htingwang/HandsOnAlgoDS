class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        order = range(len(deck));
        ans = [0]*len(deck);
        deck.sort();
        for i in range(len(ans)):
            ans[order.pop(0)] = deck[i];
            if order:
                order.append(order.pop(0));
        return ans;
            
        
