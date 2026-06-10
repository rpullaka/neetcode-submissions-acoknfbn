'''
List out all substrings
create a map for each
check for dup chars
keep track of lss
T: O(N*N) + O(N) -> O(N^2)
S: O(N*N*N) -> O(N^3)
'''

'''
[Notes]
1st attempt has bugs. All test cases failed.
2nd attempt. Fixed a few bugs. Still tests are failing.
3rd attempt. Able to fix the bug finally and get the code to run. However, the time complexity is bad. Got time limit exceeded for a couple of test cases.
4th attempt. Got all test cases passing. Did one optimization where we don't move forward if the substring so far is already not good.
'''
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lss = None
        lss = ''    # [Miss] Should initialize lss to empty string instead of None because checking for len(lss) would be bad if it's None

        # base
        if not s:
            return 0

        # code
        # i = 0
        # j = 0
        # # while i >= 0 and i < len(s) and j >= 0 and j < len(s):
        for i in range(len(s)):
            for j in range(len(s) + 1):
                substr = s[i:j]
                c_substr = Counter(substr)
                # for v in c_substr.values():   #[Miss] This for loop is unnecessary
                #     if v > 1: # [Miss] This condition is a massive bug. Didn't catch it for a long time. We are trying to verify if count of each char in the string is 1. This will pass if there's no char with count 1 which is bad.
                #         continue
                    # if lss and len(substr) > len(lss): # [Miss] This is a major bug. Couldn't identify it before running tests.
                    # if len(substr) > len(lss):    #[Miss] This is not enough.
                # if all(v == 1 for v in c_substr.values()) and len(substr) > len(lss):   # [Weakpoint] Didn't know we could use all()
                #     lss = ''.join(substr)
                # [Question] Is there a better way to breakpoint the if condition above instead of the way I'm doing below?
                if all(v == 1 for v in c_substr.values()):
                    if len(substr) > len(lss):
                        lss = ''.join(substr)
                else:
                    break   # No point moving forward since the substr already is imbalanced.
                # else:
                    # break   # [Miss] Thought breaking here would mean that if we found a substring that already violated at most 1 count per char, then it would be meaningless to continue. However, all test cases failed. May be "break" here is a bad idea.
        if lss: # [Miss] Didn't check this 1st time
            return len(lss)
        return 0
'''
Complexity

T : O(N^3)
S : O(N^3)
'''