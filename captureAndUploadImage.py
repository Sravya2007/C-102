import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
    return img_name
    print("Snapshot taken!")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'zA73qgx1C5kAAAAAAAAAAQTFxjnFXvL_c2R5nOQoNSWla0oTOG_c3WCXBWPzk1R0'
    file = img_name
    file_from = file
    file_to = "/Security System/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded!")

def main():
    while(True):
        if((time.time() - start_time) >= 10):
            name = take_snapshot()
            upload_file(name)

main()