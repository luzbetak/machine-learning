import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint

val data = (0.0 to 9.0 by 1)                      // create a collection of Doubles
  .map(n => (n, n))                               // make it pairs
  .map { case (label, features) =>
    LabeledPoint(label, Vectors.dense(features)) } // create labeled points of dense vectors
  .toDF                                           // make it a DataFrame

//data.show
