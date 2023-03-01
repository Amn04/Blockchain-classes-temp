from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import argparse
import os
import uuid 
from datetime import datetime

def create_block(prev) :
    
    dt = datetime.now()
    ts=datetime.timestamp(dt)
    nonce= uuid.uuid4().hex
    data = input("Enter block chain data:")
    digest = hashes.Hash(hashes.SHA256(),256)
    digest.update(bytes(data,encoding = 'utf8'))
    hash_data= digest.finalize()
    print (" ")
    print("nonce:" , nonce)
    print("data:" , data)
    print("Timestamp: ", ts)
    print("prev: ", prev)
    print("Hash : ", hash_data)
    return hash_data

prev = "00000000000000000000000000000000"
prev = create_block(prev)
print(" ")
print("Next block------->")
prev= create_block(prev)
print("Next block------->")
prev= create_block(prev)
print("Next block------->")
prev= create_block(prev)
print("Next block------->")
prev= create_block(prev)
