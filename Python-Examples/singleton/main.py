#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 22/Dec/16 15:12
Description:
To create a singleton class, you subclass from Singleton; each subclass will have a single instance, no matter how many
times its constructor is called. To further initialize the subclass instance, subclasses should override 'init' instead
of __init__ - the __init__ method is called each time the constructor is called

"""


class Singleton(object):
	def __new__(cls, *args, **kwargs):
		it = cls.__dict__.get("__it__")
		print('******* new *****')

		# print(it)
		# print(cls)
		# print(cls.__dict__)
		if it is not None:
			return it
		cls.__it__ = it = object.__new__(cls)
		# it = object.__new__(cls)
		it.init(*args, **kwargs)
		return it

	def init(self, *args, **kwargs):
		print('init', args)
		self.data = args
		pass

	def __init__(self, *args):
		self.data = []
		print('__init__')


a = Singleton('a')
b = Singleton('b')
c = Singleton('c')

assert a == b == c
