# model_dispatcher.py

from sklearn import tree

models = {
	"decision_tree_gini" : tree.DecisionTreeClassifier(
		criterion = "gini"),
	"decision_tree_entropy" : tre.DecisionTreeClassifier(
		criterion="entropy"),

	"rf" : ensemble.RandomForestClassifier(),
}