import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":

	# training_data is in a csv file is called train.csv

	df = pd.read_csv("/Users/thrilok/Documents/project/input/mnist_train.csv")

	#we create a new column called kfold and fill it with -1
	df["kfold"] =-1

	# the next step is to randomize the rows of the data
	df = df.sample(frac=1).reset_index(drop = True)

	# initialize the kfold class from model_selection module
	kf = model_selection.KFold(n_splits=5)

	# fill the new kfold column

	for fold, (trn_, val_) in enumerate(kf.split(X=df)):
		df.loc[val_, 'kfold'] = fold


	# save the new csv with kfold column
	df.to_csv("/Users/thrilok/Documents/project/input/mnist_train_folds.csv",index=False)