import random
from words import words

def get_valid_word(words):
  word = random.choice(words) #escolhe aleatoriamente alguma palavra da lista
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)  # letras na palavra
  alphabet = set(string.ascii_uppercase)
  used_letter = set()  # tentativa do usuário

  #recebendo a letra do usuário
  while len(word_letters) > 0:
    #letras usadas
    # ' '.join(['a', 'b', 'cd'] --> 'a b cd'
    print('Você usou as seguintes letras: ', ' '.join(used_letters))

    # qual palavra é (ie W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Palavra atual: ', ' '.join(word_list))
    
    user_letter = input('Advinhe a letra: ').upper()
    if user_letter in alphabet - used_lettersÇ
      used_letters.add(user.letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
  
    elif user_letter in used_lettersÇ
      print('Você já usou essa letra! Tente novamente!')
  
    else:
      print('Caractere inválido! Tente novamente!')  
  
# venha para cá quando len(word_letters) == 0

user_input = input('Type something')
