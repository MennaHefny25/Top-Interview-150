"""
Given an array of strings words and a width maxWidth, 

format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 

Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 

If the number of spaces on a line does not divide evenly between words, 

the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution(object):
  def fullJustify(self, words, maxWidth):

        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        result = []
        line_words = []
        line_length = 0
        n = len(words)
        
        i = 0
        while i < n:
            # Check if we can add the current word to the current line
            if line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1
            else:
                # Justify the current line
                if len(line_words) == 1:
                    # Special case: single word in line
                    result.append(line_words[0] + ' ' * (maxWidth - len(line_words[0])))
                else:
                    total_spaces = maxWidth - line_length
                    base_spaces = total_spaces // (len(line_words) - 1)
                    extra_spaces = total_spaces % (len(line_words) - 1)
                    
                    justified_line = ''
                    for j in range(len(line_words) - 1):
                        justified_line += line_words[j]
                        justified_line += ' ' * (base_spaces + (1 if j < extra_spaces else 0))
                    
                    justified_line += line_words[-1]  # last word without trailing spaces
                    result.append(justified_line)
                
                # Reset line variables
                line_words = []
                line_length = 0
        
        # Last line (left-justified)
        last_line = ' '.join(line_words)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result


sol = Solution()
# Example 1:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(sol.fullJustify(words=words, maxWidth=maxWidth))
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

print(sol.fullJustify(words=words, maxWidth=maxWidth))
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", 
# because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

print(sol.fullJustify(words=words, maxWidth=maxWidth))
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

