import numpy as np
from PIL import Image

# Load image
image = Image.open("image/birds.jpg")
image_array = np.array(image)

# Flip the image horizontal and vertical
flipped_image = np.flipud(np.fliplr(image_array))

# Add random noise
noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
noisy_image = np.clip(image_array + noise, 0, 255)

# Brighten red channel
brightened_image = image_array.copy()
brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)

# Apply mask in the center
masked_image = image_array.copy()
h, w, _ = image_array.shape
x_start, y_start = w // 2 - 50, h // 2 - 50
x_end, y_end = w // 2 + 50, h // 2 + 50
masked_image[y_start:y_end, x_start:x_end] = [0, 0, 0]

# Save the images
Image.fromarray(flipped_image).save("flipped_birds.jpg")
Image.fromarray(noisy_image).save("noisy_birds.jpg")
Image.fromarray(brightened_image).save("brightened_birds.jpg")
Image.fromarray(masked_image).save("masked_birds.jpg")
