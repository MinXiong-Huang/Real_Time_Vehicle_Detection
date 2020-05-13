from cv2 import cv2

cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml') #分類器

#偵測車
def Detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4) #取得道路上車輛的坐標

    #繪製矩形
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0,255,0), thickness=2)
    return frame

def Detect_cars_frame():
    Video_Path=r'.\Video\cars.mp4' #影片路徑
    Car_Video = cv2.VideoCapture(Video_Path) 

    while Car_Video.isOpened():
        ret, frame = Car_Video.read()
        controlkey = cv2.waitKey(1)

        if ret:        
            Cars_frame = Detect_cars(frame)
            cv2.imshow('Detect Cars', Cars_frame)
        else:
            break

        #輸入q退出視窗
        if controlkey == ord('q'):
            break
    else:
        print('請確認影片路徑是否有誤!')

    Car_Video.release() #釋放資源
    cv2.destroyAllWindows() #關閉所有視窗


if __name__ == '__main__':
    Detect_cars_frame()
    