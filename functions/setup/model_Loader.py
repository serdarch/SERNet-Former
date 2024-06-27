import torch
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim

# Load pretrained model
model = models.__dict__[config['model']['name']](pretrained=True)

# Replace the classifier for the number of classes in your dataset
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, config['model']['num_classes'])

device = torch.device('cpu') # 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)

# Define optimizer and criterion
optimizer_name = config['training']['optimizer']
if optimizer_name == 'adam':
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])
elif optimizer_name == 'sgd':
    optimizer = optim.SGD(model.parameters(), lr=config['training']['learning_rate'], momentum=config['training']['momentum'])

criterion = nn.CrossEntropyLoss()
