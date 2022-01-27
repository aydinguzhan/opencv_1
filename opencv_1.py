import cv2 # kütüphanemizi dahil ediyoruz

kamera = cv2.VideoCapture(0) # kameramızdan görüntü almak üzere ( dahili = 0), kamera değişkenine atama yapıyoruz.


while (True): # görüntü karelerimiz olduğu için sonsuz bir loop oluşturuyoruz
    ret, videoGoruntu = kamera.read()
    cv2.imshow("Bilgisayar Kamerasi", videoGoruntu)
    if cv2.waitKey(50) & 0xFF == ord('x'): # döngüyü kırmak için x tuşuna basıldığı takdirde döngüyü kırıyoruz
        break

kamera.release()
cv2.destroyAllWindows() # kamera ve frame kapatıyoruz.