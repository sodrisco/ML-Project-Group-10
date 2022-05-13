#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:47:36 2022

@author: stevenodriscoll
"""

import numpy as np


def wavsplit(file, name):
    '''
    Split the wav files into three second sections

    Parameters
    ----------
    file : string
        wav file in folder tjhat needs splitting 
    name : file taken from
        The name of the file to keep track of all the split data original locations.

    Returns
    -------
    sound : AudioSegment
        AudioSegment object of the original wav file input 

    '''
    from pydub import AudioSegment
    
    sound = AudioSegment.from_wav(file)
    
    sound = sound.set_channels(1)
    
    #beginning of the audio
    zero_mark = 0
    #three seconds after zero_mark to signify end of section
    three_mark = 3000
    #naming convention for save files
    split_name = 0
    
    #end time of the audiofile in seconds
    end = sound.duration_seconds * 1000
    
    while(three_mark<end):
        
        #three second section
        split_section = sound[zero_mark:three_mark]
        
        
        #save segment
        split_section.export(f"{name}_section_{split_name}.wav", format = "wav")
        
        #move to the next three sectond segment
        zero_mark += 3000
        three_mark += 3000
        split_name += 1
        
    return sound
    
#%%split up all crowd chatter data

wav_files = np.array([
"crowd-talking-1.wav",
"crowd-talking-2.wav",
"crowd-talking-3.wav",
"crowd-talking-4.wav",
"crowd-talking-5.wav",
"crowd-talking-6.wav",
"crowd-talking-7.wav",
"crowd-talking-8.wav",
"crowd-talking-9.wav",
"crowd-talking-10.wav"])


for i in range(len(wav_files)):
    
    sound = wavsplit(wav_files[i],f'file{i}')



#%%testing

from pydub import AudioSegment

test = AudioSegment.from_wav("file0_section_0.wav")

test1 = test.export("test1.wav", format = "wav")

