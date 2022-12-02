#!/usr/bin/env python
# coding: utf-8

# In[88]:


def start_game():
    from word_supplier import get_word
    secret_word = get_word()
    count = 1
    word_test(secret_word, count)


# In[89]:


def get_input(count):
    myword = input(f'Try #{count} - Guess the word: ')
    return myword
    


# In[96]:


def word_test(sec, cnt):
    guess = get_input(cnt)
    cnt+= 1
    if guess.isalpha() and guess == guess.lower():
        if len(guess) == 6:
            g_words, c_words = word_check(sec, guess)
            if g_words == list(sec):
                print('\n You won!')
            else:
                if cnt >= 7:
                    print(f'You lost, the secret word was: {sec}')
                else:
                    print(f'Correct letters: {c_words}')
                    print(f'Correct placement {g_words} \n')
                    word_test(sec, cnt)
        else:
            print('Incorrect number of letters, Please enter only 6 words \n')
            word_test(sec, cnt)
    else:
        print('Invalid Entry, Please enter only small letter alphabets \n')
        word_test(sec, cnt)


# In[97]:


def word_check(secret, guessed):
    word_list = ['','','','','','']
    correct = []
    if secret[0] == guessed[0]:
        word_list[0] = guessed[0]
    if secret[1] == guessed[1]:
        word_list[1] = guessed[1]
    if secret[2] == guessed[2]:
        word_list[2] = guessed[2]
    if secret[3] == guessed[3]:
        word_list[3] = guessed[3]
    if secret[4] == guessed[4]:
        word_list[4] = guessed[4]
    if secret[5] == guessed[5]:
        word_list[5] = guessed[5]
    
    if guessed[0] in secret:
        correct.append(guessed[0])
    if guessed[1] in secret:
        correct.append(guessed[1])
    if guessed[2] in secret:
        correct.append(guessed[2])
    if guessed[3] in secret:
        correct.append(guessed[3])
    if guessed[4] in secret:
        correct.append(guessed[4])
    if guessed[5] in secret:
        correct.append(guessed[5])
        
    return word_list, correct


# In[98]:


start_game()


# In[ ]:




