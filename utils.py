"""
    Name: utils.py
    Author: Adam Frisch
    Created: 9/27/22
    Purpose: A utility module with commonly used functions
"""
def get_title(program_title):
    """
        Takes in a string argument
        returns a string with ascii decorations
    """

    # Get the length of the statement
    text_length = len(program_title)

    # Create the title string
    
    title_string = "+--" + "-" * text_length + "--+\n"
    title_string = title_string + "|  " + program_title + "  |\n"
    title_string = title_string + "+--" + "-" * text_length + "--+"

    # Return the contatenated title string
    return title_string

def get_int(prompt):
   # Get an integer from the user with try catch
   # The prompt string parameter is used to ask the user
   # for the type of input needed

   # Declare local variable
   num = 0

   # Ask the user for an inout based on the prompt string parameter
   num = input(prompt)

   # If the input is numeric, convert to int and return value
   try:
      return int(num)

   # If the input is not numeric,
   # Inform the user and ask for input again
   except ValueError:
      print(f"You entered: {num}, which is not a whole number.")
      print(f"Let's try that again.\n")

      # Call function from the beginning
      # This is a recursive function call
      return get_int(prompt)
   
def main():
   print(title("Print Title Test!"))

def title(statement):
    # Takes in a string argument
    # Returns a string with ascii decorations

    # Get the length of the statement
    text_length = len(statement)

    # Create the title string
    # Initialize the result string variable
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result

def get_float(prompt :str):
   """
      Get a float from the user with try catch
      The prompt string parameter is used to ask the user
      for the type of input needed
   """
   # Declare local variable
   num = 0

   # Ask the user for an input based on the what parameter
   num = input(prompt)

   # If the input is numeric, convert to float and return value
   try:
      return float(num)

   # If the input is not numeric,
   # Inform the user and ask for input again
   except ValueError:
      print(f'You entered: {num}, which is not a number.')
      print(f"Let's try that again.\n")

      # Call function from the beginning
      # This is a recursive function call
      return get_float(prompt)

"""
def cm_to_inches(centimeters):
    inches = 0
    inches = centimeters / 2.54
    print(f'{centimeters:,.1f} centimeters is {inches:,.2f} inches')
    
def inches_to_cm(inches):
    centimeters = 0
    centimeters = inches * 2.54
    print(f'{inches:,.1f} inches is {centimeters:,.2f} centimeters')
    
def km_to_miles(kilometers):
    miles = 0
    miles = kilometers / 1.60928571
    print(f'{kilometers:,.1f} kilometers is {miles:,.2f} miles')
 
def miles_to_km(miles):
    kilometers = 0
    kilometers = miles * 1.60928571
    print(f'{miles:,.1f} miles is {kilometers:,.2f} kilometers')
 
"""        

# If  a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
