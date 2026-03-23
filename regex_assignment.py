import re

# 1
print("1.")
tests1 = ["ABCDEFabcdef123450", "*&%@#!}{"]
for s in tests1:
    if re.match("^[A-Za-z0-9]+$", s):
        print(s, "-> Valid")
    else:
        print(s, "-> Invalid")

# 2
print("\n2.")
tests2 = ["ab", "abc", "a", "ab", "abb"]
for s in tests2:
    if re.match("^ab*$", s):
        print(s, "-> Match")
    else:
        print(s, "-> No match")

# 3
print("\n3.")
tests3 = ["ab", "abc", "a", "ab", "abb"]
for s in tests3:
    if re.match("^ab+$", s):
        print(s, "-> Match")
    else:
        print(s, "-> No match")

# 4
print("\n4.")
tests4 = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
for s in tests4:
    if re.match("^[a-z]+_[a-z]+$", s):
        print(s, "-> Match")
    else:
        print(s, "-> No match")

# 5
print("\n5.")
tests5 = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]
for s in tests5:
    result = re.match(r"\w+", s)
    if result:
        print(s, "->", result.group())
    else:
        print(s, "-> No match")

# 6
print("\n6.")
tests6 = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."
]
for s in tests6:
    result = re.findall(r"\b\w*z\w*\b", s)
    print(s, "->", result)

# 7
print("\n7.")
ip = "216.08.094.196"
parts = ip.split(".")
new_ip = ""
for p in parts:
    new_ip += str(int(p)) + "."
print("Original:", ip)
print("Updated :", new_ip[:-1])

# 8
print("\n8.")
text8 = "The quick brown fox jumps over the lazy dog."
words8 = ["fox", "dog", "horse"]
for word in words8:
    if re.search(word, text8):
        print(word, "found")
    else:
        print(word, "not found")

# 9
print("\n9.")
text9 = "The quick brown fox jumps over the lazy dog."
word = "fox"
match = re.search(word, text9)
if match:
    print(word, "found at position", match.start())
else:
    print(word, "not found")

# 10
print("\n10.")
tests10 = ["Regular Expressions", "Code_Examples"]
for s in tests10:
    if " " in s:
        print(s, "->", s.replace(" ", "_"))
    else:
        print(s, "->", s.replace("_", " "))

# 11
print("\n11.")
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Date:", match.group(3))

# 12
print("\n12.")
text12 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
words = text12.split()
for w in words:
    if w.lower().startswith("a") or w.lower().startswith("e"):
        print(w)

# 13
print("\n13.")
text13 = "Python Exercises, PHP exercises."
print(re.sub("[ ,\\.]", ":", text13))

# 14
print("\n14.")
text14 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
words = text14.split()
for w in words:
    if w.lower().startswith("a") or w.lower().startswith("e"):
        print(w)

# 15
print("\n15.")
text15 = "Python      Exercises"
print("Original:", text15)
print("Updated :", re.sub(r"\s+", " ", text15))
