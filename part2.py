from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from data import load_data
from sfs import sfs, score

#=================================data======================================
path = "./flare.csv"
data , labels = load_data(path)
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.25)
#=================================Q7==========================================
KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(X=x_train, y=y_train)
train_acc = KNN.score(X=x_train, y=y_train)
test_acc = KNN.score(X=x_test, y=y_test)
print("\nKNN")
print("{}".format(test_acc))

features = sfs(x=x_train, y=y_train, k=8, clf=KNN, score=score)
filtered_data = [[row[ind] for ind in features] for row in x_train]
KNN.fit(X=filtered_data, y=y_train)
train_acc_sfs = KNN.score(X=filtered_data, y=y_train)
test_acc_sfs = KNN.score(X=[[row[ind] for ind in features] for row in x_test], y=y_test)

print("\nKNN + SFS")
print("{}".format(test_acc_sfs))
#=================================Q8==========================================
dt = DecisionTreeClassifier(criterion="entropy")
k_fold = 4
dt.fit(X=x_train, y=y_train)
print("\nDecision Tree")
print("{}".format(dt.score(X=x_test,y=y_test)))

dt_p = DecisionTreeClassifier(criterion="entropy",min_samples_leaf=20)
dt_p.fit(X=x_train, y=y_train)
print("\nDecision Tree with Pruning")
print("{}".format(dt_p.score(X=x_test,y=y_test)))