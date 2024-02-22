import random

verbs = ['Leverage', 'Sync', 'Target',
        'Gsmify','Offline','Crowd-soursed',
        '24/7','Lean in','30 000 foort']

adjectives= ['A/B tested', 'Fremium',
            'Hyperlocal', 'Siloed','B-to-B',
            'Oriented','Cloud-based',
            'API-based']

nouns = ['Early Adopter', 'Low-hanging Fruit',
        'Pipeline','Splash page','Productivity',
        'Process','Tipping Point','Paradigm']

verb = random.choice(verbs)
adjective = random.choice (adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)