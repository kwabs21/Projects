import random
word_list =["kelewele", "yaa Serwaa", "plausible deniability", "locomote"]

chosen_word = random.choice(word_list)
Length_of_Chosen_Word = len(chosen_word)
#print(chosen_word)




#for letter in chosen_word:
 #   if letter == Guess:
  #       print("Right")
   # else: print("Wrong")


# Length_of_Chosen_Word = len(chosen_word)
#
# Spaces = print("_")[Length_of_Chosen_Word]

display =[]
for _ in range(Length_of_Chosen_Word):
    display += "_"
livs = 6

end_of_game = False
while not end_of_game :
    Guess = input("Guess a letter ").lower()
    if Guess in display:
        print(f"You have already guessed {Guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == Guess:
            display[position] = letter
    if Guess not in chosen_word:
        livs-=1
        print(f"You guessed {Guess}. It is not in the word. You lose a life ")
        if livs==0:
            end_of_game= True
            print("You Lose!")
    print(display)

    if "_" not  in display:
        end_of_game=True
        print("You Win")