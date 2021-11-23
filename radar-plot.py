#!/usr/bin/env python

import os as os
import sys as sys
import plotly.graph_objects as go
import pandas as pd
import fileinput

if not os.path.exists("images"):
    os.mkdir("images")

for line in fileinput.input("/home/carson/Documents/4th_student_scores_transposed.csv"):
    student = line.split(sep=' '),
    student_name = line.split(sep=' ')[0],
    student_ART = line.split(sep=' ')[1],
    student_CHINESE = line.split(sep=' ')[2],
    student_COMPUTER = line.split(sep=' ')[3],
    student_ELA = line.split(sep=' ')[4],
    student_MATH = line.split(sep=' ')[5],
    student_MUSIC = line.split(sep=' ')[6],
    student_PE = line.split(sep=' ')[7],
    student_SCIENCE = line.split(sep=' ')[8],
    stat_visual_spacial = .4*float(student_ART[0]) + .4*float(student_MATH[0]) + .1*float(student_CHINESE[0]) + .1*float(student_PE[0]),
    stat_introspective = .4*float(student_CHINESE[0]) + .4*float(student_ELA[0]) + .1*float(student_ART[0]) + .1*float(student_MUSIC[0]),
    stat_social = .4*float(student_CHINESE[0]) + .3*float(student_ELA[0]) + .2*float(student_PE[0]) + .1*float(student_ART[0]),
    stat_verbal = .4*float(student_CHINESE[0]) + .4*float(student_ELA[0]) + .2*float(student_SCIENCE[0]),
    stat_logical = .4*float(student_MATH[0]) + .4*float(student_COMPUTER[0]) + .2*float(student_SCIENCE[0]),
    stat_musical = .7*float(student_MUSIC[0]) + .3*float(student_PE[0]),
    stat_body = .8*float(student_PE[0]) + .2*float(student_SCIENCE[0]),
    stat_nature = .6*float(student_SCIENCE[0]) + .3*float(student_COMPUTER[0]) + .1*float(student_MATH[0]),

    print(student_name[0]),


    fig = go.Figure(data=go.Scatterpolar(
        r=[stat_visual_spacial[0], stat_introspective[0], stat_social[0], stat_verbal[0], stat_logical[0], stat_musical[0], stat_body[0], stat_nature[0]],
        theta=['视觉一空间智能<br>(Visual/Spatial intelligence)','内省智能<br>(Intra-personal/Introspective intelligence)','人际社交智能<br>(Inter-personal/Social intelligence)', '语言智能<br>(Verbal/Linguistic intelligence)', '数理逻辑智能<br>(Logical/Mathematical intelligence)', '音乐韵律智能<br>(Musical/Rhythmic intelligence)', '身体运动智能<br>(Bodily/Kinesthetic intelligence)', '自然探索智能<br>(Naturalist intelligence)'],
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,5],
                tick0=0,
                nticks=5,
                categoryorder="array",
                categoryarray=[0,1,2,3,4,5]
            ),
        ),
        showlegend=False
    )
    fig.write_image(student_name[0] + ".png")
