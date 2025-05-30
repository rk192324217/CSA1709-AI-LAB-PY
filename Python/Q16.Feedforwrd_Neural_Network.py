import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with He initialization
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2./input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2./hidden_size)
        self.b2 = np.zeros((1, output_size))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.hidden = self.sigmoid(np.dot(X, self.W1) + self.b1)
        self.output = self.sigmoid(np.dot(self.hidden, self.W2) + self.b2)
        return self.output
    
    def backward(self, X, y, learning_rate, lambda_param=0.01):
        m = X.shape[0]
        
        # Output layer error
        output_error = y - self.output
        output_delta = output_error * self.sigmoid_derivative(self.output)
        
        # Hidden layer error
        hidden_error = output_delta.dot(self.W2.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden)
        
        # Update weights and biases with L2 regularization
        self.W2 += (self.hidden.T.dot(output_delta) - lambda_param * self.W2) * learning_rate / m
        self.b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate / m
        self.W1 += (X.T.dot(hidden_delta) - lambda_param * self.W1) * learning_rate / m
        self.b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate / m
    
    def train(self, X, y, epochs=1000, learning_rate=0.1, batch_size=32, tolerance=1e-4, decay_rate=0.001):
        losses = []
        for epoch in range(epochs):
            # Learning rate decay
            current_lr = learning_rate * (1. / (1. + decay_rate * epoch))
            
            # Mini-batch training
            for i in range(0, X.shape[0], batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                output = self.forward(X_batch)
                self.backward(X_batch, y_batch, current_lr)
            
            # Calculate and store loss
            output = self.forward(X)
            loss = np.mean(np.square(y - output))
            losses.append(loss)
            
            # Early stopping
            if loss < tolerance:
                print(f"Early stopping at epoch {epoch} with loss {loss:.4f}")
                break
            
            # Print progress
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
        
        return losses
    
    def predict(self, X):
        return np.round(self.forward(X))
    
    def evaluate(self, X, y):
        predictions = self.predict(X)
        return accuracy_score(y, predictions)

# Example usage
if __name__ == "__main__":
    # Generate synthetic data
    X, y = make_classification(
        n_samples=1000, 
        n_features=10, 
        n_classes=2, 
        n_clusters_per_class=1,
        random_state=42
    )
    y = y.reshape(-1, 1)  # Reshape for neural network
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.2, 
        random_state=42
    )
    
    # Initialize and train network
    print("Initializing neural network...")
    nn = NeuralNetwork(input_size=10, hidden_size=5, output_size=1)
    
    print("Training network...")
    losses = nn.train(
        X_train, 
        y_train, 
        epochs=2000, 
        learning_rate=0.1,
        batch_size=64,
        tolerance=1e-4
    )
    
    # Evaluate
    train_acc = nn.evaluate(X_train, y_train)
    test_acc = nn.evaluate(X_test, y_test)
    
    print(f"\nTraining Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")