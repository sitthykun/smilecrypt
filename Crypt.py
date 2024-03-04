"""
Author: masakokh
Year: 2024
Package: project
Note:
Version: 1.0.0
"""
# built-in
from typing import Any
# external
# internal
from Constants import Constants


class Crypto:
	"""

	"""
	def __init__(self, key: str, length: int= 3):
		"""

		:param key:
		:param length:
		"""
		# init
		self.__key      = key
		self.__length   = length

	def __unsign2Sign(self, value: int) -> int:
		"""

		:param value:
		:return:
		"""
		return value * (-1) if value < 0 else value

	def getKey(self) -> str:
		"""

		:return:
		"""
		return self.__key

	def getLength(self) -> int:
		"""

		:return:
		"""
		return self.__length

	def setKey(self, key: str) -> None:
		"""

		:param key:
		:return:
		"""
		self.__key      = key

	def setLength(self, length: int) -> None:
		"""

		:param length:
		:return:
		"""
		self.__length   = self.__unsign2Sign(length)
