import cv2

def draw_box(frame, box, label, color):
    (startX, startY, endX, endY) = box
    cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
    cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
    return frame