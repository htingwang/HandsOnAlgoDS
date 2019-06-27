https://www.lintcode.com/problem/maximum-association-set

Description


Amazon sells books, every book has books which are strongly associated with it. Given ListA and ListB,indicates that ListA [i] is associated with ListB [i] which represents the book and associated books. Output the largest set associated with each other(output in any sort). You can assume that there is only one of the largest set.

The number of books does not exceed 5000.

Have you met this question in a real interview?  

Example

Example 1:

	Input:  ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"]
    
	Output:  ["abc","acd","bcd","dfe"]
    
	Explanation:
    
	abc is associated with bcd, acd, dfe, so the largest set is the set of all books
    
	
Example 2:

	Input:  ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"]
    
	Output:  ["d","e","f","g"]
    
	Explanation:
    
	The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]
