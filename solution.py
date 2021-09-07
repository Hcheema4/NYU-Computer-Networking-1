### Collin Stilwell
### NYU Computer Networking

### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):


    if question ==  "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "The student should type the answer here"

    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"

    elif question ==  "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Yes"

    elif question ==  "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = 2

    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = 3

    return(answer)



if __name__ == "__main__":
    #use this space to debug and verify that the program works
    q1 = "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?"
    q2 = "Are encoding and encryption the same? - Yes/No"
    q3 = "Is it possible to decrypt a message without a key? - Yes/No"
    q4 = "Is it possible to decode a message without a key? - Yes/No"
    q5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    q6 = "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
    q7 = "Is MD5 a secured hashing algorithm? - Yes/No"
    q8 = "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
    q9 = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"

    print(welcome_assignment_answers(q1))
    print(welcome_assignment_answers(q2))
    print(welcome_assignment_answers(q3))
    print(welcome_assignment_answers(q4))
    print(welcome_assignment_answers(q5))
    print(welcome_assignment_answers(q6))
    print(welcome_assignment_answers(q7))
    print(welcome_assignment_answers(q8))
    print(welcome_assignment_answers(q9))
