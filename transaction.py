import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import logging
import datetime
import collections
import Crypto.Hash.SHA256 as sha
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15 as signer_object
from user import *


class Transaction:
	def __init__(self, sender: User, recipient: User, value):
		self.sender = sender
		self.recipient = recipient
		self.value = value
		self.timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

		print("------------------------------------------")
		print("Transaction:")
		print(json.dumps(self.get_transaction(), indent=4))
		signature = self.sign_transaction()
		print("\nsignature: " + format_signature(signature))
		try:
			## sender <-> recipient csere bizonyit
			self.sender.get_signer_object().verify(self.hash_transaction(), signature)
			print("The signature is valid.")
			if (sender.balance >= value):
				sender.balance -= value
				recipient.balance += value
				print("Success!")
				print(sender.name + " Successfully sent " + str(value) + " coins to: " + recipient.name + "\n")
			else:
				print("No sufficient balance")

		except ValueError:
			print("The signature is not valid.")

	def sign_transaction(self):
		signer = self.sender.get_signer_object()
		hashed = self.hash_transaction()
		return signer.sign(hashed)

	def hash_transaction(self):
		return sha.new(str(self.get_transaction()).encode('utf8'))

	def get_transaction(self):
		return collections.OrderedDict({
			'sender': self.sender.get_user_key(),
			'recipient': self.recipient.get_user_key(),
			'value': self.value,
			'time': self.timestamp
		})


def format_signature(signature):
	return binascii.hexlify(signature).decode('ascii')
