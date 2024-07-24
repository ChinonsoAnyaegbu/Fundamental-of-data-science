# Define a dictionary to store user data

Users = {
 1: {"First name": "Chinonso ","Last name":"Isaacs","Email address":"mynameischinonso.email","Password": "12345"},
 2: {"First name": "John","Last name":"Doe","Email address":"john.doe.email","Password": "67890"},
 3: {"First name": "Jane ","Last name":"Smith ","Email address":"jane.smith.email","Password": "abcde"},
}
# Print the Users dictionary to check its contents (for debugging purposes)

print(Users)

# Start an infinite loop to continuously prompt the user for their email and password

while True:
 # Prompt the user to enter their email address
 userEmail = input("What is your Email address? ")

 # Prompt the user to enter their password
 userPassword = input("What is your password? ")

# Iterate through the Users dictionary to check for a match
    
 for userId, userInfo in Users.items():
    if userInfo["Email address"] == userEmail and userInfo["Password"] == userPassword:
     print (f"Hello {userInfo['First name']} {userInfo['Last name']}, you have successfully logged in")
     
    # Exit the program after successful login
     exit()

 # If no match is found, print an error message and prompt the user to try again
 print("Incorrect email or password try again")