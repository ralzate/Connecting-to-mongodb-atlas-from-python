from pymongo import MongoClient

# MongoDB Atlas credentials
username = ""
password = ""
cluster_name = "" 

# Construct the connection string
connection_string = f"mongodb+srv://{username}:{password}@{cluster_name}.ehmknym.mongodb.net/?retryWrites=true&w=majority&appName={cluster_name}"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)

try:
    # Access a specific database
    database = client.get_database('sample_mflix')

    # Access a specific collection (users collection in this case)
    collection = database['users']

    # Find all documents in the collection
    documents = collection.find()

    # Print documents in the collection
    print("\nDocuments in the 'users' collection:")
    for doc in documents:
        print(doc)

except Exception as e:
    print(f"Error connecting to MongoDB Atlas or accessing collection: {e}")

finally:
    # Close the MongoDB connection
    client.close()
    