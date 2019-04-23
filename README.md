# LipReadingGUI

This is an implementation of LipNet for CSCE 629 - Neural Networks at Texas A&M University.
Reference - https://github.com/rizkiarm/LipNet
Research Paper - https://arxiv.org/abs/1611.01599

The repository contains a small subset of GRID CORPUS to see how code for preprocessing, training and GUI works. 

# Dataset Preprocessing
Run mouth_extract.py in the MouthExtract directory. The code loads videos from the Video folder and saves each video as 75 mouth-crop frames. 

# Network Training
Run train.py in the Training directory. The code loads training data which is preprocessed. 
