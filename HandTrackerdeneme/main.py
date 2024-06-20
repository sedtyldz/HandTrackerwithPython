import cv2
import mediapipe as mp

benimelim = mp.solutions.hands
elcizgilerim = mp.solutions.drawing_utils


def paint(gelenfotoğraflar,x,y):
    cv2.rectangle(gelenfotograflar, (x, y), (x + 100, y + 100), (0, 0, 255), -1)


#0. index bilgisayarın kendi kamerası, 1.index bağlı cihazlar için kullanılır
mykamera = cv2.VideoCapture(0)

with benimelim.Hands(max_num_hands=1, min_detection_confidence=0.5) as el:
    while True:


        #mykamera.read fonksiyonu iki adet değer döndürür
        #1. okumanın başarılı olduğu bilgisi başarılı  değişkenine atılıyor
        #2. çekilen fotoğrafları gelenfotoğraflar değişkenine atılıyor
        basarili, gelenfotograflar = mykamera.read()

        if not basarili:
            break

        #hand tracker modeliniekleme
        gelenfotograflar = cv2.cvtColor(gelenfotograflar,cv2.COLOR_BGR2RGB)

        sonuclar = el.process(gelenfotograflar)


        #animasyonlari ciz

        gelenfotograflar = cv2.cvtColor(gelenfotograflar, cv2.COLOR_RGB2BGR)

        if sonuclar.multi_hand_landmarks:
            for hand_landmarks in sonuclar.multi_hand_landmarks:
                elcizgilerim.draw_landmarks(gelenfotograflar,hand_landmarks,connections=benimelim.HAND_CONNECTIONS)

                for i, landmark in enumerate(hand_landmarks.landmark):
                    boy,genislik,_= gelenfotograflar.shape
                    position_x = int(landmark.x * genislik)
                    position_y = int(landmark.y * boy)

                    if i==4:
                        paint(gelenfotograflar,position_x,position_y)

                        metin1 = "x degeri " + str(position_x)
                        metin2 = "y degeri " + str(position_y)

                        metinkordinatı =(900,50)
                        metinkordinatı1 = (900, 80)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        olcek = 1
                        renk = (255, 0, 0)
                        kalinlik = 2
                        cv2.putText(gelenfotograflar, metin1, metinkordinatı,font, olcek, renk, kalinlik)
                        cv2.putText(gelenfotograflar, metin2, metinkordinatı1, font, olcek, renk, kalinlik)

        #pencere oluşturup ekranda göstermek için kullanılır
        cv2.imshow('El izleme uygulaması', gelenfotograflar)
        # basılan karakteri key değişkenine atıyoruz ve görüntüyü ekranda 1 saniye bekletiyor
        key = cv2.waitKey(1)
        #karakter kontrolü
        if key == ord('q'):
            break

#kameraya işinin bittiğini söyleriz
mykamera.release()
cv2.destroyAllWindows()
