from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import cv2
import pyttsx
import time

time_temp = time.clock()
time_e = 0
engine = pyttsx.init()
file = r"C:\Users\Travis Pittman\Desktop\Drive_Thru\Faces\face.jpeg"
face = 0
while(1):
    
    while(face == 0):

        # Camera 0 is the integrated web cam on my netbook
        camera_port = 0
         
        #Number of frames to throw away while the camera adjusts to light levels
        ramp_frames = 30
         
        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        camera = cv2.VideoCapture(camera_port)
         
        # Captures a single image from the camera and returns it in PIL format
        def get_image():
         # read is the easiest way to get a full image out of a VideoCapture object.
         retval, im = camera.read()
         return im
         
        # Ramp the camera - these frames will be discarded and are only used to allow v4l2
        # to adjust light levels, if necessary
        for i in xrange(ramp_frames):
         temp = get_image()
        #print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = get_image()
        
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)
         
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        del(camera)

        time_e = time.clock() - time_temp
	# print time_e
        # print time.clock()
        # print time_temp
        if(time_e >= 3):
            time_e = 0
            time_temp = time.clock()

            app = ClarifaiApp(api_key='f821bb98d49942dfbe8018e898fe72c0')

            model = app.models.get('face-v1.3')
            image = ClImage(file_obj=open(r'C:\Users\Travis Pittman\Desktop\Drive_Thru\Faces\face.jpeg', 'rb'))
            picInfo = (model.predict([image]))

            try:
                x = (picInfo['outputs'][0]['data']['regions'])
                face = 1
            except:
                face = 0
    
    engine.say('Alexa.')
    engine.runAndWait()
    engine.say('run Clever Cashier.')
    engine.runAndWait()
    print("Welcome to Dairy Queen")
    print("Begin order when Ready")
    # print("Hand off to alexa here...")
    # print("Run until there is no more face seen")
    while(face):
        # Camera 0 is the integrated web cam on my netbook
        camera_port = 0
         
        #Number of frames to throw away while the camera adjusts to light levels
        ramp_frames = 30
         
        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        camera = cv2.VideoCapture(camera_port)
         
        # Captures a single image from the camera and returns it in PIL format
        def get_image():
         # read is the easiest way to get a full image out of a VideoCapture object.
         retval, im = camera.read()
         return im
         
        # Ramp the camera - these frames will be discarded and are only used to allow v4l2
        # to adjust light levels, if necessary
        for i in xrange(ramp_frames):
         temp = get_image()
        # print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = get_image()
        
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)
         
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        del(camera)

        time_e = time.clock() - time_temp
        # print time_e
        # print time.clock()
        # print time_temp
        if(time_e >= 3):
            time_e = 0
            time_temp = time.clock()

            app = ClarifaiApp(api_key='c6af06c1faa0445ca7ec5aaab2c015e6')

            model = app.models.get('face-v1.3')
            image = ClImage(file_obj=open(r'C:\Users\Travis Pittman\Desktop\Drive_Thru\Faces\face.jpeg', 'rb'))
            picInfo = (model.predict([image]))

            try:
                x = (picInfo['outputs'][0]['data']['regions'])
                face = 1
            except:
                face = 0
    print
    print
    print("Thank you for coming, Please come again")
    print
    print

