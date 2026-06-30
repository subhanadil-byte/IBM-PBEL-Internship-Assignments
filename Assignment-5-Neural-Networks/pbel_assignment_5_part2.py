import math

# TOPIC 1: SIGMOID ACTIVATION FUNCTION & DERIVATIVE
def sigmoid(x):
    """Squashes input values strictly between 0 and 1."""
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    """Derivative of Sigmoid: used during backpropagation."""
    s = sigmoid(x)
    return s * (1 - s)


# TOPIC 2: TANH (HYPERBOLIC TANGENT) FUNCTION & DERIVATIVE
def tanh(x):
    """Squashes input values between -1 and +1 (Zero-centered)."""
    return math.tanh(x)

def tanh_derivative(x):
    """Derivative of Tanh: used during backpropagation."""
    t = math.tanh(x)
    return 1 - (t ** 2)


# TOPIC 3: RELU (RECTIFIED LINEAR UNIT) FUNCTION & DERIVATIVE
def relu(x):
    """Returns 0 for negative inputs, and the same value for positive inputs."""
    return max(0, x)

def relu_derivative(x):
    """Derivative of ReLU: 1 for positive numbers, 0 for negative numbers."""
    return 1 if x > 0 else 0


# TOPIC 4: SOFTMAX ACTIVATION FUNCTION
def softmax(scores):
    """Converts a list of raw scores into probabilities that sum up to 1.0."""
    exp_scores = [math.exp(s) for s in scores]
    total_sum = sum(exp_scores)
    return [e / total_sum for e in exp_scores]


# TOPIC 5: EXPERIMENTAL NETWORK LAYER FOR COMPARISON
class ActivationComparisonNetwork:
    def __init__(self, activation_mode):
        self.mode = activation_mode
        # Hardcoded baseline parameters for standardized evaluation
        self.W1 = [[0.15, 0.20], [0.25, 0.30]]
        self.b1 = [0.35, 0.35]
        self.W2 = [0.40, 0.45]
        self.b2 = 0.60

    def forward(self, X):
        self.X = X
        # Dynamically applying the selected hidden layer activation function
        if self.mode == "sigmoid":
            self.A1 = [sigmoid(X[0]*self.W1[0][0] + self.b1[0]), sigmoid(X[1]*self.W1[1][1] + self.b1[1])]
        elif self.mode == "tanh":
            self.A1 = [tanh(X[0]*self.W1[0][0] + self.b1[0]), tanh(X[1]*self.W1[1][1] + self.b1[1])]
        elif self.mode == "relu":
            self.A1 = [relu(X[0]*self.W1[0][0] + self.b1[0]), relu(X[1]*self.W1[1][1] + self.b1[1])]
            
        # Final output prediction layer
        self.Z2 = self.A1[0] * self.W2[0] + self.A1[1] * self.W2[1] + self.b2
        self.A2 = sigmoid(self.Z2)
        return self.A2

    def train_step(self, target, lr=0.2):
        # Calculate loss gradient at output layer
        error = self.A2 - target
        dZ2 = error * (self.A2 * (1 - self.A2))
        
        # Calculate gradients using the respective function's derivative
        if self.mode == "sigmoid":
            dZ1 = [dZ2 * self.W2[0] * sigmoid_derivative(self.A1[0]), dZ2 * self.W2[1] * sigmoid_derivative(self.A1[1])]
        elif self.mode == "tanh":
            dZ1 = [dZ2 * self.W2[0] * tanh_derivative(self.A1[0]), dZ2 * self.W2[1] * tanh_derivative(self.A1[1])]
        elif self.mode == "relu":
            dZ1 = [dZ2 * self.W2[0] * relu_derivative(self.A1[0]), dZ2 * self.W2[1] * relu_derivative(self.A1[1])]
            
        # Standard Gradient Descent updates
        self.W2[0] -= lr * dZ2 * self.A1[0]
        self.W2[1] -= lr * dZ2 * self.A1[1]
        self.b2    -= lr * dZ2


# TOPIC 6: RUNNING THE EXPERIMENT & VERIFYING OUTPUTS
if __name__ == "__main__":
    X_in = [1.0, 1.0]
    y_true = 1.0

    print("--- PART 2: Activation Function Mode Comparison ---\n")
    for mode in ["sigmoid", "tanh", "relu"]:
        model = ActivationComparisonNetwork(activation_mode=mode)
        init_err = abs(y_true - model.forward(X_in))
        
        # Train for 10 simple loops
        for epoch in range(10):
            model.forward(X_in)
            model.train_step(y_true)
            
        final_err = abs(y_true - model.forward(X_in))
        print(f"[{mode.upper()}] Start Error: {init_err:.5f} -> Final Error: {final_err:.5f}")

    print("\n--- Output Layer Softmax Logits Translation ---")
    logits = [1.0, 2.0, 3.0]
    probabilities = softmax(logits)
    print("Raw Input Logits:     ", logits)
    print("Softmax Probabilities:", probabilities)