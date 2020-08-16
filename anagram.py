
class Solution:
    from collections import Counter
    # @param A : tuple of strings
    # @return a list of list of integers

    def __init__(self):
        self.anagram = []
        self.anagram_index = []

    def is_anagram(self, word_1, word_2):
        word_1_count = Counter(word_1)
        word_2_coun t = Counter(word_2)
        if (word_1_count.items() == word_2_count.items()):

            return True
        else:
            return False

    def anagrams(self, A):
        self.anagram = A

        for index, word in enumerate(self.anagram):
            if index == len(self.anagram)-1:
                break

            for index_end, word_from_end in enumerate(self.anagram[::-1]):
                index_2 = len(self.anagram) - index_end
                if index_2-1 <= index:
                    break

                if self.is_anagram(word, word_from_end):

                    self.anagram_index.append([index+1, index_2])
                    break
                elif index_2-1 == index+1:
                    self.anagram_index.append([index + 1])
        if len(self.anagram) not in self.anagram_index:
            self.anagram_index.append(len(self.anagram))
        return self.anagram_index


from collections import Counter
A = ["abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]

for word in A:
    word_count = Counter(word)

    print(word_count)
word_list = ['cat', 'dog', 'god', 'tca']
solution = Solution()
solution.anagrams(A)
print(solution.anagram_index)
