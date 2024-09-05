"""
There are n children standing in a line. 

Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.

Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Each child must have at least one candy.
        candies = [1] * len(ratings)

        # Check neighbors before on the left to right 
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Check neighbors after on the left to right 
        for i in range(len(ratings) -2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)  
    
        # Step 4: Calculate total candies needed
        min_candies = sum(candies)
        
        return min_candies


sol = Solution()
# Example 1: Output: 5
ratings = [1,0,2]

print(sol.candy(ratings=ratings))

# Example 2: Output: 4
ratings = [1,2,2]

print(sol.candy(ratings=ratings))
