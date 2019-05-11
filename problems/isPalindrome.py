def is_palindrome(word):
    # Calling reverse function 
    rev =  word[::-1]  
  
    # Checking if both string are equal or not 
    if (word.lower() == rev.lower()): 
        return True
    return False
    
print(is_palindrome('Deleveled'))
