from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result_morse_codes = set()
        morse_code_map = dict()
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for ascii_number, morse_code in zip(range(97, 122 + 1), morse_codes):
            morse_code_map[chr(ascii_number)] = morse_code

        for word in words:
            converted_morse_code = ''
            for char in word:
                converted_morse_code += morse_code_map[char]
            result_morse_codes.add(converted_morse_code)

        return len(result_morse_codes)


Solution().uniqueMorseRepresentations([])
