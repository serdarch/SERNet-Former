from torchvision.io.image import read_image
from torchvision.models.segmentation import deeplabv3_resnet101, DeepLabv3_ResNet101_Weights
from torchvision.transforms.functional import to_pil_image

img = read_image("_Your_image_.jpg")

# Step 1: Initialize model with the best available weights
weights = DeepLabv3_ResNet101_Weights.DEFAULT
model = deeplabv3_resnet101(weights=weights)
model.eval()

# Step 2: Initialize the inference transforms
preprocess = weights.transforms()
 
# Step 3: Apply inference preprocessing transforms
batch = preprocess(img).unsqueeze(0)
 
# Step 4: Use the model and visualize the prediction
prediction = model(batch)["out"]
normalized_masks = prediction.softmax(dim=1)
class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}
mask = normalized_masks[0, class_to_idx["dog"]]
