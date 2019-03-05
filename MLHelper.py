from sklearn import linear_model, svm
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
import csv

class MLModule:
	def loadData(self, csvFile):
		data = []
		with open(filename, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for row in reader:
				data.append(row)
		return data
		
	def regression(self, data, target):
		model = None
		##########################################
		# 1. Set model to linear regression model
		##########################################
		# Hint: use linear_model

		##########################################
		# 2. Split train and test datasets 70/30
		##########################################
		# Hint: use train_test_split. 


		##########################################
		# 3. Fit model to training data
		##########################################


		##########################################
		# 4. Predict on test data
		##########################################


		##########################################
		# 5. Evaluate with MAE and MSE
		##########################################
		MAE = 0
		MSE = 0




		print("Mean absolute error: " + str(MAE))
		print("Mean squared error: " + str(MSE))
		return model

	def classification(self, data, target):
		model = None
		##########################################
		# 1. Set model to svm classifier
		##########################################


		##########################################
		# 2. Fit model to training data
		##########################################


		##########################################
		# 3. Cross Validation
		##########################################
		# Hint: Use cross_val_score
		CVS = 0




		print("Cross validation score: " + str(CVS))
		return model