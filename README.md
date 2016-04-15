# raspi_image_reel
A button controlled image reel for the Raspberry Pi

**_Requires images to be placed in the img_folder_** 

- Loads images from folder into an image reel which is controlled by a button.
- This can be easily scaled up to make an exhibtion style terminal

By default the button is connected to PIN 11 and 3.3v PIN.
Uses an internal pulldown resistor.


### Issues:
1. get_paths() function loads any file. could use imghdr to specify only images. (However imghdr often doesn't recognise .jpg!)
2. Images need to be scaled properly to the screen. This has been tested with images larger than the screen and it works ok at 1280x720.

Could possibly added a left and right button or touchpad(swipe left/right)



