#########################
Linux Development Guide
#########################

Welcome to the Axon Linux Development Guide, designed especially for those
new to the world of Single Board Computers! This guide will walk you through
the fundamental steps of creating the Axon Linux Operating System,
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

.. toctree::
   :caption: Development Guide
   :maxdepth: 3
   :titlesonly:

   u-boot/index

..
   Linux SDK <axon-linux-sdk>
   Linux Kernel <axon-linux-kernel>
