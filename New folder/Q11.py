def contains_spam(s):
    if "spam" in s.lower():
        print("This email contains SPAM!")
        return True
    else:
        return False

# test the function
contains_spam('Spam Spam Spam Spam')
