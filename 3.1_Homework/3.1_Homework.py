########################
# CASE STUDY 1 EXERCISES
########################
# A cipher is a secret code for a language. In this case study, we will explore a cipher that is reported by
# contemporary Greek historians to have been used by Julius Caesar to send secret messages to generals during times of
# war.
# The Caesar cipher shifts each letter of a message to another letter in the alphabet located a fixed distance from the
# original letter. If our encryption key were 1, we would shift h to the next letter i, i to the next letter j, and so
# on. If we reach the end of the alphabet, which for us is the space character, we simply loop back to a. To decode the
# message, we make a similar shift, except we move the same number of steps backwards in the alphabet.
# In the five exercises of this homework, we will create our own Caesar cipher, as well as a message decoder for this
# cipher.

#   Exercise 1:
#       In Exercise 1, we will define the alphabet used in the cipher.
#       The sample code imports the string library has been imported. Create a string called alphabet consisting of the
#       space character (' ') followed by (concatenated with) the lowercase letters. Note that we're only using the
#       lowercase letters in this exercise.
#       Sample code:
#           import string
#           # write your code here!
#       What is the correct way to create the alphabet string using the string library?
#   Solution 1:
        import string
        alphabet = " " + string.ascii_lowercase # This is the solution

#   Exercise 2:
#       In Exercise 2, we will define a dictionary that specifies the index of each character in alphabet.
#       Note that alphabet is as defined in Exercise 1. Create a dictionary with keys consisting of the characters in
#       alphabet and values consisting of the numbers from 0 to 26. Store this as positions.
#       What is the value of the key n in the positions dictionary?
#   Solution 2:
        positions = {} # Create 'positions' dictionary
        index = 0 # Start at 0
        for char in alphabet: # For all of the characters in alphabet
            positions[char] = index # Assign the character with value = index
            index += 1 # Update index to be the last index + 1
        positions['n'] # Returns "14"

#   Exercise 3:
#       In Exercise 3, we will encode a message with a Caesar cipher.
#       Note that alphabet and positions are as defined in Exercises 1 and 2. Use positions to create an encoded message
#       based on message where each character in message has been shifted forward by 1 position, as defined by positions
#       Note that you can ensure the result remains within 0-26 using result % 27.
#       Store this as encoded_message.
#       Use this code to get started:
#           message = "hi my name is caesar"
#           # write your code here!
#       What is encoded_message?
#   Solution 3:
        message = "hi my name is caesar" # Message to encode
        encoded_message = "" # Create empty string
        for i in range(0,len(message)): # Loop starting at zero and ending on the last letter of the message
            if message[i] in alphabet: # Check if letter/element is in the alphabet string
                x = positions[message[i]] # Store positions of letters in message in x
                encoded_message += alphabet[x+1] # Shift the positions of the alphabet by 1
            else:
                encoded_message += " " # If you can't +1, concatenate an empty space
        encoded_message # Returns "ijanzaobnfajtadbftbs"

        # Can also use:
        encoding_list = [] # Create an empty list
        for char in message: # Loop over all the characters in the message
            position = positions[char] # Create position object that stores position of character
            encoded_position = (position + 1) % 27 # Shift position of the alphabet by 1, ensuring it's in range
            encoding_list.append(alphabet[encoded_position]) # Append the shifted position to the empty list
        encoded_message = "".join(encoding_list) # Concatenate an empty string to encoding list and store in object

        encoded_message # Returns "ijanzaobnfajtadbftbs"

#   Exercise 4:
#       In this Exercise 4, we will define a function that encodes a message with any given encryption key.
#       Use alphabet, position, and message as defined in Exercises 1 through 3. Define a function encoding that takes a
#       message as input as well as an int encryption key key to encode a message with the Caesar cipher by shifting
#       each letter in message by key positions.
#       Your function should return a string consisting of these encoded letters.
#       Use encoding to encode message using key = 3 and save the result as encoded_message. Print encoded_message.
#       What is the new encoded_message?
#   Solution 4:
        def encoding(message, key=0): # Define a function that will take the message and key to shift by - starting at 0
            encoding_list = [] # Create an empty list
            for char in message: # Loop over all the characters in the message
                position = positions[char] # Create position object that stores position of character
                encoded_position = (position + key) % 27 # Shift position of the alphabet by key, ensuring it's in range
                encoding_list.append(alphabet[encoded_position]) # Append the shifted position to the empty list
            encoded_string = "".join(encoding_list) # Concatenate an empty string to encoding list and store in object
            return encoded_string # Return the encoded string
        encoded_message = encoding(message, 3) # Call the function and shift the message by 3
        print(encoded_message) # Returns "klcpacqdphclvcfdhvdu"

#   Exercise 5:
#       In Exercise 5, we will decode an encoded message.
#       Instructions
#       - Use encoding to decode encoded_message.
#       - Store your encoded message as decoded_message.
#       - Print decoded_message. Does this recover your original message?
#       What key can be used to decode the message and recover the original message shifting backwards?
#   Solution 5:
        decoded_message = encoding(encoded_message, -3) # Call the function and shift the encoded message by -3
        print(decoded_message) # Returns "hi my name is caesar"
        # The answer is "-3"