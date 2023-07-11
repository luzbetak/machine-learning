# Import required libraries
from pyspark.sql import SparkSession
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import re

# Create SparkSession
spark = SparkSession.builder.appName("NaiveBayes").getOrCreate()

# Load Data
raw_trips = spark.sparkContext.textFile("2014-Q1-cabi-trip-history-data.csv")

# Function to convert duration
def convert_dur(dur):
    dur_regex = re.compile(r"(\d+)h\s(\d+)m\s(\d+)s")
    matches = dur_regex.match(dur)
    hour, minute, second = matches.groups()
    return int(hour) * 3600 + int(minute) * 60 + int(second)

# Convert RDD to DataFrame
from pyspark.sql import Row
bike_trips = raw_trips.map(lambda line: line.split(","))\
    .filter(lambda r: r[0] != "Duration")\
    .map(lambda r: Row(id=r[5], dur=convert_dur(r[0]), s0=r[2], s1=r[4], reg=r[6]))
bike_trips.cache()

# Create DataFrame
bike_df = spark.createDataFrame(bike_trips)

# Register the DataFrame as a SQL temporary view
bike_df.createOrReplaceTempView("bikeshare")

# SQL query
query = """
  SELECT COUNT(*) AS num, s0, s1
  FROM bikeshare
  GROUP BY s0, s1
  ORDER BY num DESC LIMIT 10
"""
result = spark.sql(query)
result.show()

# Compute NaiveBayes model
# This part depends on how you want to handle 'train_set' and 'test_set' in your Python script.
# We assume they are already defined and preprocessed according to the format that Spark ML's NaiveBayes requires.
# You also need to define the 'label' and 'features' columns in your DataFrame.

# Model Training
nb = NaiveBayes(smoothing=1.0, modelType="multinomial")
model = nb.fit(train_set)

# Model Evaluation
predictions = model.transform(test_set)
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction",
                                              metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test set accuracy = " + str(accuracy))

# Exit
spark.stop()

