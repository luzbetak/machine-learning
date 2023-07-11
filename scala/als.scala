// Alternating Least Squares (ALS) Matrix Factorization for Recommender Systems
// Based on JavaALSExample from the official Spark examples
// https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/ml/JavaALSExample.java

// 1. Save the code to als.scala
// 2. Run `spark-shell -i als.scala`

import spark.implicits._

import org.apache.spark.ml.recommendation.ALS
val als = new ALS().
  setMaxIter(5).
  setRegParam(0.01).
  setUserCol("userId").
  setItemCol("movieId").
  setRatingCol("rating")

import org.apache.spark.ml.recommendation.ALS.Rating
// FIXME Use a much richer dataset, i.e. Spark's data/mllib/als/sample_movielens_ratings.txt
// FIXME Load it using spark.read
val ratings = Seq(
  Rating(0, 2, 3),
  Rating(0, 3, 1),
  Rating(0, 5, 2),
  Rating(1, 2, 2)).toDF("userId", "movieId", "rating")
val Array(training, testing) = ratings.randomSplit(Array(0.8, 0.2))

// Make sure that the RDDs have at least one record
assert(training.count > 0)
assert(testing.count > 0)

import org.apache.spark.ml.recommendation.ALSModel
val model = als.fit(training)

// drop NaNs
model.setColdStartStrategy("drop")
val predictions = model.transform(testing)

import org.apache.spark.ml.evaluation.RegressionEvaluator
val evaluator = new RegressionEvaluator().
  setMetricName("rmse").  // root mean squared error
  setLabelCol("rating").
  setPredictionCol("prediction")
val rmse = evaluator.evaluate(predictions)
println(s"Root-mean-square error = $rmse")

// Model is ready for recommendations

// Generate top 10 movie recommendations for each user
val userRecs = model.recommendForAllUsers(10)
userRecs.show(truncate = false)

// Generate top 10 user recommendations for each movie
val movieRecs = model.recommendForAllItems(10)
movieRecs.show(truncate = false)

// Generate top 10 movie recommendations for a specified set of users
// Use a trick to make sure we work with the known users from the input
val users = ratings.select(als.getUserCol).distinct.limit(3)
val userSubsetRecs = model.recommendForUserSubset(users, 10)
userSubsetRecs.show(truncate = false)

// Generate top 10 user recommendations for a specified set of movies
val movies = ratings.select(als.getItemCol).distinct.limit(3)
val movieSubSetRecs = model.recommendForItemSubset(movies, 10)
movieSubSetRecs.show(truncate = false)

System.exit(0)
