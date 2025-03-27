
print("Welcome to Mad Libs!")
print("Please provide the following words:")

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")
adjective3 = input("Enter a final adjective: ")

story = f"""
Once upon a time, there was a {adjective1} {noun1} who {verb_past} {adverb} through the forest.
Suddenly, they encountered a {adjective2} {noun2}!
"Wow," said the {noun1}, "that's the most {adjective3} {noun3} I've ever seen!"
And so they lived happily ever after.
"""

print("\nHere's your Mad Lib story:")
print(story)
