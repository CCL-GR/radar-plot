#!/usr/bin/env python


import sys as sys
import plotly.graph_objects as go
import fileinput
import os as os

# TODO: Fix directory creation from cluttering if garbage input

def make_radar_plot_image(plotter, name, cname, grade_level):
    plotter.update_layout(
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
    make_dir_for_grade(grade_level)
    grade_directory = get_dir_for_grade(grade_level)
    plotter.write_image(f"{grade_directory}/{grade_level}_{cname}_{name}.png")

def make_dir_for_grade(grade_level):
    if not os.path.exists(f"grade_{grade_level}"):
        os.mkdir(f"grade_{grade_level}")

def get_dir_for_grade(grade_level):
    match grade_level:
        case "1":
            return "grade_1"
        case "2":
            return "grade_2"
        case "3":
            return "grade_3"
        case "4":
            return "grade_4"
        case "5":
            return "grade_5"
        case "6":
            return "grade_6"
        case "7":
            return "grade_7"
        case "8":
            return "grade_8"
        case "9":
            return "grade_9"
        case _:
            return "grade_99"

for line in fileinput.input(sys.argv[1]):
    student = line.split(sep=' '),
    student_cname = line.split(sep=' ')[0],
    student_name = line.split(sep=' ')[1],
    student_grade_level = line.split(sep=' ')[2],
    student_ART = line.split(sep=' ')[3],
    student_CHINESE = line.split(sep=' ')[4],
    student_COMPUTER = line.split(sep=' ')[5],
    student_ELA = line.split(sep=' ')[6],
    student_MATH = line.split(sep=' ')[7],
    student_MUSIC = line.split(sep=' ')[8],
    student_PE = line.split(sep=' ')[9],
    student_SCIENCE = line.split(sep=' ')[10],
    stat_visual_spacial = .4*float(student_ART[0]) + .4*float(student_MATH[0]) + .1*float(student_CHINESE[0]) + .1*float(student_PE[0]),
    stat_introspective = .4*float(student_CHINESE[0]) + .4*float(student_ELA[0]) + .1*float(student_ART[0]) + .1*float(student_MUSIC[0]),
    stat_social = .4*float(student_CHINESE[0]) + .3*float(student_ELA[0]) + .2*float(student_PE[0]) + .1*float(student_ART[0]),
    stat_verbal = .4*float(student_CHINESE[0]) + .4*float(student_ELA[0]) + .2*float(student_SCIENCE[0]),
    stat_logical = .4*float(student_MATH[0]) + .4*float(student_COMPUTER[0]) + .2*float(student_SCIENCE[0]),
    stat_musical = .7*float(student_MUSIC[0]) + .3*float(student_PE[0]),
    stat_body = .8*float(student_PE[0]) + .2*float(student_SCIENCE[0]),
    stat_nature = .6*float(student_SCIENCE[0]) + .3*float(student_COMPUTER[0]) + .1*float(student_MATH[0]),
    fig = go.Figure(data=go.Scatterpolar(
        r=[stat_visual_spacial[0], stat_introspective[0], stat_social[0], stat_verbal[0], stat_logical[0], stat_musical[0], stat_body[0], stat_nature[0]],
        theta=['视觉一空间智能<br>(Visual/Spatial intelligence)','内省智能<br>(Intra-personal/<br>Introspective intelligence)','人际社交智能<br>(Inter-personal/Social intelligence)', '语言智能<br>(Verbal/Linguistic intelligence)', '数理逻辑智能<br>(Logical/<br>Mathematical intelligence)', '音乐韵律智能<br>(Musical/Rhythmic intelligence)', '身体运动智能<br>(Bodily/Kinesthetic intelligence)', '自然探索智能<br>(Naturalist intelligence)'],
        fill='toself'
    ))
    make_radar_plot_image(fig, student_name[0], student_cname[0], student_grade_level[0])
    print(student_name[0]), #Shows which students are printing, good for watching if progress is hanging
