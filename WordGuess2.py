import random
from os import system

#the start
print("██╗  ██╗███████╗██╗     ██╗      █████╗")
print("██║  ██║██╔════╝██║     ██║     ██╔══██╗")
print("███████║█████╗  ██║     ██║     ██║  ██║")
print("██╔══██║██╔══╝  ██║     ██║     ██║  ██║")
print("██║  ██║███████╗███████╗███████╗╚█████╔╝")
print("╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚════╝")
print()
print("██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗")
print("██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗")
print("██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝")
print("██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗")
print("██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║")
print("╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
print()
print("───────ＷＥＬＣＯＭＥ ＴＯ ＴＨＥ ＂ＷＯＲＤ ＧＵＥＳＳＩＮＧ＂ ＧＡＭＥ！─────────")
print()
print("───ＹＯＵ ＨＡＶＥ ＯＮＬＹ ６ ＡＴＴＥＭＰＴＳ ＴＯ ＧＵＥＳＳ ＴＨＥ ＷＯＲＤ！──")
print()
print("────────────────────────────ＡＲＥ ＹＯＵ ＲＥＡＤＹ？──────────────────────────────")
print()
print("─────────────────────────────ＴＨＥＮ ＬＥＴＳ ＳＴＡＲＴ────────────────────────────")



#choose a random word
def random_word(word_list):
    return random.choice(word_list)


#players guess and the random word
def the_word(word, guessed_letters):

    status = ''
    word_characters = list(word)
    
    guessed_letters_dict = {letter: True for letter in guessed_letters}
    
    for letter in word_characters:
        if letter.isalpha():
            if guessed_letters_dict.get(letter, False):
                status += letter
            else:
                status += '_'
        else:
            status += letter 
    return status



#HP bar and hearts
def hp_hearts(attempts_remaining, total_attempts):
    hearts = '🤍 ' * attempts_remaining + '🖤 ' * (total_attempts - attempts_remaining)
    return hearts

#loop to play more then 1 time
while True:
    
#words list
    word_list = [
    # A
    'abandon', 'ability', 'absence', 'academy', 'account', 'accuse', 'achieve', 'acquire', 'address', 'advance',
    # B
    'balance', 'battery', 'beautiful', 'because', 'bedroom', 'benefit', 'besides', 'between', 'beyond', 'billion',
    # C
    'calculate', 'campaign', 'capture', 'careful', 'carrier', 'category', 'celebrate', 'ceremony', 'certain', 'champion',
    # D
    'damage', 'danger', 'darkness', 'database', 'daughter', 'daylight', 'deadline', 'decade', 'decide', 'declare',
    # E
    'economy', 'edition', 'educate', 'effort', 'election', 'elegant', 'element', 'embrace', 'emergency', 'emphasis',
    # F
    'fabric', 'faculty', 'failure', 'famous', 'fashion', 'feature', 'feedback', 'festival', 'fiction', 'finance',
    # G
    'gallery', 'garbage', 'general', 'generate', 'gesture', 'gigantic', 'glimpse', 'govern', 'graduate', 'grammar',
    # H
    'habitat', 'handful', 'happiness', 'hardware', 'harmony', 'harvest', 'heading', 'healthy', 'hearing', 'heaven',
    # I
    'ideal', 'identify', 'ignorance', 'illegal', 'illness', 'imagine', 'impact', 'implement', 'improve', 'include',
    # J
    'jacket', 'january', 'jealous', 'jelly', 'jewel', 'join', 'journal', 'journey', 'joyful', 'justice',
    # K
    'kangaroo', 'keen', 'keeper', 'kettle', 'keyboard', 'kidnap', 'kindness', 'kingdom', 'kitchen', 'knight',
    # L
    'label', 'laboratory', 'landscape', 'language', 'laughter', 'launch', 'leader', 'learning', 'lecture', 'legend',
    # M
    'machine', 'magazine', 'magnitude', 'maintain', 'majority', 'manager', 'mandate', 'manner', 'manufacturer', 'marathon',
    # N
    'narrative', 'national', 'native', 'nature', 'navigation', 'neglect', 'negotiate', 'neighbour', 'network', 'neutral',
    # O
    'objective', 'obligation', 'observe', 'obtain', 'occasion', 'occupation', 'occur', 'offense', 'official', 'operate',
    # P
    'package', 'painting', 'parallel', 'parent', 'particle', 'passenger', 'password', 'patient', 'pattern', 'payment',
    # Q
    'qualification', 'quality', 'quantity', 'quarter', 'question', 'quickly', 'quietly', 'quotation', 'quote', 'quiver',
    # R
    'radical', 'railway', 'random', 'rapidly', 'rarely', 'reaction', 'realize', 'reality', 'reason', 'rebuild',
    # S
    'sacred', 'safety', 'salary', 'sample', 'satisfy', 'science', 'season', 'secret', 'secure', 'segment',
    # T
    'table', 'tackle', 'talent', 'target', 'teacher', 'technique', 'telephone', 'temperature', 'temporary', 'tendency',
    # U
    'ultimate', 'umbrella', 'unaware', 'uncertain', 'undergo', 'understand', 'unfold', 'uniform', 'unique', 'universe',
    # V
    'vacation', 'valid', 'valuable', 'variety', 'vehicle', 'venture', 'version', 'vessel', 'veteran', 'victory',
    # W
    'wage', 'waste', 'wealth', 'weather', 'wedding', 'weekend', 'welfare', 'western', 'whisper', 'widespread',
    # X
    'xenon', 'xerox', 'xylophone', 'xenophobia', 'xenolith', 'xenogenesis', 'xenonlamp', 'xanthophyll', 'xenotropic', 'xenograft',
    # Y
    'yacht', 'yearly', 'yellow', 'yield', 'young', 'youthful', 'yummy', 'yearn', 'yawn', 'yonder',
    # Z
    'zeal', 'zebra', 'zero', 'zest', 'zigzag', 'zinc', 'zone', 'zoology', 'zoom', 'zucchini', 'zmal'
    ]


    word_to_guess = random_word(word_list)
    guessed_letters = []
    total_attempts = 6
    attempts_remaining = total_attempts
    guessed_correctly = False
    

#players status(HP) #Guess the word: # Guess a letter(1 letter each time)
    while attempts_remaining > 0 and not guessed_correctly:
        print()
        print("Word to guess:", the_word(word_to_guess, guessed_letters))
        print("HP:", hp_hearts(attempts_remaining, total_attempts))
        guess = input("Guess a letter: ").lower()
        system("cls||clear")
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts_remaining -= 1
            print("Incorrect guess. Attempts remaining:", attempts_remaining)
        
        if all(letter in guessed_letters for letter in word_to_guess):
            guessed_correctly = True
    

    if guessed_correctly:
        print()
        print("Congratulations! You've guessed the word correct🤩, you win!🥳:")
        print("The word:", word_to_guess)
    else:
        print()
        print("You've run out of HP, your dead ☠. The word was:", word_to_guess)

#play again or finish
    again = input("Want to play again?(Y / N): ").lower().strip()
    if again != "y":
        break
    else:
        print()
