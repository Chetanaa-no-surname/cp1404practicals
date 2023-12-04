"""
Word Occurrences
Estimate: 30 minutes
Actual:   16 minutes
"""

text = input("Enter Text: ").lower()
text_list = text.split()

occurrences = {}

for word in text_list:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

sorted_occurrence = sorted(occurrences)

max_length = 0
for word in sorted_occurrence:
    if len(word) > max_length:
        max_length = len(word)

for word in sorted_occurrence:
    print(f"{word:{max_length:<}} : {occurrences[word]}")
