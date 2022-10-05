import collections

import Crypto.Hash.SHA256 as sha


def hash_t(transaction):
	return sha.new(str(transaction).encode('utf8')).hexdigest()


def build_merkel_tree(transactions):
	tmp = []

	for i in range(0, len(transactions)):
		transactions[i] = hash_t(transactions[i])
	print("---------Merkel tree---------\n")
	while (len(transactions) >= 2):
		for i in range(0, len(transactions), 2):
			tmp.append(hash_t(transactions[i] + transactions[i+1]))  # ket hasht osszekonkat aztan hash
		print("also szint")
		print(transactions)
		transactions = tmp
		print("felso szint")
		print(transactions)
		tmp = []

	return transactions[0]
