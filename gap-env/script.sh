#!/bin/sh
gap -r -b -q << input
$ARRAY * 2;
input

# runs the lines between input and input as gap commands
