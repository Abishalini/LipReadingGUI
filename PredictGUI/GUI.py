import Tkinter as tkinter
import cv2
import Image, ImageTk
import time
import tkFileDialog

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

  	self.frame = tkinter.Frame(window)
	self.frame.pack()

	self.bottomFrame = tkinter.Frame(window)
	self.bottomFrame.pack(side="bottom")

        # Button that lets the user take uploads a video
        self.btn_upload = tkinter.Button(window, text="Upload", width=10, command=self.upload)
        self.btn_upload.pack(side="top")

        self.btn_caption = tkinter.Button(window, text="Caption", width=10, command=self.caption)
        self.btn_caption.pack(side="top")

        self.btn_clear = tkinter.Button(window, text="Clear", width=10, command=self.clear)
        self.btn_clear.pack(side="top")

	self.T = tkinter.Text(window, height=20, width=45)
	self.T.pack(side="bottom")

        self.window.mainloop()

    def clear(self):
	self.T.delete(1.0, tkinter.END)
	self.canvas.delete("all")

    def caption(self):
	self.T.insert('1.0', "My name is Mike.")

    def upload(self):
        self.window.filename = tkFileDialog.askopenfilename()
	print(self.window.filename)
	self.video_source = self.window.filename

	self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above source size
        self.canvas = tkinter.Canvas(self.window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack(side="bottom")

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

    # Function to use if the architure allows captioning live video
    def record(self):
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above source size
        self.canvas = tkinter.Canvas(self.window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
root = tkinter.Tk()
App(root, "Tkinter and OpenCV")
