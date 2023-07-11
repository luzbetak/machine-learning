from textstat import textstat

# Here's a sample text
text = """
The Australian platypus is seemingly a hybrid of a mammal and reptilian creature. 
The platypus is categorized as a mammal because it has fur and feeds its young with milk. 
It is also one of the few venomous mammals; the male platypus has a spur on the hind foot that delivers a venom capable of causing severe pain to humans. 
The unique features of the platypus make it an important subject in the study of evolutionary biology and a recognizable and iconic symbol of Australia.
"""

# Now we can compute the Gunning Fog Index for this text
fog_index = textstat.gunning_fog(text)

print(f"The Gunning Fog Index of the text is: {fog_index}")

"""
OUTPUT:

The Gunning Fog Index of the text is: 12.28
"""
