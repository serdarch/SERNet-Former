import torch
import torchvision.models.segmentation as segmentation
from torchvision import transforms
from PIL import Image

# Download a pretrained DeepLabV3 model
model = segmentation.deeplabv3_resnet50(pretrained=True)
model.eval()

# Load and preprocess an image (you should adapt the preprocessing steps as per your dataset)
input_image = Image.open('your_image.jpg')
preprocess = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image).unsqueeze(0)

# Make a forward pass
with torch.no_grad():
    output = model(input_tensor)['out'][0]

# Optionally, post-process the output (e.g., apply softmax, thresholding, etc.)
# For segmentation, you typically visualize or use the output directly

# Example of visualizing the segmentation mask
import matplotlib.pyplot as plt
plt.imshow(output.argmax(0))
plt.show()
