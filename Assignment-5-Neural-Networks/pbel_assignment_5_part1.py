import math

# --- Activation Function and Derivative ---
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# --- Neural Network Class ---
class NeuralNetwork2Layer:
    def __init__(self):
        # 2 Input neurons -> 2 Hidden neurons -> 1 Output neuron
        self.W1 = [[0.15, 0.20], [0.25, 0.30]]  # Hidden Layer Weights
        self.b1 = [0.35, 0.35]                  # Hidden Layer Biases
        self.W2 = [0.40, 0.45]                  # Output Layer Weights
        self.b2 = 0.60                          # Output Layer Bias

    def forward(self, X):
        self.X = X
        # Hidden layer calculation
        self.Z1 = [
            X[0] * self.W1[0][0] + X[1] * self.W1[1][0] + self.b1[0],
            X[0] * self.W1[0][1] + X[1] * self.W1[1][1] + self.b1[1]
        ]
        self.A1 = [sigmoid(self.Z1[0]), sigmoid(self.Z1[1])]
        
        # Output layer calculation
        self.Z2 = self.A1[0] * self.W2[0] + self.A1[1] * self.W2[1] + self.b2
        self.A2 = sigmoid(self.Z2)
        return self.A2

    def backward(self, target, learning_rate):
        # 1. Output Layer Error
        error_output = self.A2 - target
        dZ2 = error_output * sigmoid_derivative(self.Z2)
        
        dW2 = [dZ2 * self.A1[0], dZ2 * self.A1[1]]
        db2 = dZ2
        
        # 2. Backpropagate to Hidden Layer
        dZ1 = [
            (dZ2 * self.W2[0]) * sigmoid_derivative(self.Z1[0]),
            (dZ2 * self.W2[1]) * sigmoid_derivative(self.Z1[1])
        ]
        
        dW1 = [
            [dZ1[0] * self.X[0], dZ1[1] * self.X[0]],
            [dZ1[0] * self.X[1], dZ1[1] * self.X[1]]
        ]
        db1 = dZ1

        # 3. Parameter updates via Gradient Descent
        self.W2[0] -= learning_rate * dW2[0]
        self.W2[1] -= learning_rate * dW2[1]
        self.b2    -= learning_rate * db2
        
        self.W1[0][0] -= learning_rate * dW1[0][0]
        self.W1[0][1] -= learning_rate * dW1[0][1]
        self.W1[1][0] -= learning_rate * dW1[1][0]
        self.W1[1][1] -= learning_rate * dW1[1][1]
        self.b1[0]    -= learning_rate * db1[0]
        self.b1[1]    -= learning_rate * db1[1]

# --- Run & Verification ---
net = NeuralNetwork2Layer()
X_data = [1.0, 0.0]
y_target = 1.0

print("--- PART 1: 2-Layer Network Training Progress ---")
initial_pred = net.forward(X_data)
print(f"Initial Prediction Error: {abs(y_target - initial_pred):.5f}")

for epoch in range(20):
    net.forward(X_data)
    net.backward(y_target, learning_rate=0.5)
    
final_pred = net.forward(X_data)
print(f"Final Prediction Error:   {abs(y_target - final_pred):.5f}")