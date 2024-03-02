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
