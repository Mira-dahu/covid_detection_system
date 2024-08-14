import cv2
from social_distance.distance_detector import DistanceDetector
from mask_detection.mask_detector import MaskDetector

def main():
    cap = cv2.VideoCapture(0)  # 使用默认摄像头
    distance_detector = DistanceDetector()
    mask_detector = MaskDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 社交距离检测
        frame = distance_detector.detect(frame)

        # 口罩佩戴检测
        frame = mask_detector.detect(frame)

        cv2.imshow('COVID-19 Detection System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()