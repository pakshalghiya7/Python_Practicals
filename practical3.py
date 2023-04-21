def group_anagrams(lst : list[strs]) -> dict[list]:
    
    """
    Groups the words in the given list into sets of anagrams.

    Args:

    lst (list): A list of words.

    Returns:

    dict: A dictionary mapping sorted strings of characters to lists of words that are anagrams of each other.

    """
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams


try:
    strs = eval(input("Enter Inputs In List Seperated by Commas : "))
    
    
    for item in strs:
        if len(strs) < 0 or len(strs) > 104:
            raise ValueError("Number of inputs must be between 1 and 104.")
           
        
        for sub in item:
            if sub.isupper():
             raise ValueError("Please Enter String In LowerCase")
            if len(item) >  100 or len(item) < 0:
                    raise ValueError("Bigger or Smaller String Entered than Expected")

        
    anagrams = group_anagrams(strs)
    print(list(anagrams.values()))

except ValueError as vError:
    print(f"Invalid input: {vError}")
except TypeError:
    print("Please enter valid String Input")
except Exception:
    print("An Error occurred. Please try again.")

