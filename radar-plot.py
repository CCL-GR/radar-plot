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
    file_name = student_name[0],
    student2 = line.split(sep=' ')[1],
    st2sc = student2[0],
    student3 = line.split(sep=' ')[2],
    st3sc = student3[0],
    student4 = line.split(sep=' ')[3],
    st4sc = student4[0],
    student5 = line.split(sep=' ')[4],
    st5sc = student5[0],
    student6 = line.split(sep=' ')[5],
    st6sc = student6[0],
    student7 = line.split(sep=' ')[6],
    st7sc = student7[0],
    student8 = line.split(sep=' ')[7],
    st8sc = student8[0],
    student9 = line.split(sep=' ')[8],
    st9sc = student8[0],
    print(student_name[0]),

    fig = go.Figure(data=go.Scatterpolar(
        r=[st2sc[0], st3sc[0], st4sc[0], st5sc[0], st6sc[0], st7sc[0], st8sc[0], st9sc[0]],
        theta=['[ART]Visual/Spacial Intelligence','[CHINESE]Intra-personal/Introspective Intelligence','[COMPUTER]Interpersonal/Social Intelligence', '[ELA]Verbal/Linguistic Intelligence', '[MATH]Logical/Mathematical Intelligence', '[MUSIC]Musical Rhythmic Intelligence', '[PE]Bodily/Kinesthetic Intelligence', '[SCIENCE]Naturalist Intelligence'],
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

    # df = pd.DataFrame(dict(
    #     r=[st2sc[0], st3sc[0], st4sc[0], st5sc[0], st6sc[0], st7sc[0], st8sc[0], st9sc[0]],
    #     theta=['[ART]Visual/Spacial Intelligence','[CHINESE]Intra-personal/Introspective Intelligence','[COMPUTER]Interpersonal/Social Intelligence', '[ELA]Verbal/Linguistic Intelligence', '[MATH]Logical/Mathematical Intelligence', '[MUSIC]Musical Rhythmic Intelligence', '[PE]Bodily/Kinesthetic Intelligence', '[SCIENCE]Naturalist Intelligence']))
    # fig = po.line_polar(df, r='r', theta='theta', line_close=True)
    # fig.update_traces(fill='toself')
    # fig.write_image(student_name[0] + ".png")
    # fig.data = []
    # fig.layout = {}
