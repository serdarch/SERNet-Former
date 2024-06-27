import torch
import torchvision.models as models

# Define your model architecture (must match the one saved in the checkpoint)
model = selectOneCheckpoint()

# Load the state_dict from a checkpoint file
checkpoint_path = 'path_to_your_checkpoint.pth'
checkpoint = torch.load(checkpoint_path)
net = model.load_state_dict(checkpoint['model_state_dict'])

# If you also saved optimizer state_dict during training, you can load it as well
# optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

# Set the model to evaluation mode
model.eval()

# Example usage:
# Use the model for inference or further training
