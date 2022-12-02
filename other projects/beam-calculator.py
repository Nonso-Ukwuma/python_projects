#!/usr/bin/env python
# coding: utf-8

# In[59]:
'''
Assignment #3
Date: Oct 7, 2022
Authors: Nonso, Sunil, Vikash
'''


# In[60]:


def input_beam():
    '''
    This function gets the user's input and evaluates 
    the input to confirm if it a valid input
    and returns valid inputs to the calling function
    '''
    import sys
    print('Welcome to Big Steel Construction')
    
    counter = True
    while counter == True:
        no_beams = input('Please enter the length of beam needed in meters (q to quit): ')

        if no_beams == 'q':
            print('Thank you for using our system, good-bye.')
            #sys.exit()
            counter = False
            exit()
        else:
            if no_beams == '0':
                print('Zero length is not allowed')
                print('Please retry \n')
                #input_beam()
            elif float(no_beams) < 0:
                print('Only positive numbers allowed')
                print('Please retry \n')
                #input_beam()
            elif no_beams.isdigit() == False:
                print('Only integers allowed')
                print('Please retry \n')
                #input_beam()
            elif int(no_beams) > 365:
                print('Not enough stock, only 365m available')
                print('Please retry \n')
                #input_beam()
            else:
                counter = False
    
    return int(no_beams)
    


# In[61]:


def beam_calculator():
    '''
    This function calculates the number of beams
    based on the user's input and returns the breakdown
    of the best use of the available beams.
    '''
       
    beam_length = [30, 20, 5, 2, 1]
    beam_quantity = [4, 10, 5, 5, 10]
    beam = input_beam()
    temp = beam
    temp_count = [0, 0, 0, 0, 0]
    
    while temp > 0:
        for length in range(0, len(beam_length)):
            count = temp / beam_length[length]
            if count > 0:
                if count <= beam_quantity[length]:
                    temp_count[length] = int(count)
                    temp -= (int(count) * beam_length[length])
                else:
                    count = beam_quantity[length]
                    temp_count[length] = int(count)
                    temp -= (int(count) * beam_length[length])
                
    print('Beams to load on truck:')
    print(f'Quan \t Item')
    for temp in range(0, len(temp_count)):
        print(f'{temp_count[temp]} \t {beam_length[temp]:3}m')

    print('\n')
    beam_calculator()    


# In[62]:
beam_calculator()
