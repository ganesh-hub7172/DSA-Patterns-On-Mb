class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",
            ".-.","...","-","..-","...-",".--","-..-","-.--","--.."
        ]

        seen = set()

        for word in words:
            code = ""
            for c in word:
                code += morse[ord(c) - ord('a')]
            seen.add(code)

        return len(seen)
