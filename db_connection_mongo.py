#-------------------------------------------------------------------------
# AUTHOR: Erika Ledesma
# FILENAME: db_connection_mongo.py
# SPECIFICATION: Program that defines how actions in index_mongo.py menu are carried out
# FOR: CS 4250- Assignment #2
# TIME SPENT: 5PM-5:17PM, 9:45AM-10:45AM, 11:50AM-12:41PM, 1:40PM-7:13PM, 7:30PM-8:00PM
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
# --> add your Python code here
import re;
from pymongo import MongoClient

def connectDataBase():

    # Create a database connection object using pymongo
    # --> add your Python code here
    return MongoClient("mongodb://localhost:27017/")

def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary (document) to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    # --> add your Python code here

    document = {}

    #lowercase the original text
    lowercase = docText.lower()

    #remove all punctuation
    no_punct = re.sub(r'[^\w\s]', '', lowercase)
    docText = no_punct

    #separate words by space " "
    terms = docText.split()

    for word in terms:
        document[word] = terms.count(word)
    
    # Testing
    # print(document)

    # create a list of dictionaries (documents) with each entry including a term, its occurrences, and its num_chars. Ex: [{term, count, num_char}]
    # --> add your Python code here

    docs = []

    entry = {}

    #Producing a final document as a dictionary including all the required fields
    # --> add your Python code here

    #obtain keys from document
    keys = document.keys()

    for k in keys:
        entry["term"] = k
        entry["count"] = document.get(k)
        entry["num_char"] = len(k)
        docs.append(entry.copy())

    # Insert the document
    # --> add your Python code here

    final = {}

    final["_id"] = docId
    final["title"] = docTitle
    final["terms"] = docs

    col.insert_one(final)

def deleteDocument(col, docId):
    # Delete the document from the database
    # --> add your Python code here

    col.delete_one({"_id": docId})

def updateDocument(col, docId, docText, docTitle, docDate, docCat):
    # Delete the document
    # --> add your Python code here
    temp = docId
    deleteDocument(col, docId)

    # Create the document with the same id
    # --> add your Python code here

    createDocument(col, temp, docText, docTitle, docDate, docCat)

def getIndex(col):
    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3', ...}
    # We are simulating an inverted index here in memory.
    # --> add your Python code here

    pipeline = [
        {"$unwind": "$terms"},
        {"$group": {"_id": "$terms.term", "title": "$title"}, "count": {"$sum": "$terms.count"}},
        {"$group": {"_id": "$_id.term", }}
    ]