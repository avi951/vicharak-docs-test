:nosearch:

How to change U-Boot Logo
=========================

**To change the U-Boot logo, you’ll need to follow these steps:**

-  Prepare your new logo.

.. warning::
   Ensure that your logo is in the BMP (Bitmap) format, with a colour
   depth of 24 bits (RGB). The logo size should be less than 1MB to fit
   within the constraints of U-Boot.

- Convert the logo to the correct format:

.. note:: 
   If your logo is not already in the correct format, you can use an
   image editing software like GIMP or Photo-shop to convert it. Open
   the logo in the software, adjust the colour depth to 24 bits, and
   save it in BMP format.

-  Access the U-Boot source code: Obtain the U-Boot source code for
   Vaaman from Vicharak `U-Boot GitHub
   repository <https://github.com/vicharak-in/u-boot-vicharak>`__.

-  Locate the logo file: In the U-Boot source code, navigate to the
   ``drivers/video/drm/`` where the logo file is contained. The logo
   file is typically named logo.h or similar.

-  Converting BMP file to logo.h (Using vicharak ``bmp2hex`` tool).

.. code:: bash

   ./tools/bmp2hex logo.bmp

   mv logo.h drivers/video/drm/logo.h

-  Recompile U-Boot: Recompile the U-Boot source code with your new
   logo. Follow the instructions provided with the U-Boot source code to
   build it for your specific board or device.

-  Flash the new U-Boot image: Once you have successfully compiled the
   U-Boot source code, you’ll need to flash the new U-Boot image to your
   device.

.. note::
   The flashing process depends on the specific board you are using.
   Refer to the Vaaman’s documentation or the U-Boot documentation for
   instructions on how to flash the new image.

-  Test the new logo: After flashing the new U-Boot image, reboot your
   device. You should now see your custom logo during the U-Boot boot-up
   process.
