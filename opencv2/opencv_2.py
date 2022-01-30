import cv2


pic = cv2.imread("590300.jpg") # resime ulaştık ve değişkene attık

cv2.imshow("opencv coding", pic)

cv2.waitKey(0) #kapanması için klavye bekliyor
cv2.destroyAllWindows()