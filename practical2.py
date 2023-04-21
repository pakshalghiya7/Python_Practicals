def generate_parenthesis(n: int) -> list[str]:
    
    """
    Generates all combinations of well-formed parentheses for a given number n.

    Args:
        n (int): The number of pairs of parentheses to use.

    Returns:
        list[str]: A list of all combinations of well-formed parentheses.
    """

    if not isinstance(n, int) or n < 1 or n > 8:
        raise ValueError("Input must be an integer in the range of 1 to 8.")

    # Initialize an empty list to store the results
    results = []

    # Define a helper function that uses recursion to generate all possible combinations
    
    def generate_helper(left: int, right: int, parentheses: str):
        
        """
        A recursive helper function to generate all possible combinations of well-formed parentheses.

        Args:
            left (int): The number of left parentheses used so far.
            right (int): The number of right parentheses used so far.
            parentheses (str): The string of parentheses generated so far.

        Returns:
            None
        """
        
        # Base case: if we have used n left and right parentheses, add the result to the list of results

        if left == n and right == n:
            results.append(parentheses)
        
        else:

            # Recursive case: if we haven't used n left parentheses yet, add a left parenthesis

            if left < n:
                generate_helper(left + 1, right, parentheses + "(")

            # If we have used more left parentheses than right parentheses, add a right parenthesis

            if right < left:
                generate_helper(left, right + 1, parentheses + ")")

    # Start the recursion with zero left and right parentheses and an empty string of parentheses

    generate_helper(0, 0, "")
    return results


try:
    # Take user input for the number of pairs of parentheses

    n = int(input("Enter the number of pairs of parentheses: "))

    # Generate all well-formed parentheses combinations

    parentheses_combinations = generate_parenthesis(n)

    # Print the result as a list

    print(parentheses_combinations)

except ValueError as e:
    print(e)


#################################################

# The Same Logic Is Implemented using OOP Concepts

# class ParenthesisGenerator:
#     def __init__(self, n):
#         self.n = n
#         self.results = []

#     def generate(self):
#         """
#         Generates all combinations of well-formed parentheses for a given number n.

#         Returns:
#             list[str]: A list of all combinations of well-formed parentheses.
#         """
#         self._generate_helper(0, 0, "")
#         return self.results

#     def _generate_helper(self, left, right, parentheses):
#         """
#         A recursive helper function to generate all possible combinations of well-formed parentheses.

#         Args:
#             left (int): The number of left parentheses used so far.
#             right (int): The number of right parentheses used so far.
#             parentheses (str): The string of parentheses generated so far.

#         Returns:
#             None
#         """
#         if left == self.n and right == self.n:
#             self.results.append(parentheses)
#         else:
#             if left < self.n:
#                 self._generate_helper(left + 1, right, parentheses + "(")
#             if right < left:
#                 self._generate_helper(left, right + 1, parentheses + ")")


# n = int(input("Enter the number of pairs of parentheses: "))
# generator = ParenthesisGenerator(n)
# results = generator.generate()
# print(results)

################################################
