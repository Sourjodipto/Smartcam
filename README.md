# Smartcam

Technology Stack used: Python, openCV.
Features:
1. Connected the phone camera with the laptop using python.
2. Used black and white conversion (if the image is normal and readable)
3. Used adaptive threshoding(if the image is unclear and not readable)
4.  Live Colour Detection and Colour tracking mode :
	In this mode we can detect any specific colour present in the live video by adjusting HSV properties in the trackbar. Once the colour is detected properly, the live camera feed will only show the objects which are of that specific colour, objects of other colours will be blacked out completely.
	Explanation : At first I converted the captured frame to HSV format as it is more convenient to work with. Then I created 6 trackbars in a different window where we can input trackbar values of our preferences. I assigned 6 variables to the 6 trackbars. With cv2.getTrackbarPos , the assigned variables get input from the trackbar position we provide. Then I defined two matrices named ‘lower’ and ‘upper’ as numpy arrays, which store the lower and upper values of the variables respectively. Now I created a mask where I used the function cv2.inrange which only gives the values in the specified lower and upper range. Finally, I merge the original image and the mask to get the final result. Here I use the function cv2.bitwise_and() and in argument I put the original image and the mask so that only whatever is common in both of them will be visible. The rest of the elements in the image will be blacked out.
5. Optical Character Reader : (for captured frame)
	It prints any text that is there in the captured frame.
	Explanation : Imported pytesseract and used the function pytesseract.image_to_string() to convert the text elements of the scanned frame to a string.
6. Edge detection : (for captured frame)
	It detects edges of the objects in the captured frame.
	Explanation : used canny edge detection by putting the function cv2.canny() where in the argument we I put the first and second threshold values 200 and 220 to accurately identify pixels which are actually contributing to the edges.
7. Live Object detection and shape identification mode :
	Here I’m identifying objects and shape using the basic method of finding contours.
	Contours are basically a curve joining all the continuous points (along the boundary), having same color or intensity. 
The code blurs the image a little bit at first.
Then it turns it into a grayscale image.
Now canny edge detection is applied. As we know, canny edge requires two threshold values in argument. So for the convenience of the user and for improving accuracy, I decided to take threshold inputs from the user.
So I used the easiest trackbar method in the same way I did for live colour detection, as mentioned in point #1.
Now I declared a kernel of odd size as numpy array which would be used to convolve with the cannied image.
Then I defined the dilation function to remove noise and overlaps from the cannied image.
Now I finally sent this dilated image through the contour function.
For removing unwanted small object in the output as per users liking, I introduced a for loop. In the loop I set up variables named area and areamin. Also assigned the areamin with a trackbar which will take inputs from user. Suppose, If areamin is set to 5 unit by the user, the contours will be shown only if the object in the frame has an area more than 5 unit. Thus we can remove small dots and things like that from the output.
	Used cv2.arcLength to find the length of contours.
	Used cv2.contourArea to find the area.
	Used approximation of poly to approximate the shape of the object.
The approximation array will have certain amounts of points based on  which we can identify the shapes.
Finally used cv2.putText to have the number of points and the area written on the frame.
8. Noise Reduction: (for captured frame)
	Reduces noise of a grainy image.
	Used cv2.GaussianBlur to blur out the captured image.


     








Name:     Sourjodipto Das                                     Mobile Number: 8159944466

