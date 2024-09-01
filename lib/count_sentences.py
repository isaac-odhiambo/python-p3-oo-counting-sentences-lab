#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        '''Returns True if the value ends with a period and False otherwise.'''
        return self._value.endswith('.')

    def is_question(self):
        '''Returns True if the value ends with a question mark and False otherwise.'''
        return self._value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark and False otherwise.'''
        return self._value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        # Define sentence end patterns: period, exclamation mark, or question mark
        sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings that result from splitting
        return len([s for s in sentences if s.strip()])
