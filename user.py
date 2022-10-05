from kripto import *
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15 as signer_object
import binascii


class User:
	def __init__(self, name, balance):
		self._private_key = RSA.generate(1024)
		self._public_key = self._private_key.publickey()
		self._signer_object = signer_object.new(self._private_key)
		self.balance = balance
		self.name = name

	def get_user_key(self):
		return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

	def get_signer_object(self):
		return self._signer_object

