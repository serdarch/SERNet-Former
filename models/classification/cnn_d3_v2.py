# Python code for CNN_D3_v2 architecture
# Serdar Erisen, 2024
import torch
import torch.nn as nn
import torch.nn.functional as F
 
class CNN_D3_v2(nn.Module):
     def __init__(self):
        super(CNN_D3_v2, self).__init__()
        self.conv = nn.Conv2d(1, 4, kernel_size=1, padding='same')
        self.batchnorm = nn.BatchNorm2d(4)
        self.relu = nn.ReLU()
        self.gmpool = nn.AdaptiveMaxPool2d((1, 1))
         
        self.conv_1 = nn.Conv2d(4, 8, kernel_size=1, padding='same')
        self.conv_2 = nn.Conv2d(8, 8, kernel_size=1, padding='same')
        self.batchnorm_1 = nn.BatchNorm2d(8)
        self.relu_1 = nn.ReLU()
        self.gmpool_1 = nn.AdaptiveMaxPool2d((1, 1))
         
        self.conv_3 = nn.Conv2d(8, 16, kernel_size=1, padding='same')
        self.conv_4 = nn.Conv2d(16, 16, kernel_size=1, padding='same')
        self.batchnorm_2 = nn.BatchNorm2d(16)
         
        self.conv_5 = nn.Conv2d(16, 32, kernel_size=1, padding='same')
        self.conv_6 = nn.Conv2d(32, 32, kernel_size=1, padding='same')
        self.batchnorm_3 = nn.BatchNorm2d(32)
        self.relu_2 = nn.ReLU()
         
        self.fc = nn.Linear(32, 4)
        self.softmax = nn.Softmax(dim=1)
 
     def forward(self, x):
        x = self.conv(x)
        x = self.batchnorm(x)
        x = self.relu(x)
        x = self.gmpool(x)
         
        x = self.conv_1(x)
        x = self.conv_2(x)
        x = self.batchnorm_1(x)
        x = self.relu_1(x)
        x = self.gmpool_1(x)
        
        x = self.conv_3(x)
        x = self.conv_4(x)
        x = self.batchnorm_2(x)
        
        x = self.conv_5(x)
        x = self.conv_6(x)
        x = self.batchnorm_3(x)
        x = self.relu_2(x)
        
        x = torch.flatten(x, 1)
        
        x = self.fc(x)
        x = self.softmax(x)
        
        return x

# Example usage:
# model = CNN_D3_v2()
# # Print model architecture
# print(model)


