import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# Define your batch preprocessing and transformation pipeline
def batch_preprocess_transform(images):
    # images: list of PIL images or a batch tensor of shape (batch_size, channels, height, width)
    
    # Define your transformations
    preprocess = transforms.Compose([
        transforms.Resize((720, 960)),          # Resize to a fixed size
        transforms.ToTensor(),                  # Convert to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize
    ])
    
    # If images are in a list of PIL images, convert them to tensor and apply transformations
    if isinstance(images, list):
        tensor_batch = [preprocess(image) for image in images]
        tensor_batch = torch.stack(tensor_batch, dim=0)  # Stack into a batch tensor
    elif isinstance(images, torch.Tensor):
        # If images are already a batch tensor, apply transformations directly
        tensor_batch = images
        # Ensure images are float and within [0, 1] range for proper normalization
        if tensor_batch.max() > 1:
            tensor_batch = tensor_batch.float() / 255.0
        tensor_batch = preprocess(tensor_batch)
    else:
        raise TypeError('Unsupported input type. Expected list of PIL images or batch tensor.')

    return tensor_batch

# Example usage:
# Assuming you have a list of PIL images or a batch tensor of images
# Replace this with your actual batch of images or modify as needed

# Example 1: List of PIL images
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
images = [Image.open(image_path) for image_path in image_paths]

# Example 2: Batch tensor (batch_size, channels, height, width)
# images = torch.randn(3, 3, 720, 960)  # Example batch tensor

# Apply batch preprocessing and transformation
batch_tensor = batch_preprocess_transform(images)

# Check the shape of the output batch tensor
print(f"Shape of batch tensor: {batch_tensor.shape}")
