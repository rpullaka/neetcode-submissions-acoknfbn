class Solution:
    def get_letters(self, digit) -> str:
        letter_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', 
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        return letter_map[digit]

    def letterCombinations(self, digits: str) -> List[str]:
        words = []
        cur_word = []
        self.helper(digits, cur_word, words)
        return words


    def helper(self, digits: str, cur_word: List, words: List[str]):
        if not digits:
            if cur_word:
                words.append(''.join(cur_word))
            return

        letters = self.get_letters(digits[0])
        for letter in letters:
            cur_word.append(letter)
            self.helper(digits[1:], cur_word, words)
            cur_word.pop()

        

        