# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:24:56 2023

@author: steven.m
"""

import os

output_folder = 'output'  # Path to the folder where the modified .txt files will be stored

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt'):
        # Read the stock symbols from the input file
        with open(filename, 'r') as file:
            symbols = file.read().split(',')

        # Add "/SPY" to each symbol
        symbols_with_spy = [symbol.strip() + "/SPY" for symbol in symbols]

        # Write the modified symbols to the output file
        output_filename = os.path.splitext(filename)[0] + '_relative.txt'
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, 'w') as file:
            file.write(','.join(symbols_with_spy))


