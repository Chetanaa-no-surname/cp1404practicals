"""
CP1404/CP5632 Practical
Programming language
"""
# Assumed we are not using functions since we are learning the basics of OOP

from prac_06.programming_language import ProgrammingLanguage

languages = []

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)


"""Adding the initialised languages into a list"""
languages.append(python)
languages.append(ruby)
languages.append(visual_basic)


print("The dynamically types languages are: ")
for language in languages:
    if language.is_dynamic() == True:
        print(language.name)
