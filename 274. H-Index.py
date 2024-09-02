"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 

return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as 
    
    the maximum value of h such that the given researcher has published 
    
    at least h papers that have each been cited at least h times.

    Formally, if f is the function that corresponds to the number of citations for each publication, 
    
    we compute the h-index as follows: 
        
        First we order the values of f from the largest to the lowest value. 
        
        Then, we look for the last position in which f is greater than or equal to the position (we call h this position). 
        
        For example, if we have a researcher with 5 publications A, B, C, D, and E with 10, 8, 5, 4, and 3 citations, respectively, 
        
        the h-index is equal to 4 because the 4th publication has 4 citations and the 5th has only 3.

    
 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 
3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining 
two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        # Sort citations in decreasing order
        citations_sorted = sorted(citations, reverse=True) 

        # look for the last position in which f is greater than or equal to the position.
        for i, f in enumerate(citations_sorted):
            if f > i:
                h = i + 1

        return h


sol = Solution()
# Example 1: Output: 3
citations = [3,0,6,1,5]

print(sol.hIndex(citations=citations))


# Example 2: Output: 1
citations = [1,3,1]

print(sol.hIndex(citations=citations))


