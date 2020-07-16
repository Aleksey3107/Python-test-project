def add_spam():
    spam = []
    while True:
        spam_item = input("Enter some spam news: ")
        spam.append(spam_item)
        if spam_item == '':
            spam.pop(-1)
            break
    return spam


def return_spam(spam):
    spam_range = len(spam) - 2
    print(', '.join(spam[0:spam_range]) + ', and ' + spam[-1])


def runner():
    spam = add_spam()
    return_spam(spam)


runner()