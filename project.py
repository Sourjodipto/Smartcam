import cv2
from fpdf import FPDF
import os
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



url = "http://192.168.1.104:8080/video"
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
while ret:
    ret, frame = cap.read()
    if f1 == 0:
        print("press 's' to scan the document")
        print("press 'q' to quit")
        print("press 'm' to turn on colour detection mode")
        print("press 'a' to turn on object detection and shape identification mode")
        f1 = f1 + 1


    def empty(a):
        pass


    cv2.imshow("camera feed", frame)
    k = cv2.waitKey(1)
    if k == ord('m'):
        cv2.destroyWindow("camera feed")
        cv2.namedWindow("HSV")
        cv2.resizeWindow("HSV", 640, 480)
        cv2.createTrackbar("Min Hue", "HSV", 0, 179, empty)
        cv2.createTrackbar("Max Hue", "HSV", 179, 179, empty)
        cv2.createTrackbar("Min Sat", "HSV", 0, 255, empty)
        cv2.createTrackbar("Max Sat", "HSV", 255, 255, empty)
        cv2.createTrackbar("Min Val", "HSV", 0, 255, empty)
        cv2.createTrackbar("Max Val", "HSV", 255, 255, empty)
        print("Adjust the trackbar until you get your desired colour in focus")
        print("press 'd' to go back to normal mode")

        while True:
            _, img = cap.read()
            new5 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            hue_min = cv2.getTrackbarPos("Min Hue", "HSV")
            hue_max = cv2.getTrackbarPos("Max Hue", "HSV")
            sat_min = cv2.getTrackbarPos("Min Sat", "HSV")
            sat_max = cv2.getTrackbarPos("Max Sat", "HSV")
            val_min = cv2.getTrackbarPos("Min Val", "HSV")
            val_max = cv2.getTrackbarPos("Max Val", "HSV")

            lower = np.array([hue_min, sat_min, val_min])
            upper = np.array([hue_max, sat_max, val_max])

            mask = cv2.inRange(new5, lower, upper)

            new_final = cv2.bitwise_and(img, img, mask=mask)

            cv2.imshow("HSVi", new5)
            cv2.imshow("mask", mask)
            cv2.imshow("result", new_final)

            if cv2.waitKey(1) & k == ord('d'):
                cv2.destroyWindow("HSV")
                cv2.destroyWindow("mask")
                cv2.destroyWindow("HSVi")
                cv2.destroyWindow("result")
                break

    elif k == ord('a'):
        cv2.destroyWindow("camera feed")
        cv2.namedWindow("Parameters")
        cv2.resizeWindow("Parameters", 640, 240)
        cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
        cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)
        cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)
        print("press 'h' to go back to normal mode")


        def getContours(img, imgContour):
            contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                areaMin = cv2.getTrackbarPos("Area", "Parameters")
                if area > areaMin:
                    cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                    print(len(approx))
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)

                    cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20),
                                cv2.FONT_HERSHEY_COMPLEX, .7,
                                (0, 255, 0), 2)
                    cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX,
                                0.7,
                                (0, 255, 0), 2)


        while True:
            success, img22 = cap.read()
            imgContour = img22.copy()
            imgBlur = cv2.GaussianBlur(img22, (7, 7), 1)
            imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
            threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
            threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
            imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
            kernel = np.ones((5, 5))
            imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
            getContours(imgDil, imgContour)
            cv2.imshow("Result", imgContour)
            cv2.imshow("Threshold", imgDil)
            if cv2.waitKey(1) & 0xFF == ord('h'):
                cv2.destroyWindow("Parameters")
                cv2.destroyWindow("Result")
                cv2.destroyWindow("Threshold")
                break
        continue

    elif k == ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.imshow("Scanned photo", frame)
        print("press u if its unreadable")
        print("press b to convert it to black and white form")
        print("press c for OCR")
        print("press e for showing edges")
        print("press n for reducing noise")
        k1 = cv2.waitKey(0)
        if k1 == ord('u'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 165, 1)
            cv2.imwrite("E://pdf//scanned%d.jpg" % i, new)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('b'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("E://pdf///scanned%d.jpg" % i, gray)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('c'):
            cv2.destroyWindow('Scanned photo')
            text = pytesseract.image_to_string(frame)
            print(text)
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('e'):
            cv2.destroyWindow('Scanned photo')
            new1 = cv2.Canny(frame, 200, 220)
            cv2.imwrite("E://pdf///scanned%d.jpg" % i, new1)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue
        elif k1 == ord('n'):
            cv2.destroyWindow('Scanned photo')
            new4 = cv2.GaussianBlur(frame, (9, 9), 0, 0)
            cv2.imwrite("E://pdf///scanned%d.jpg" % i, new4)
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue

    elif k == ord('q'):
        ret = False
        break

cv2.destroyAllWindows()
imagelist = os.listdir("E://pdf")
pdf = FPDF('L', 'mm', 'A4')
for image in imagelist:
    image = "E://pdf//" + image
    pdf.add_page()
    pdf.image(image)
pdf.output("E://your_file.pdf", "F")
