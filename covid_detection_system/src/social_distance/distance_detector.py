import cv2
import numpy as np

class DistanceDetector:
    def __init__(self):
        # 初始化 YOLOv5 模型
        self.net = cv2.dnn.readNet("yolov5s.onnx")
        self.safe_distance = 100  # 像素单位的安全距离

    def detect(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
        self.net.setInput(blob)
        output = self.net.forward()

        people = []
        for detection in output[0]:
            confidence = detection[4]
            if confidence > 0.5 and detection[5] == 0:  # 0 是人类类别
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                people.append((center_x, center_y))

        for i, person1 in enumerate(people):
            for person2 in people[i+1:]:
                distance = np.sqrt((person1[0] - person2[0])**2 + (person1[1] - person2[1])**2)
                if distance < self.safe_distance:
                    cv2.line(frame, person1, person2, (0, 0, 255), 2)
                else:
                    cv2.line(frame, person1, person2, (0, 255, 0), 2)

        return frame