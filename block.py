import collections
import datetime
import Crypto.Hash.SHA256 as sha


class Block:
	def __init__(self, merkel_root, prev_block_hash, serial):
		self.timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
		self.nonce = ""
		self.merkel_root = merkel_root
		self.prev_block_hash = prev_block_hash
		self.serial = serial

		find_nonce(self)

	def get_block(self):
		return collections.OrderedDict({
			'timestamp': self.timestamp,
			'nonce': self.nonce,
			'merkel_root': self.merkel_root,
			'prev_block_hash': self.prev_block_hash,
			'serial': self.serial
		})


def find_nonce(block):
	prefix = '000'
	for i in range(100000):
		block.nonce = i
		hash = hash_block(block.get_block())
		if hash.startswith(prefix):
			print("\n----------POW----------")
			print("hash: " + hash +"\nFound with nonce:"+str(i))
			return hash


def hash_block(block):
	return sha.new(str(block).encode('utf8')).hexdigest()
