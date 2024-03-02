"""
Author: masakokh
Year: 2024
Package: project
Note:
Version: 1.0.0
"""
# built-in
import random
from typing import Any
# external
# internal
from Constants import Constants


class Random:
	"""

	"""
	def __init__(self):
		"""

		"""
		self.__length   = 8

	def __generate(self, among: str, length: int= None) -> str:
		"""

		:param among:
		:param length:
		:return:
		"""
		# init
		length  = length if length else self.__length

		#
		return ''.join(random.choice(among) for _ in range(length))

	def generateAlphabet(self, mixCase: bool= False, length: int= None) -> str:
		"""

		:param mixCase:
		:param length:
		:return:
		"""
		return self.__generate(
			among   = f'{Constants.STR_LOWER}{Constants.STR_UPPER}' if mixCase else Constants.STR_LOWER
			, length= length
		)

	def generateAlphatbetUpper(self, length: int= None) -> str:
		"""

		:param length:
		:return:
		"""
		return self.__generate(
			among   = f'{Constants.STR_UPPER}'
			, length= length
		)

	def generateDecimal(self, length: int= None) -> str:
		"""

		:param length:
		:return:
		"""
		return self.__generate(
			among   = Constants.DECIMAL
			, length= length
		)

	def generateHex(self, mixCase: bool= False, length: int= None) -> str:
		"""

		:param mixCase:
		:param length:
		:return:
		"""
		return self.__generate(
			among   = Constants.HEXUL if mixCase else Constants.HEXL
			, length= length
		)

	def generateHexUpper(self, length: int= None) -> str:
		"""

		:param length:
		:return:
		"""
		return self.__generate(
			among   = Constants.HEXU
			, length= length
		)

	def generatePassword(self, among: str= None, length: int= None) -> str:
		"""

		:param among:
		:param length:
		:return:
		"""
		return self.__generate(
			among   = among if among else f'{Constants.DECIMAL}{Constants.STR_LOWER}{Constants.STR_UPPER}{Constants.STR_SYMBOL_P}'
			, length= length
		)
