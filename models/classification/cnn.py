import torch
import torch.nn as nn

class YourModel(nn.Module):
    def __init__(self, num_classes):
        super(YourModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=20, kernel_size=5)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc = nn.Linear(20 * 12 * 12, num_classes)  # Assuming input image size is 28x28

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 20 * 12 * 12)  # Flatten the tensor for fully connected layer
        x = self.fc(x)
        return x

# Example usage:
# model = YourModel(num_classes=numClasses)
