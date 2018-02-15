__author__ = 'robincarr'

# The code below is adapted from a post on Daniweb

# Display an animated GIF displaying a series of GIFs
# First, an animated GIF was broken up into a series of GIFs
# using the online site:  http://ezgif.com/split

import time
from Tkinter import *


root = Tk()
root.title("Time to Relax!")

folder_info= "animation_images/orchid/"
# Collect all the images in the animation folder into a big list.
imagelist = []
beginning = folder_info + 'frame_'
ending = '_delay-0.07s.gif'

for n in range(0,12): # Frames are labelled from 0 to 11.
    middle = str(n)
    next_file = beginning + middle + ending
    imagelist.append(next_file)

# extract width and height info
photo = PhotoImage(file=imagelist[0])  # Use first image to establish dimensions
width  = photo.width()
height = photo.height()
print 'The image height and width are:  %d x %d'  % (width, height )

# Create a Canvas object to display the animation.
border_width = 40
canvas = Canvas(width=width + border_width, height=height + border_width, bg='black')
canvas.grid()
# Create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

# Loop through the gif image objects.
# Play the  animation N times.


# The window fades away after the movie is done playing.
def fade():
    for k in range(21):
        root.after(k*200, root.attributes, "-alpha", (1-k*0.05) )
    root.after(4000, root.destroy)


def play_movie(N): # Play movie N times.
    K = len(giflist) # number of frames in movie
    delay = 70 # in milliseconds
    for n in range(N):
        print "Loop Number:", n+1
        for k in range(K):
            print "\tShowing frame %2d of %d" % (k +1, K) # For the user, first frame is frame 1.
            nextFrame = giflist[k]
            canvas.delete(ALL)  # Clear the canvas of all previous images.
            canvas.create_image(border_width / 2 + width / 2.0, border_width / 2 + height / 2.0, image=nextFrame,
                                anchor=CENTER)
            canvas.update()
            root.after(delay) # pause for delay milliseconds.
    print "Your movie selection has ended."
    fade()


# play_movie(10) # Play the full movie this number of times.
play_movie(10)
root.mainloop()

