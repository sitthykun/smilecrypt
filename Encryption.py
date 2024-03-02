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
from Crypt import Crypto


class Encryption(Crypto):
	"""

	"""
	def __init__(self, key: str, length: int= 10):
		"""

		:param key:
		:param length:
		"""
		super().__init__(key, length)
