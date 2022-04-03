import random
import string #to create a list of letters from A-Z

def password_generator():
    
    #Creation of characters list
    #we define the lists that we are going to fill
    list_up=[]
    list_low=[]
    list_sym=[]
    list_num=[]
    #with string, you could retrieve this lists
    upper=string.ascii_uppercase#as a string
    lower=string.ascii_lowercase
    symbols=string.punctuation
    numb=string.digits 
    #Finally it is added to lists
    for i in upper:             #to append it to a list
        list_up.append(i)
    for i in lower:
        list_low.append(i)
    for i in symbols:
        list_sym.append(i)
    for i in numb:
        list_num
    #then all added together
    characters=list_low+list_num+list_sym+list_up
    characters=str(characters)

    #Finally, We will create passwords with 15 random characters
    password=[]
    for i in range(15):
        characters_random=random.choice(characters) #with the random library
        password.append(characters_random)
    
    password="".join(password) #this function is applied to join all the characters in list
    
    return password

def run():
    password=password_generator()
    print('your new password is: '+password)


if __name__ =='__main__':
    run()

