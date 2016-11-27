import random

numberCorrect = 0

characters = {
    'Jack Sparrow': 'Captain of the Black Pearl',
    'Moana': 'Badass of Hawaii',
    'Luke Skywalker': 'Son of Darth Vader',
    'Mulan': 'Savior of China',
    'Mickey Mouse': 'The one that started it all',
    'Goofy': 'The silliest dog in the bunch',
    'Bambi': 'The lost little deer',
    'Tinker Bell': 'That sassy fairy that hangs out with Peter Pan',
    'Alice': 'That one little girl that gets lost in the rabbit hole',
    'Snow White': 'The one that eats the poison apple',
    'Hercules': 'The mythological hero with great strength',
    'Pocohantes': 'Paints with all the colors of the wind',
    'Rapunzel': 'Really, really, really long hair',
    'Flynn Rider': 'The guy Rapunzel falls in love with',
    'Merida': 'The bravest Scott of them all',
    'Pascal': 'That silly chameleon',
    'Darth Vader': 'Bad guy from \'Star Wars\'',
    'Baloo': 'The easy-going bear in the jungle',
    'Winnie The Pooh': 'Willy, nilly, silly old bear',
    'Mushu': 'The dragon with attitude from \'Mulan\'',
    'Belle': 'The bookworm',
    'Aladdin': 'Street rat',
    'Figaro': 'Obsessed with goldfish',
    'Lilo': 'Ohana means family',
    'Stitch': 'The cute little blue alien that lands in Hawaii',
    'Ariel': 'Look at this stuff...isn\'t it neat?',
}

print('Let\'s play a game!')
print('How well do you know your Disney characters?')
print('I\'ll put up a clue about a notable Disney character and you have to guess their name!')
print('Sounds fun, right?  Let\'s do this!\n')

hintNumber = 0
hintNumber += 1

character = random.choice(list(characters.keys()))
characterHint = characters[character]

guessedCharacter = None

while (guessedCharacter != character):
    character = random.choice(list(characters.keys()))
    characterHint = characters[character]

    print('Hint #{}'.format(hintNumber))
    print(characterHint)

    guessedCharacter = input()

    if (guessedCharacter == character):
        print('Right!')
        del characters[character]
        hintNumber += 1
        numberCorrect += 1
        print('Number correct: {}'.format(numberCorrect))
    else:
        print('Wrong!')
        del characters[character]
        hintNumber += 1

    if (characters == None):
        print('Game over!')
        print('Let\'s see how you did')
        if ((numberCorrect / 26) > .50):
            print('Not bad, more than half right')
        elif ((numberCorrect / 26) < .50):
            print('Your Disney knowledge could use some work')
        elif ((numberCorrect / 26) > .80):
            print('Wow!  On your way to perfection!')
        elif ((numberCorrect / 26) > .90):
            print('You\'re a Disney genius!')
        elif ((numberCorrect / 26) == .1):
            print('You got them all!')