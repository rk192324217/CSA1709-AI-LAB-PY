import math
from collections import Counter

class DecisionNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature    # Index of feature to split on
        self.threshold = threshold  # Threshold value
        self.left = left          # Left subtree
        self.right = right        # Right subtree
        self.value = value        # Value if leaf node

class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.root = None
    
    def fit(self, X, y):
        self.root = self._build_tree(X, y, depth=0)
    
    def _build_tree(self, X, y, depth):
        n_samples, n_features = X.shape
        n_classes = len(set(y))
        
        # Stopping criteria
        if (depth >= self.max_depth or n_classes == 1 or n_samples < 2):
            leaf_value = self._most_common_label(y)
            return DecisionNode(value=leaf_value)
        
        # Find best split
        best_feature, best_threshold = self._best_split(X, y, n_features)
        
        # Split data
        left_idxs = X[:, best_feature] < best_threshold
        right_idxs = ~left_idxs
        
        # Recursively build left and right subtrees
        left = self._build_tree(X[left_idxs], y[left_idxs], depth+1)
        right = self._build_tree(X[right_idxs], y[right_idxs], depth+1)
        
        return DecisionNode(best_feature, best_threshold, left, right)
    
    def _best_split(self, X, y, n_features):
        best_gain = -1
        best_feature, best_threshold = None, None
        
        for feature in range(n_features):
            thresholds = set(X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(X, y, feature, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        return best_feature, best_threshold
    
    def _information_gain(self, X, y, feature, threshold):
        # Parent entropy
        parent_entropy = self._entropy(y)
        
        # Split data
        left_idxs = X[:, feature] < threshold
        right_idxs = ~left_idxs
        
        if len(y[left_idxs]) == 0 or len(y[right_idxs]) == 0:
            return 0
        
        # Weighted child entropy
        n = len(y)
        n_l, n_r = len(y[left_idxs]), len(y[right_idxs])
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l/n) * e_l + (n_r/n) * e_r
        
        # Information gain
        return parent_entropy - child_entropy
    
    def _entropy(self, y):
        counts = Counter(y)
        probs = [count/len(y) for count in counts.values()]
        return -sum(p * math.log(p) for p in probs if p > 0)
    
    def _most_common_label(self, y):
        return Counter(y).most_common(1)[0][0]
    
    def predict(self, X):
        return [self._traverse_tree(x, self.root) for x in X]
    
    def _traverse_tree(self, x, node):
        if node.value is not None:
            return node.value
        
        if x[node.feature] < node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

# Example usage
if __name__ == "__main__":
    import numpy as np
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train and predict
    clf = DecisionTree(max_depth=3)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    
    # Calculate accuracy
    accuracy = np.sum(predictions == y_test) / len(y_test)
    print(f"Decision Tree Accuracy: {accuracy:.2f}")