from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession


"""
First create a SparkSession which is the entry point to any functionality in Spark. 
We then define the sparse vector using PySpark's Vectors class. 
The DataFrame is created using the SparkSession's createDataFrame method, 
which takes a list of tuples as input. Each tuple correspon
"""

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Define the sparse vector
features = Vectors.sparse(10, {2: 0.2, 4: 0.4})

# Create a DataFrame
data = spark.createDataFrame([(float(i), features) for i in range(5)], ["label", "features"])

# Show the DataFrame
data.show(truncate=False)


