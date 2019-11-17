
import cv2

class WebcamX(object):
    def __init__(self,camera_index = 0):
        self.cam_idx = camera_index
        self.cap = None
        self.frame = None

    def acquisition(self):
        self.cap = cv2.VideoCapture(self.cam_idx,cv2.CAP_V4L)
        print("Webcam is opened...")

    def get_frame(self):
        _, self.frame = self.cap.read()
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame) 
        print("Frame is taking...")
        return self.frame

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print("Webcam is closed...")

if __name__ == '__main__':

    cam = WebcamX()
    cam.acquisition()
    for i in range(100):
        frame = cam.get_frame()
        #height, width, bytesPerComponent = frame.shape
        #print("frame height = {} width = {} bytesPerComponent = {}".format(height,width,bytesPerComponent))
        print("frame height = {} width = {} bytesPerComponent = {}".format(frame.shape[0],frame.shape[1],frame.shape[2]))
        cv2.imshow("Webcam Frame Window", frame)
        cv2.waitKey(1)
        print(str(i) + ".frame")

    cam.close()
    print("Webcam Finished...")