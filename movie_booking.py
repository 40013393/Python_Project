#!/usr/bin/env python
"""This code is to facilitate and automate booking management"""
movie_list = {"Superman": 250, "Avengers": 300, "Hulk": 200, "Ironman": 400}
ADM_PWD = "password"
ADM_VAL = 0


def movie_add(name):
    """This function is to add a new movie name and its price into the list of
    available movies"""
    while True:
        try:
            price = int(input("Enter the ticket price: "))
            break
        except ValueError:
            print("Invalid input")
    if name not in movie_list.keys():
        movie_list[name] = price
        print("Movie added successfully")
        return 1
    print("\nMovie already exists")
    return 0


def movie_view():
    """This function is to view the list of available movies"""
    print("Movies running now")
    cnt = 1
    for i in movie_list.keys():
        print("{} Movie Name: {:<10} Price: {}".format(cnt, i, movie_list[i]))
        cnt = cnt+1
    return 1


def movie_search(name):
    """This function is used to search a movie by its name"""
    if name in movie_list.keys():
        print(name, "is currently running\n")
        return 1
    print("\nMovie not available\n")
    return 0


def book_movie(c_name=" "):
    """This function is to get customer input and book tickets accordingly"""
    movie = input("Choose the movie you wish to watch: ")
    while True:
        try:
            total_ticket = int(input("Enter the total number of seats: "))
            break
        except ValueError:
            print("Invalid input")
    if movie in movie_list.keys():
        price = movie_list[movie]
        cost = (price.__mul__(total_ticket))  # using magic method mul
        if ADM_VAL == 1:
            print("Congrats!!!You received admin discount")
            c_name = input("Enter your name")
            cost = cost.__sub__(100)  # using magic method sub
        print("Movie booked succesfully")
        print("Amount to be paid: ", cost, "\n")
        with open("info.txt", "a") as dat:
            dat.write("Customer name: " + c_name + "\t")
            dat.write("Movie booked: " + movie + "\t")
            dat.write("Tickets booked: " + str(total_ticket) + "\t")
            dat.write("Total cost: " + str(cost) + "\n")
        return 1
    print("\nMovie not available")
    return 0


def log_in(passwd):
    """To aunthenticate the admin"""
    if passwd == ADM_PWD:
        return 1
    return 0


def view_orders():
    """To view the list of movie bookings"""
    with open("info.txt", "r") as dat:
        print(dat.read())
        dat.close()
    return 1


def set_adm():
    """To set"""
    global ADM_VAL
    ADM_VAL = 1


def unset_adm():
    """To unset"""
    global ADM_VAL
    ADM_VAL = 0


def menu():
    """Acts as the home screen"""
    while True:
        print("\n\nWelcome to the home screen\n")
        print("Enter 1 to add a movie")
        print("Enter 2 to view all movies")
        print("Enter 3 to search a movie")
        print("Enter 4 to book tickets")
        print("Enter 5 to view bookings")
        print("Enter any other keys to exit\n")
        while True:
            try:
                choice = int(input())
                break
            except ValueError:
                print("Invalid option")
        if choice == 1:
            passwd = input("Enter the password for admin log-in: ")
            if log_in(passwd):
                name = input("Enter the movie you want to add: ")
                movie_add(name)
            else:
                print("Wrong admin password")
        elif choice == 2:
                movie_view()
        elif choice == 3:
            movie = input("Enter the movie you want to search: ")
            movie_search(movie)
        elif choice == 4:
            print("Want to view movies as admin or customer")
            opt = int(input(("Enter 1 for admin\nEnter 2 for customer")))
            if opt == 1:
                passwd = input("Enter the password for admin log-in: ")
                if log_in(passwd):
                    set_adm()
                    book_movie()
                    unset_adm()
            elif opt == 2:
                person = input("Enter your name: ")
                book_movie(person)
        elif choice == 5:
            passwd = input("Enter the password for admin log-in: ")
            log_in(passwd)
            view_orders()
        else:
            break
menu()
