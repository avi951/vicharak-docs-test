#########################
Linux Development Guide
#########################

Welcome to the Vaaman Linux Development Guide, designed especially for those
new to the world of Single Board Computers! This guide will walk you through
the fundamental steps of creating the Vaaman Linux Operating System,
covering key components like the bootloader, Linux kernel, and rootfs.

U-Boot (Universal Bootloader)
------------------------------
Let's start with U-Boot, also known as the Universal Bootloader. Think of it
as the conductor orchestrating the symphony of your Vicharak board. U-Boot
takes the lead in initializing hardware and loading the Linux kernel.
In simpler terms, it's the maestro ensuring everything kicks off smoothly.

Linux Kernel
------------
Now, let's dive into the heart of the matter - the Linux kernel. This is the
powerhouse, the brain of your operating system. Here, you'll learn how to
build and customize the Linux kernel specifically tailored for your Vicharak
computer board. It's like giving your computer its unique set of skills.

Linux SDK (Software Development Kit)
------------------------------------
The Linux SDK is like your toolbox for crafting applications and tools that run
on your Vaaman board. In this section, we'll guide you through setting up the
Linux SDK and show you the ropes of cross-compiling software for your embedded
system. We'll even explore how to build your very own Debian, Ubuntu, Yocto, or
Android system. It's like unleashing your creativity on your computer!

So, if you're ready to embark on a journey into the heart of Single Board
Computer development, grab your toolkit and let's get started with the
Vaaman Linux Development!

.. toctree::
   :caption: Development Guide
   :titlesonly:

   U-Boot <u-boot>
   Linux Kernel <linux-kernel>
   Linux SDK <linux-sdk>
