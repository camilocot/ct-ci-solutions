# Given a string and a set of characters, return the shortest substring containing all the characters in the set.

# We start with two pointers, left and right initially
# pointing to the first element of the string S.
# We use the right pointer to expand the window until we get a desirable window
# Once we have a window with all the characters,
# we can move the left pointer ahead one by one.
# If the window is still a desirable one we keep on updating the minimum window size.
# If the window is not desirable any more, we repeat step step2 onwards

import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        # Initialize a vector called hashmap, which contains the needed matching numbers of each character in s.
        hashmap = collections.Counter(t)
        # The total number of required characters
        counter = len(t)
        min_window = ""
        start, end = 0, 0

        for end in range(len(s)):

            # If there are still characters needed to be contained(increment i in this case), decrease the matching number of that character and check if it is
            # still non-negative. If it is, then it is the character in t, so decrease the total required number counter.
            if hashmap[s[end]] > 0:
                counter -= 1
            hashmap[s[end]] -= 1

            #   windows constrain is sastisfied
            while counter == 0:
                length = end - start + 1

                if not min_window or len(min_window) > length:
                    min_window = s[start:end+1]

                # advance begin index as far as possible
                # stop when advancing breaks window constraint
                hashmap[s[start]] += 1

                if hashmap[s[start]] > 0:
                    counter += 1

                start += 1
        return min_window
