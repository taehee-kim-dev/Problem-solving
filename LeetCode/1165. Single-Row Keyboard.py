class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        answer = 0
        current_index = 0
        for char in word:
            new_index = keyboard.find(char)
            answer += abs(current_index - new_index)
            current_index = new_index
        return answer
