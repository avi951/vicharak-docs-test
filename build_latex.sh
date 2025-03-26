#!/bin/bash

make dirhtml -j $(nproc --all)
make latexpdf
