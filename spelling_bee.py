#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate valid words for the New York Times Spelling Bee puzzle.

Copyright 2024 Arun K Viswanathan
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""
import argparse


def parse_arguments():
    """
    Parse command-line arguments for the Spelling Bee puzzle.

    The arguments include the center letter, other letters, minimum word length, and the
    dictionary file for the Spelling Bee puzzle.

    Returns:
    Namespace: An argparse.Namespace object with the parsed arguments as attributes.
    """
    parser = argparse.ArgumentParser(description='Spelling Bee')
    parser.add_argument('-c', '--center', type=str, required=True,
                        help='Center letter')
    parser.add_argument('-o', '--other', type=str, required=True,
                        help='Other letters')
    parser.add_argument('-m', '--min', type=int, default=4,
                        help='Minimum word length')
    parser.add_argument('-d', '--dict', type=str, required=True,
                        help='Dictionary file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    try:
        with open(args.dict, 'r', encoding='utf-8') as file:
            word_list = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File {args.dict} not found.")
        word_list = []
    center_letter_set = set(args.center.lower())
    letters_set = center_letter_set.union(set(args.other.lower()))
    valid_words = [word for word in word_list
                   if center_letter_set.issubset(word)
                   and set(word).issubset(letters_set)
                   and len(word) >= args.min]
    words = sorted(valid_words, key=len, reverse=True)
    pangrams = [word for word in words if set(word) == letters_set]
    print(f'Total words: {len(words)}')
    print(f'Pangrams: {pangrams}')
    print(f'Valid words: {words}')
