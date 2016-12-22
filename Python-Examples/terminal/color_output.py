#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 22/Nov/16 14:19
Description:

https://en.wikipedia.org/wiki/ANSI_escape_code

ESC[ … 38;2;<r>;<g>;<b> … m Select RGB foreground color
ESC[ … 48;2;<r>;<g>;<b> … m Select RGB background color

In 256-color mode (ESC[38;5;<fgcode>m and ESC[48;5;<bgcode>m), the color-codes are the following:[citation needed]
0x00-0x07:  standard colors (as in ESC [ 30–37 m)
0x08-0x0F:  high intensity colors (as in ESC [ 90–97 m)
0x10-0xE7:  6 × 6 × 6 = 216 colors: 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
0xE8-0xFF:  gray scale from black to white in 24 steps
ESC is  (ASCII decimal 27/hex 0x1B/octal 033)

#################################################################
### Please set the width of your terminal as wide as possible ###
#################################################################
"""
print('\x1b[1m bold text\x1b[0m')  # bold

print('\x1b[1m standard eight colors \x1b[0m')
for color_code in range(30, 38):
	print('\x1b[' + str(color_code) + 'm' + str(color_code) + '\x1b[0m', end='\t')
print('\x1b[0m\n')  # reset color

print('\x1b[1m high intensity colors \x1b[0m')
for color_code in range(90, 98):
	print('\x1b[' + str(color_code) + 'm' + str(color_code) + '\x1b[0m', end='\t')
print('\x1b[0m\n')

print('\x1b[1m 256-color, foreground \x1b[0m')
for color_code in range(00, 256):
	print('\x1b[38;5;' + str(color_code) + 'm' + str(color_code).zfill(3) + '\x1b[0m', end='\t')
	if (color_code + 1) % 8 == 0:
		print('')
print('\x1b[0m\n')

print('\x1b[1m 256-color, background \x1b[0m')
for color_code in range(00, 256):
	print('\x1b[48;5;' + str(color_code) + 'm' + str(color_code).zfill(3) + '\x1b[0m', end='\t')
	if (color_code + 1) % 8 == 0:
		print('')
print('\x1b[0m\n')

print('\x1b[1m RGB-color, foreground \x1b[0m')
for R in range(0, 256, 32):
	for G in range(0, 256, 32):
		for B in range(0, 256, 32):
			print('\x1b[38;2;' + str(R) + ';' + str(G) + ';' + str(B) + 'm' +
						str(R).zfill(3) + '.' + str(G).zfill(3) + '.' + str(B).zfill(3) + '\x1b[0m',
						end='\t')
		print('')
print('\x1b[0m\n')

print('\x1b[1m RGB-color, background \x1b[0m')
for R in range(0, 256, 32):
	for G in range(0, 256, 32):
		for B in range(0, 256, 32):
			print('\x1b[48;2;' + str(R) + ';' + str(G) + ';' + str(B) + 'm' +
						str(R).zfill(3) + '.' + str(G).zfill(3) + '.' + str(B).zfill(3) + '\x1b[0m',
						end='\t')
		print('')

print('\x1b[0m\n')
