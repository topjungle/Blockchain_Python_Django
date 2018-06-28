import hashlib
import json
from time import time


class Blockchain():

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof, previous_hash):
        """

        Args:
            proof: <int> proof of work
            previous_hash: <str> hash value of previous block

        Returns:<object> block

        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        self.current_transactions = []
        return block

    def new_transaction(self, sender, recipient, amount):
        """

        Args:
            sender: <str> specify the sender of the transaction
            recipient: <str> specify the recipient of the transaction
            amount: <int> amount

        Returns: <int> where the transaction is added

        """
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,

            }

        )

        index = self.last_block['index'] + 1
        return index

    def proof_of_work(self, last_proof):
        """

        Args:
            last_proof:

        Returns:<int> proof

        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """

        Args:
            last_proof:
            proof:

        Returns:

        """
        guess = f'{last_proof}{proof}'.encode()
        return hashlib.sha256(guess).hexdigest()[:4] == "0000"

    @staticmethod
    def hash_block(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
