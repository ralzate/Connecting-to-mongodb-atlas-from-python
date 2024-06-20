# README - Connecting to MongoDB Atlas

This document outlines the necessary steps to set up and connect your project to MongoDB Atlas, a cloud-based database service.

## Step 1: Create an account on MongoDB Atlas

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create an account or log in if you already have one.
3. Once logged in, follow these steps to create a cluster:

## Step 2: Create a cluster

1. In the MongoDB Atlas dashboard, click on "Build a Cluster" or similar to start creating a new cluster.
2. Choose your preferred cloud provider (e.g., AWS, Azure, Google Cloud).
3. Configure your cluster options according to your needs (e.g., region, cluster type, instance size).
4. Follow the instructions to complete cluster creation.

## Step 3: Set up database access

1. In the MongoDB Atlas dashboard, go to "Database Access" in the left sidebar.
2. Click on "Add New Database User" to create a new database user.
3. Enter a secure username and password. Remember these credentials as you will need them to connect from your application.
4. Assign appropriate privileges to this user as needed (e.g., readWriteAnyDatabase for testing or custom roles for production).

## Step 4: Configure whitelist IP (if necessary)

1. In the MongoDB Atlas dashboard, go to "Network Access" in the left sidebar.
2. Click on "Add IP Address" and then "Allow Access from Anywhere" for quick testing.
3. For production environments, configure a specific IP from which connections will be made.

## Step 5: Get the connection string

1. In the MongoDB Atlas dashboard, click on "Clusters" in the left sidebar.
2. Click on "Connect" next to the cluster you created.
3. Select "Connect Your Application" to get the connection string.
4. Choose Python as your programming language and copy the provided connection string.

## Step 6: Configure credentials in your application

1. Open your configuration file or Python script.
2. Use the copied connection string to connect your application to MongoDB Atlas.
   
   ```python
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
