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
    parser.add_argument('-c', '--center', type=str, required=True, help='Center letter')
    parser.add_argument('-o', '--other', type=str, required=True, help='Other letters')
    parser.add_argument('-m', '--min', type=int, default=4, help='Minimum word length')
    parser.add_argument('-d', '--dict', type=str, required=True, nargs='+',
                        help='Dictionary files')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    word_list = set()
    for word_file in args.dict:
        try:
            with open(word_file, 'r', encoding='utf-8') as file:
                word_list = word_list.union([line.strip() for line in file])
        except FileNotFoundError:
            print(f"File {word_file} not found.")

    all_letters = set(args.center.lower()).union(set(args.other.lower()))
    words = sorted([word for word in word_list
                    if set(args.center.lower()).issubset(word)
                    and set(word).issubset(all_letters)
                    and len(word) >= args.min])
    pangrams = [word for word in words if set(word) == all_letters]

    print(f'Total words: {len(words)}\nPangrams: {pangrams}\nValid words: {words}')
