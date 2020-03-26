class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()
        output = [];
        for c in str:
            if ord(c) <= 90 and ord(c) >= 65:
                output.append(chr(ord(c)+32));
            else:
                output.append(c);
        return "".join(output);
                
