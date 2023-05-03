import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# notes the most similar items are apple and banana becuase they are both fruit
# monkey and banana are fairly similar becuase of the association of monkeys eating bananas.
# Cat and banana and cat and apple are the lowest becuase there is not much to associate the two pairs together.


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# when using the en_cor_web_sm a warning is displayed. the sm version does not seem to have the necessary components to process word similarities accurately. 
# the resulting similarity index returned is diffferent to when the md version is used.