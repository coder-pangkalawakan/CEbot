#a separate python file that stores the long responses to avoid messy code
import long

#Function to calculate similarity between strings
def calculate_similarity(user_input, keyword): 

    user_input = user_input.lower().split()  # splits user input to separate words
    keyword = keyword.lower().split()  # splits keyword to separate words
    
    # Calculate the number of common words
    set_user_input = set(user_input) #converts the user_input to set
    set_keyword = set(keyword) #converts the keyword to set
    common_words = set_user_input.intersection(set_keyword)
    num_common_words = len(common_words)
    
    # Calculate the total number of words
    total_words = len(user_input) + len(keyword)
    
    # Calculate similarity score as the ratio of common words to total words
    similarity_score = num_common_words / total_words
    
    return similarity_score

#Function to find the closest matching keyword to the user input
def get_closest_match(user_input, responses):

    #initital values
    best_match = None
    best_score = 0

    # Loop through each keyword in the responses
    for keyword in responses:
        # Calculate the similarity score between the user input and the keyword
        score = calculate_similarity(user_input, keyword)

        # If the current score is higher than the best score so far
        if score > best_score:
            # Update the best score and best match
            best_score = score
            best_match = keyword

    # Return the keyword with the highest similarity score
    return best_match

#Check if all required words are present in the user input.
def contains_required_words(user_input, required_words): 

    # Loop through each required word
    for word in required_words:
        # Check if the word is present in the user input
        if word not in user_input:
            # If any required word is not found, return False
            return False
    # If all required words are found, return True
    return True

#function that mainly handles user and bot interaction
def cebot():
    responses = {
        "hello": [("hello",), "Hello there!"],
        "how are you": [("how", "you"), "I'm just a bot, but thanks for asking!"],
        "bye": [("bye",), "Goodbye!"],
        "pogi": [("pogi",), "Thanks!"],
        "what is the mission of bsu": [("mission"), long.mission],
        # Add more keywords and responses here
    }
    #Loop to continually prompt user to input chat
    while True:
        #prompts the user to input something
        user_input = input("You: ").lower()

        closest_match = get_closest_match(user_input, responses)
        #checks if there is a word that closely matches
        if closest_match:
            response_tuple = responses[closest_match]  # Get the tuple from the responses dictionary
            required_words = response_tuple[0]  # Get the required words from the tuple
            response = response_tuple[1]  # Get the response from the tuple
            #if it does, then it returns a response
            if contains_required_words(user_input, required_words):
                print("Bot:", response)
                #the loop breaks if it recognizes bye from the user_input
                if closest_match == "bye":
                    break
            #if the user_input does not contain the required words from the tuple, it will ask you to rephrase it
            else:
                print("Bot: I'm sorry, can you rephrase that.")
        #if there is not word that closely matches, it prompts you to enter another message
        else:
            print("Bot: I'm sorry, I didn't understand that.")

#Greeting to the user
print("Bot: Hi, I'm CEbot. You can ask me anything about Civil Engineering at BSU-Alangilan!")
#calling the function cebot()
cebot()