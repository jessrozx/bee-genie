#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:19:30 2024

@author: jessicaorozco
"""
from flask import Flask, render_template, request
import re
import urllib.request
import string
import os

app = Flask(__name__)

# Function to filter words
def filter_words(center_letter, other_letters):

    with app.open_resource('static/collins_scrabble_words_2019.txt') as f:
        response = f.read()
    data = response.decode('utf-8')
    word_list = data.splitlines()
    short_words_uppercase = [word.upper() for word in word_list if len(word) > 3]
    seven_letters = center_letter + other_letters
    need = seven_letters[0]
    bad_letters = ''.join(letter for letter in string.ascii_uppercase if letter not in seven_letters)
    pattern = "[" + re.escape(bad_letters) + "]"
    filtered_words = [word for word in short_words_uppercase if not re.search(pattern, word) and need in word]
    filtered_words = sorted(filtered_words, key=lambda x: (len(x), x))
    return filtered_words

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/filter', methods=['POST'])
def filter():
    center_letter = request.form['center_letter'].upper()
    other_letters = request.form['other_letters'].upper()
    filtered_words = filter_words(center_letter, other_letters)
    return render_template('result.html', filtered_words=filtered_words)
if __name__ == '__main__':
    app.debug = False
 


