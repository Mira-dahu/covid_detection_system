import cv2
import numpy as np

class MaskDetector:
    def __init__(self):
        # 初始化口罩检测模型
        self.net = cv2.dnn.readNet("mask_rcnn_inception_resnet_v2_atrous_coco.pb")

    def detect(self, frame):
        blob = cv2.dnn.blobFromImage(frame, swapRB=True)
        self.net.setInput(blob)
        output = self.net.forward()

        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > 0.5:
                class_id = int(detection[1])
                box = detection[3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (startX, startY, endX, endY) = box.astype("int")

                if class_id == 1:  # 假设1表示佩戴口罩
                    color = (0, 255, 0)
                    label = "Mask"
                else:
                    color = (0, 0, 255)
                    label = "No Mask"

                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

        return frame