def ispalindrome(name):
    name = name.replace(" ", "")
    if name == name[::-1]:
        return "Yes, it is a palindrome."
    else:
        return "No, it is not a palindrome."


def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"


def frequency_of_letters(name):
    name = name.replace(" ", "")  
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    result = ', '.join(f"{char}-{count}" for char, count in freq.items())
    return f"Frequency of letters: {result}"
