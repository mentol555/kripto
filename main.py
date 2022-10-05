from transaction import *
from user import *
from merkel import *
from block import *


def main():
	blockchain = []

	Alice = User("Alice", 100)
	Bob = User("Bob", 100)
	Peter = User("Peter", 100)
	John = User("John", 100)
	t1 = Transaction(Alice, Bob, 100).get_transaction()
	Transaction(Alice, Peter, 100)  # nincs balance, nem mukodik
	t2 = Transaction(Bob, Alice, 50).get_transaction()
	t3 = Transaction(Bob, Peter, 50).get_transaction()
	t4 = Transaction(Peter, John, 50).get_transaction()
	transactions = [t1, t2, t3, t4]
	merkel_root = build_merkel_tree(transactions)

	prev_block_hash = None
	block1 = Block(merkel_root, prev_block_hash, 0).get_block()
	prev_block_hash = hash_block(block1)
	blockchain.append(block1)

	transactions = []
	merkel_root = ""

	t5 = Transaction(Alice, Bob, 1).get_transaction()
	t6 = Transaction(Alice, Peter, 1).get_transaction()
	t7 = Transaction(Alice, John, 1).get_transaction()
	t8 = Transaction(Alice, Peter, 2).get_transaction()
	transactions = [t5, t6, t7, t8]
	merkel_root = build_merkel_tree(transactions)

	block2 = Block(merkel_root, prev_block_hash, 1).get_block()
	prev_block_hash = hash_block(block2)
	blockchain.append(block2)
	transactions = []
	merkel_root = ""

	print("\n----------------------------------------------------------------")
	print("---------------------------Blockchain---------------------------")
	print("----------------------------------------------------------------")
	for i in range(0, len(blockchain)):
		print(json.dumps(blockchain[i], indent=4))


if __name__ == '__main__':
	main()
