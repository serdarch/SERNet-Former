import torch
import torch.nn as nn

class YourModel(nn.Module):
    def __init__(self, num_features, hidden_size, num_classes):
        super(YourModel, self).__init__()
        self.lstm = nn.LSTM(num_features, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
        self.softmax = nn.Softmax(dim=1)  # Softmax across classes

    def forward(self, x):
        _, (h_n, _) = self.lstm(x)
        x = self.fc(h_n.squeeze(0))
        x = self.softmax(x)
        return x

# Example usage:
# model = YourModel(num_features=numFeatures, hidden_size=hiddenSize, num_classes=numClasses)
