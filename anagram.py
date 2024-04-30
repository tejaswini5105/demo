def are_anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2

str1 = input().strip()
str2 = input().strip()

print(are_anagrams(str1,str2))