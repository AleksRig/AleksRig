import random
def get_word():
   words = ['программирование', 'виселица', 'компьютер', 'питон', 'разработка', 'искусство', 'интеллект']
   return random.choice(words).upper()
def display_board(hidden_word, guessed_letters):
   print(' '.join(hidden_word))
   print('Угаданные буквы:', ' '.join(guessed_letters))
   print()
def play_game():
   word = get_word()
   hidden_word = ['_' for _ in word]
   guessed_letters = []
   attempts = 6
   print("Добро пожаловать в игру 'Виселица'!")
   print("Угадайте слово по буквам.")
   print(f"У вас есть {attempts} попыток.")
   print()
   while attempts > 0:
        display_board(hidden_word, guessed_letters)
        guess = input("Введите букву: ").upper()
        if guess in guessed_letters:
            print("Вы уже угадали эту букву. Попробуйте другую.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            if '_' not in hidden_word:
                display_board(hidden_word, guessed_letters)
                print("Поздравляем! Вы угадали слово!")
                break
        else:
            attempts -= 1
            print(f"Неправильная буква. У вас осталось {attempts} попыток.")
        if attempts == 0:
            print("К сожалению, вы проиграли. Загаданное слово было:", word)

if __name__ == "__main__":
    play_game()