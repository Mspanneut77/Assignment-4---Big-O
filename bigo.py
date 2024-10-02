"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Mathis Spanneut and Mathis Spanneut, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: MS92374
"""


def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0
    for i in range(len(s)):
        letters = []
        num = 0
        for j in range(i, len(s)):
            if s[j] not in letters:
                num += 1
                letters.append(s[j])
            else:
                break

        max_length = max(max_length, num)

    return max_length

def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0
    num = 0

    while num < len(s):
        letters = set()
        max_num = num

        while max_num < len(s) and s[max_num] not in letters:
            letters.add(s[max_num])
            max_num += 1

        current = max_num - num
        max_length = max(max_length, current)
        num += 1

    return max_length

def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    start = 0
    max_length = 0
    dictionary = {}

    for i in range(len(s)):
        current = s[i]

        if current in dictionary and dictionary[current] >= start:
            start = dictionary[current] + 1

        dictionary[current] = i

        other_length = i - start + 1

        max_length = max(max_length, other_length)

    return max_length

