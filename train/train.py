import numpy as np
import deeplake
import matplotlib.pyplot as plt
import cv2

# Dataset(path='hub://activeloop/lsp-train', read_only=True, tensors=['images', 'keypoints', 'images_visualized'])
ds_train = deeplake.load("hub://activeloop/lsp-train")
ds_test = deeplake.load("hub://activeloop/lsp-test")

img = ds_train['images'][53]

print(img)
print(img.shape)

img = img.numpy()

print(type(img))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()