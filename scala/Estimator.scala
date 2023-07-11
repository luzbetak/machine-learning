import org.apache.spark.ml.classification.LogisticRegression

// Define parameters upon creating an Estimator
val lr = new LogisticRegression().
  setMaxIter(5).
  setRegParam(0.01)
val training: DataFrame = ...
val model1 = lr.fit(training)

// Define parameters through fit
import org.apache.spark.ml.param.ParamMap
val customParams = ParamMap(
  lr.maxIter -> 10,
  lr.featuresCol -> "custom_features"
)
val model2 = lr.fit(training, customParams)
