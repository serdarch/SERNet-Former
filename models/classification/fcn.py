import torch
import torch.nn as nn

class YourModel(nn.Module):
    def __init__(self, hidden_size, num_classes):
        super(YourModel, self).__init__()
        self.fc1 = nn.Linear(28 * 28 * 1, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
        self.softmax = nn.Softmax(dim=1)  # Softmax across classes

    def forward(self, x):
        x = x.view(-1, 28 * 28 * 1)  # Flatten the input images
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# Example usage:
# model = YourModel(hidden_size=100, num_classes=numClasses)
