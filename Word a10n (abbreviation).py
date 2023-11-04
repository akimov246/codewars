import re
#import regex as re

text = "elephant-rides are really fun!"
text2 = 'i17on' #'i18n'
text3 = 'cat. c25' #'cat. cat5'
text4 = "b5n; sat_b5n'm8c'd3y-"

# def abbreviate(string: str) -> str:
#     #pattern = re.compile(r"\w+|\W+")
#     #pattern = re.compile(r"[a-zA-Z0-9]+|\W+|_")
#     pattern = re.compile(r"[a-z]{4,}", re.IGNORECASE)
#     words = pattern.findall(string)
#     print(words)
#     for i in range(len(words)):
#         if len(words[i]) > 3:
#             first_letter = words[i][0]
#             rest = words[i][1:len(words[i])-1]
#             last_letter = words[i][-1]
#
#             num = re.search(r"\d+", rest)
#             if num:
#                 rest = rest[:num.start()] + rest[num.end():]
#                 rest_int = int((num.group())) + len(rest)
#                 words[i] = first_letter + str(rest_int) + last_letter
#             else:
#                 words[i] = first_letter + str(len(rest)) + last_letter
#
#     return "".join(words)

pattern = re.compile(r"[a-z]{4,}", re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(string: str):
    return pattern.sub(replace, string)

print(abbreviate(text))