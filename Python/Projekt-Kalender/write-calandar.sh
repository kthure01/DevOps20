#!/usr/bin/bash

todaysDate=$(date +"%d")
cal |sed "s/$todaysDate/($todaysDate)/g" > /tmp/todaysDate.txt

