**********************Cetrion Package Instructions**********************



Cetrion is an animated loading screen for Projects under Cetrion division
written in python and applicable for tkinter windows. This is particularly 
useful when importing heavy python modules. The program is not perfect 
since tkinter is not thread safe and may create the following errors if not
handled properly.
1.Tcl_AsyncDelete: async handler deleted by the wrong thread
2.RuntimeError: main thread is not in main loop


Initialization: Copy the Cetrion.py and the logo.png file in your programs 
root directory.


Minimal Animation:


import Cetrion,time
Animator=Cetrion.Animator()
Animator.start()
time.sleep(3) #import modules instead
Top=Animator.stop()
#Your Tkinter Main Window
Top.mainloop()


Things to Remember:

1.If you ever need to destroy the main window programatically,
do not call .destroy() method. Use del <windowname> instead.
Cetrion has a way to handle WM_DELETE_WINDOW message which is
triggered only when client presses the 'close window' button at 
the top right corner of the window.

2. If you need to redefine WM_DELETE_WINDOW protocol, be sure to
add a .quit() at the end of your protocol handler function.


Documentation:


Class Cetrion.Animator(self,ui=True,param=None,bg='green',
fg='black',font='Calibri',image_location=(.5,.6,'s'),
text_location=(.5,.6,'n'),image_size=None,text_size=None)


 Arguments:
  ui:		 if true, returns a tkinter object for main window.
  param:	 a list or tuple containing the arguments of the 
		 geometry (window size) of the animation.
  bg:		 background color of the animation.
  fg:		 text color of the animation
  font:		 font family of the animation text
  image_location:a list or tuple containing the relx, rely and anchor
		 value of the image.
  text_location: a list or tuple containing the relx, rely and anchor
		 value of the text.
  image_size:	 a list or tuple containing the width and height of
		 the image.
  text_size:	 font size of the text.

 Instance Methods:
  Animator.start():
	Starts The animation.
  Animator.stop():
	Closes the animation.
  Animator.iterate():
	Internal function, called by Animator.start()
  Animator pquit():
	Internal function, called by Animator.stop()
**Internal functions are not to be called explicitly.


Known Issues:
1. If ui is set to False and a tkinter object is created afterwards, creating
a Photoimage object for that program causes the Runtime Error.
 Aid: set ui to True and withdraw the returned tkinter object as long as you
      don't need it.

Goals for next version:


1. Fix issues and bugs.
2. Improve graphics and animation control (Rounded widgets,window,animation timout and more...)
