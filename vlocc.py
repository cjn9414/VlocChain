"""
VlocChain
Authors: Owen Sullivan, Joe DeGrand, Carter Nesbitt
Filename: vlocc.py
"""

from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
import random
node = Flask(__name__)


## This file holds some functions that will be called
## throughout the code in the other files of this project.


## The "Vlocc" class is important for storing all the
## information that is used when making exchanges, or
## logging data.
class Vlocc:
    ## title --> the name of the file shared,
    ## assigned by the sender

    ## author --> person sending the data to receiver

    ## index --> the index of the instance of a Vlocc,
    ## stored within itself

    ## time --> timestamp of when the instance of the
    ## Vlocc was created

    ## attachment --> what the author sent; could be
    ## a string, picture, video etc.

    ## previous_hash --> the hash of the current Vlocc;
    ## named as previous for relevance in later code

	def __init__(self, title, author, index, time, attachment, previous_hash, data):
		self.title = title
		self.author = author
		self.index = index
		self.time = time
		self.attachment = attachment
		self.previous_hash = self.create_hash()

	def create_hash(self):
	## uses relevant info. of Vlocc to generate hash
		new_hash = hasher.sha256(str(self.index) + self.author)
		new_hash = new_hash.hexdigest
		return new_hash


def create_genesis():
    ## creates the first instance of a Vlocc
    ## parameters are trivial, and index is 0.

    first_stamp = date.datetime.now()
    starter = Vlocc("first", "author_name", 0, first_stamp, "attachment", "0", "this_would_be_a_dictionary")
    return starter

def create_identity():
    ## creates an address which will be assigned to
    ## a user upon function-call with a length of 10
    ## using numbers and letters
    identity = ""
    for strLength in range(0, 10):
        charType = random.randint(0, 3)
        if (charType == 0):
            ascii = random.randint(48, 57)
        elif (charType == 1):
            ascii = random.randint(65, 90)
        else:
            ascii = random.randint(97, 122)
        identity += chr(ascii)
    return identity



nodes = [] #All known nodes get added here
vlocchain = [] #the main chain, most updated
exchanges = [] #all the exchanges
miner_address = "yeet" #temporary
vlocchain.append(create_genesis())




@node.route('/new', methods=['POST'])
def exchange_vid():
        """
        The output for when an exchange occurs
        """
        curr_exchange = request.get_json()
        exchanges.append(curr_exchange)
        print("New Video Exchange!")    #Prints out the new exchange in the terminal
        print("TITLE:", (str(curr_exchange['title'].encode('utf-8', 'replace'))))
        print("AUTHOR:", (str(curr_exchange['author'].encode('utf-8', 'replace'))))
        print("FILE:", (str(curr_exchange['fname'].encode('utf-8', 'replace'))))
        return "Exchange complete!"

@node.route('/exchanges', methods=['GET'])
def get_previous():
        """
        Gets all past exchanges to show on webpage
        """
        curr_chain = vlocchain
        everything = ""
        for i in len(0, curr_chain):    #Puts all of the vloccs and their attributes in a string for printing on a webpage
                vlocc = str(curr_chain[i])
                vtitle = str(vlocc.title)
                vauthor = str(vlocc.author)
                vattachment = str(vlocc.attachment)
                all = "Title: " + vtitle +  "   Author: " + vauthor + "   Attachment: " + vattachment + "\n"
                everything += all
        return everything       #All of the vloccs in a string

def get_chains():
    """
    desc-Recieves and returns all known vlocchains
    returns- all vlocchains from all nodes
    """
    chains = []
    for element in nodes: #loop through all nodes
        chains.append(element)
    return chains

def consensus():
    """
    desc- updates the vlocchain to the newest
    """
    chains = get_chains()
    largest_chain = vlocchain

    for element in chains:
        if len(element) > len(largest_chain):
            largest_chain = element

    #sets the vlocchain
    vlocchain = largest_chain

@node.route('/mine', methods = ['GET'])
def mine():
    """
    des- How to recieve vloccs, then send to the miner
    """
    #grab the working variables
    previous_vlocc = vlocchain[-1]
    previous_proof = previous_vlocc['proof']
    #next find the proof of concept
    new_proof = proof(previous_proof)
    
    new_data = {'proof':new_proof,'exchanges':exchanges}
    #Get the variables for the new vlocc
    exchange.append({"from":"Vlocc","to":miner_address,"ammount")
    new_index = previous_vlocc.index + 1
    new_timestamp = date.datetime.now()
    previous_hash = previous_vlocc.hash
    exchanges[:] = []
    #Get the pictures input from miner
    (new_title,new_author,new_attachment) = new_info()
    #new vlocc creation
    new_vlocc = Vlocc(new_title,new_author,new_index,new_time,
        new_attachment,previous_hash,data)
    vlocchain.append(new_vlocc)
    #Send information to the client
    return(json.dumps({"title":new_title,"Author":new_Author,
        "Time":new_time_stamp,"Previous Hash":previous_hash}))

