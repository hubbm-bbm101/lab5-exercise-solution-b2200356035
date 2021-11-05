def check_email(text):
    dot_counter = None
    sign_counter = None
    for i in text:
        if i=="@":
            sign_counter=True
        elif i==".":
            dot_counter=True
    if dot_counter and sign_counter:
        return "This is a valid e-mail"
    else:
        return "This is not a valid e-mail"
given=input("Please enter an e-mail: ")
print(check_email(given))
