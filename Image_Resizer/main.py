import cv2

src_image = cv2.imread("Image_Resizer/krishna_photo.jpeg",cv2.IMREAD_UNCHANGED)

# cv2.imshow("title",src_image)

scale_percent = 50

new_width = int(src_image.shape[1]*scale_percent/100)

new_height = int(src_image.shape[0]*scale_percent/100)

resize = (new_width,new_height)

output_image = cv2.resize(src_image,resize)

cv2.imwrite("Image_Resizer/newImage.png",output_image)
cv2.waitKey(0)