#!/usr/bin/env python
"""This code is to test booking_management functions"""
import movie_funcs as Movie_Management


def test_add():
    """To test movie_add function"""
    assert Movie_Management.movie_add("Superman") == 0
    assert Movie_Management.movie_add("Spiderman") == 1


def test_view():
    """To test movie_view function"""
    assert Movie_Management.movie_view() == 1


def test_search():
    """To test movie_search function"""
    assert Movie_Management.movie_search("Hulk") == 1
    assert Movie_Management.movie_search("Godfather") == 0


def test_book():
    """To test movie_book function"""
    assert Movie_Management.book_movie("Hulk") == 1


def test_orders():
    """To test view_orders function"""
    assert Movie_Management.view_orders() == 1


def test_login():
    """To test movie_login function"""
    assert Movie_Management.log_in("password") == 1
    assert Movie_Management.log_in("wrong") == 0
