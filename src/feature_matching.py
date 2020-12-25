import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("res/set-1/sift-scene.jpg", None)
img2 = cv2.imread("res/set-1/object-1.jpg", None)

# ORB Detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute Force Matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance)

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# cv2.imshow("Img1", img1)
# cv2.imshow("Img2", img2)
cv2.imshow("Matching result", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()