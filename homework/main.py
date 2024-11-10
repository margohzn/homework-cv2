import cv2 

ghost_image = cv2.imread("ghost.png")
greyscale_image = cv2.imread("ghost.png", cv2.IMREAD_GRAYSCALE) 
unchanged_image = cv2.imread("ghost.png", cv2.IMREAD_UNCHANGED)


blue, green, red, = cv2.split(ghost_image)

cv2.imshow("Ghost image original", ghost_image)
cv2.waitKey(delay = 1000)

cv2.imshow("blue saturation", blue)
cv2.waitKey(delay = 1000)

cv2.imshow("green saturation", green)
cv2.waitKey(delay = 1000)

cv2.imshow("red saturation", red)
cv2.waitKey(delay = 1000)

cv2.imshow("Greyscale ghost", greyscale_image)
cv2.waitKey(delay = 1000)

cv2.imshow("Unchanged ghost", unchanged_image)
cv2.waitKey(delay = 1000)


cv2.waitKey(0)
cv2.destroyAllWindows()