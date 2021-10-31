import cv2
import numpy as np


def decode(Starting_Index, Ghap, Add_a_Value, LengthOfString, ImagePath):
    image = cv2.imread(ImagePath)
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    Row, Column = grayimage.shape
    Counter = 1
    k = Start = SetValue = 0
    DecodedString = ""
    for i in range(0, Row, 1):
        for j in range(0, Column, 1):
            if Counter == Starting_Index:
                Start = 1
            if Start == 1:
                if SetValue % (Ghap + 1) == 0:
                    if k == LengthOfString:
                        k = -1
                        break
                    Value = grayimage[i, j]
                    while Value < Add_a_Value:
                        Value = Value + 255
                    DecodedString = DecodedString + chr(Value - Add_a_Value)
                    k = k + 1
                    SetValue = SetValue + 1
                else:
                    SetValue = SetValue + 1

            Counter = Counter + 1
        if k == -1:
            break
    return DecodedString