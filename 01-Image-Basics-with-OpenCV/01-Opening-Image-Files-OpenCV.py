import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

# Resize the image
resized_img = cv2.resize(img, (800, 600))

while True:
    cv2.imshow('Puppy', resized_img)
    cv2.resizeWindow('Puppy', 800, 600)

    # IF we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()