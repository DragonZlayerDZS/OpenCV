# OpenCV
I'm learning how to use OpenCV. I'll put some programs here that I make or use for OpenCV
# Overview
I'll put some programs here for detecting faces, eyes, mouths, etc. I might also add some kind of action for it to do when it sees a certain face(like send a message, record, or anything else).
# Comments/Feedback
If you have any feedback or comments for me feel free to tell me here or email me at `ogttv.streamerbtw7@gmail.com`
# Programs and folders
`cascades` folder has default files to identify a face(not recognize, identifying just means it'll tell you when it sees a face)

`images` folder is where you put the folders of peoples faces.

`venv` folder (for the virtual environment to run the program)

`base.py` not needed to run any programs. It is just the base code used in most of the files

`camera-test.py` just used to test out openCV and to make a normal color frame and a grayscale frame

`faces.py` facial recognition program(and eyes and smile)

`faces-train.py` stores the faces and who they are from the `images` folder onto the `labels.pickle` file

`labels.pickle` contains the labels(folders) with all the faces for faces.py to use

`README.md` this file

`record-video.py` program that records a video(has no sound) and can be implemented into the `faces.py` file

`res-change` program that changes the resolution of the camera and can be implemented into the `faces.py` file

`trainer.yml` trains the facial recognition program with what faces to recognize
# How to close frames
Press `q` on any frame to close all that are open.
# How to use
### Initial Startup

Take some pictures of people you want it to recognize(the more pictures you have per person, the higher the accuracy will be). Separate the pictures into folders named after the people. Put the folders in the `images` folder. 

### Running for the first time

Run the `faces-train.py` program, and wait for it to finish. Run the `faces.py` program and put the face of whomever you want it to recognize up to the camera(either irl or a photo). Try rotating the face or putting the face at different angles to see if the program is recognizing it good. Press `q` to close the frame.

### Setting up to train the program

When you close the frame a file will be saved called `number.png` (instead of *number* it'll just be a number ex:1,2,3,4,5,etc.). That is an image of the last time the face was in the frame before you closed it. Move the file into the appropriate label(folder) in the `images` folder, rename the file if necessary. Run the program again a few times to add more images or just manually put images of whoever you are trying to recognize in the label.

### Training the program

Now that you have more images in the appropriate label, run the `faces-train.py` program again. Wait for it to finish and then run the `faces.py` program again. It should now have better accuracy, but if it doesn't then just repeat the steps for **Setting up to train the program** and for **Training the program**.
 
### End

These are all the instructions I have right now. When I make more programs, I will add more instructions for how to use them.