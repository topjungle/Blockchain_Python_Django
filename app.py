from flask import Flask, request, jsonify
from .blockchain import *

chain = Blockchain()
app = Flask(__name__)


@app.route('/mine', methods=['GET'])
def mine():
    last_block = chain.last_block
    last_proof = last_block['proof']
    proof = chain.proof_of_work(last_proof)
    block = chain.new_block(proof)
    response = {
        'index': len(chain) + 1,
        'poorf': proof,
        'previous_hash': chain.hash_block(last_block)
    }
    return jsonify(response), 200


@app.route('transactions/new', ['POST'])
def new():
    message = request.get_json()
    requirements = ['sender', 'recipient', 'amount']
    if not all(k in message for k in requirements):
        return "input incorrectly", 400
    index = chain.new_transaction(
        message['sender'],
        message['recipient'],
        message['amount'],

    )
    response = {
        "sender": message['sender'],
        'recipient': message['recipient'],
        'amount': message['amount'],
        'index': index,
    }
    return jsonify(response), 201


if __name__ == "__main__":
