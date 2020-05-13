#### 安裝所需套件
`pip install -r requirements.txt`

#### 透過cv2套件來實作功能
- CascadeClassifier: 選擇分類器(haarcascade_car.xml)
- detectMultiScale: 偵測圖像中不同大小的物件，以矩形列表回傳
- rectangle: 繪製矩形
- VideoCapture: 擷取視頻
- imshow: 呈現視窗畫面
- waitKey: 等待輸入按鍵
- destroyAllWindows: 關閉所有視窗
