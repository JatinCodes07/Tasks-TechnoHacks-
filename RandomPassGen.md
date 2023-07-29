The gen_pass(len) function generates a random password of a specified length. 
It first defines a string chars that contains all possible characters to be used in the password generation. 
This includes uppercase letters, lowercase letters, digits, and punctuation marks.
Using a list comprehension and random.choice, the function selects random characters from the chars string and concatenates them to form the password.
The number of characters selected is determined by the user-defined length.
The main() function is responsible for handling user input.
It prompts the user to enter the desired password length and then calls the gen_pass() function to generate the password.
Finally, the generated password is displayed to the user.
When you execute this Python script, it will ask you to input the desired password length. 
After entering the length, it will generate a random password using the specified characters and display it to you.
