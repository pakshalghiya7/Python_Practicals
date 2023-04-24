def group_anagrams (lst : list[str]) -> dict[list]:
    
    """
    Groups the words in the given list into sets of anagrams.

    Args:

    lst (list): A list of words.

    Returns:

    dict: A dictionary mapping sorted strings of characters to lists of words that are anagrams of each other.

    """

    # Initialize an empty dictionary to store the anagram groups
    anagrams = {}

    # Iterate over each word in the list
    for word in lst:

        # Sort the characters of the word and join them into a string
        sorted_word = ''.join(sorted(word))

        # Check if the sorted string already exists in the dictionary
        if sorted_word in anagrams:
            # If it does, add the current word to the corresponding list
            anagrams[sorted_word].append(word)
        else:
            # If it doesn't, create a new list and add the current word to it
            anagrams[sorted_word] = [word]

    # Return the dictionary of anagram groups
    return anagrams

# Get input from user and call the group_anagrams function
try:
    strs = eval(input("Enter Inputs In List Seperated By Commas : "))

    # Validate the input
    for item in strs:
        if len(strs) < 0 or len(strs) > 104:
            raise ValueError("Number of inputs must be between 1 and 104.")
        
        for sub in item:
            if sub.isupper():
                raise ValueError("Please Enter String In LowerCase")
            if len(item) >  100 or len(item) < 0:
                raise ValueError("Bigger or Smaller String Entered than Expected")

    # Group the anagrams and print the result
    anagrams = group_anagrams(strs)
    print(list(anagrams.values()))

except ValueError as vError:
    # Catch any ValueErrors thrown during input validation and print an error message
    print(f"Invalid input: {vError}")

except TypeError:
    # Catch TypeErrors thrown during input validation and print an error message
    print("Please Enter valid String Input")

except Exception:
    # Catch any other exceptions and print a generic error message
    print("An Error occurred. Please try again.")
