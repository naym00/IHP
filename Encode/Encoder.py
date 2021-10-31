import cv2
import numpy as np

def encode(SavingPath, Starting_Index, Ghap, Add_a_Value, HiddenData):
    image = np.zeros((500, 500, 3), np.uint8)
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    LengthOfString = len(HiddenData)

    Counter = 1
    k = Start = SetValue = 0
    for i in range(0, 50, 1):
        for j in range(0, 50, 1):
            if Counter == Starting_Index:
                Start = 1
            if Start == 1:
                if SetValue % (Ghap + 1) == 0:
                    if k == LengthOfString:
                        k = -1
                        break
                    grayimage[i, j] = (ord(HiddenData[k]) + Add_a_Value) % 255
                    k = k + 1
                    SetValue = SetValue + 1
                else:
                    SetValue = SetValue + 1
            Counter = Counter + 1
        if k == -1:
            break
    cv2.imwrite(SavingPath, grayimage)
    return LengthOfString