#!/usr/env/python
"""This code is to encapsulate the functions in
booking management for testing purpose"""
movie_list = {"Superman": 250, "Avengers": 300, "Hulk": 200, "Ironman": 400}
ADM_PWD = "password"


def movie_add(name):
    """This function is to add a new movie name and its price into the list of
        available movies"""
    if name not in movie_list.keys():
        return 1
    return 0


def movie_view():
    """This function is to view the list of available movies"""
    return 1


def movie_search(name):
    """This function is used to search a movie by its name"""
    if name in movie_list.keys():
        return 1
    return 0


def book_movie(movie):
    """This function is to get customer input and book tickets accordingly"""
    if movie in movie_list.keys():
        return 1
    return 0


def view_orders():
    """To view the list of movie bookings"""
    return 1


def log_in(passwd):
    """To aunthenticate the admin"""
    if passwd == ADM_PWD:
        return 1
    return 0
