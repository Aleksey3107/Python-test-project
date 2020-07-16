def cat_name():
    cat_names = []
    while True:
        print("Enter cat name or press Enter to finish")
        name = input()
        if name == '':
            break
        cat_names += [name]



cat_name()