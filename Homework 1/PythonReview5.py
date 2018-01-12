import time

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

# create the root window
root = tk.Tk()


def back():  # Complete this stub. Start by removing the return.
    print("Back button pressed.")
    global N

    # Add your code here. First update N. Just decrement it by 1.
    # Take the remainder to be sure the index is always valid.
    N -= 1
    N = N % len(photos)
    # Then update the text_display and picture_display widgets.
    text_display["text"] = description[N]
    picture_display["image"] = photos[N]
    root.update()

def forward():  # Complete this stub. Start by removing the return.
    print("Forward button pressed.")
    global N

    # Add your code here. First update N. Just increment it by 1.
    # Take the remainder to be sure the index is always valid.
    N += 1
    N = N % len(photos)
    # Then update the text_display and picture_display widgets.
    text_display["text"] = description[N]
    picture_display["image"] = photos[N]
    root.update()


# This makes it possible for the user to choose AutoPlay again.
def enable_autoplay():
    auto_button.config(text="AutoPlay")
    auto_button.config(command=autoplay)


# autoplay_mode = True    # This variable was not really needed.

# A method to show the images in a cycle, (repeating over and over from the available images).
def autoplay():
    back_button.configure(state=tk.DISABLED)
    forward_button.configure(state=tk.DISABLED)

    global pending_job_ID
    global N
    if auto_button["text"]=="AutoPlay":
        print("Autoplay button pressed.")
    auto_button["text"]="Stop AutoPlay"
    auto_button.config(command=stop_autoplay)  # If the same button is pressed again, autoplay stops.

    # global autoplay_mode     < - -  This variable is no longer necessary thanks to the after_cancel() method.
    # autoplay_mode = True
    text_display["text"]= description[N]
    picture_display["image"] = photos[N]
    root.update()
    pending_job_ID = root.after(2000, autoplay)  # We need to record the ID of this pending job, so we can cancel it.
    N = (N+1) % len(photos)   # Index for the next image.

def stop_autoplay():
    global pending_job_ID;
    global N
    root.after_cancel(pending_job_ID)  # Cancels the pending autoplay job that results from the recursion.
    N = (N-1) % len(photos)   # Go back to Index for the last shown image.

    back_button.configure(state=tk.NORMAL)
    forward_button.configure(state=tk.NORMAL)

    if auto_button["text"]=="Stop AutoPlay":
        print("Stop Autoplay button pressed.")
    # Now enable autoplay to resume if the user wishes.
    root.after(1000, enable_autoplay)



""" The geometry() method sets a size for the window and positions it on the screen.
The first two parameters are the width and height of the window in pixels.
The last two parameters are x and y screen coordinates from the top left corner."""
root.geometry("820x560+50+50")
root.title("Natural Wonders")

# delay in seconds (time each slide shows)
delay = 2.5

# create a list of image file names for the slideshow.
# images selected from: http://www.nature-pictures.info/the-15-craziest-things-in-nature-you-wont-believe-actually-exist/
# (you can add more files as needed)

imageFiles = [
'images/Crater.gif',
'images/CrystalCave_Mexico.gif',
'images/VolcanicLightning.gif',
'images/RainbowEucalyptusTrees_Kailua_Hawaii.gif',
'images/BloodFalls_Antartica.gif',
'images/SpiderWebs_Pakistan.gif',
'images/SaltFlats_Bolivia.gif',
'images/SandstoneFormations_Arizona.gif',
'images/LakeHillier_Australia.gif',
'images/LakeBaikal_Russia.gif'
]

description = [
    "Underground natural springs in Mexico.",
    "Giant Crystal Cave in Nacia, Mexico.",
    "Volcanic Lightning.",
    "Rainbow Eucalyptus trees in Kailua, Hawaii.",
    "Blood Falls in Antartica",
    "Trees completely cocooned in spider webs in Pakistan.",
    "Reflective Salt Flats in Bolivia.",
    "Beautiful Sandstone Formations in Arizona.",
    "Lake Hillier in Australia",
    "Beautiful Turquoise Ice on Lake Baikal in Russia"
]
#  Prepare the list of image objects using PhotoImage
photos = [tk.PhotoImage(file=fname) for fname in imageFiles]


# Present the pictures inside a black frame.
frame = tk.Frame(root, bg="black", padx = 10, pady=10)
frame.pack(fill=tk.X)

# Add a label to show a description of the image.
text_display = tk.Label(frame, bg="beige", padx=6, pady=6)
text_display.pack(fill=tk.X)

control_frame = tk.Frame(frame, bg="lightyellow")
control_frame.pack(fill=tk.X)

back_button = tk.Button(control_frame, text="Back", command=back)  # Specify that the callback method is named back.
back_button.pack(side=tk.LEFT, padx = 10)

forward_button = tk.Button(control_frame, text="Forward", command=forward)  # Specify that the callback method is named forward.
forward_button.pack(side=tk.RIGHT)

auto_button = tk.Button(control_frame, text="AutoPlay", command=autoplay)
auto_button.pack(side=tk.BOTTOM)


# A. Display each picture inside a Label, inside the frame.
picture_display = tk.Label(frame, bg="beige", padx=6, pady=6)
picture_display.pack(padx=6, pady=6)

# Show the initial image and description, which has index 0.
N=0 # Index of the current image.
text_display["text"]= description[0]
picture_display["image"] = photos[0]

# This next line was added so we can cancel the autoplay.
pending_job_ID = root.after(1, stop_autoplay)  # This will be a global variable, so w can cancel the job using after_cancel()

# B. Or you could use a button instead of the Label.
# Then the button can also be used as a control, say to quit the program as shown below.
# button = tk.Button(frame, command=root.destroy)
# button.pack(padx=5, pady=5)


# execute the event loop
root.mainloop()