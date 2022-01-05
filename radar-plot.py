#!/usr/bin/env python


import sys as sys
import plotly.graph_objects as go
import fileinput
import os as os


def make_radar_plot_image(plotter, name, cname, grade_level):
    plotter.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10],
                tick0=0,
                nticks=10,
                categoryorder="array",
                categoryarray=[0,1,2,3,4,5,6,7,8,9,10]
            ),
        ),
        showlegend=False
    )
    grade_directory = get_dir_for_grade(grade_level)
    make_dir_for_grade(format_grade_string(grade_directory))
    plotter.write_image(f"{grade_directory}/{grade_level}_{cname}_{name}.png")

def format_grade_string(grade_directory_string):
    grade = grade_directory_string[-2:]
    if (grade[0] == "_"):
        grade = grade_directory_string[-1:]
    return str(grade)

def make_dir_for_grade(grade_level):
    if not os.path.exists(f"grade_{grade_level}"):
        os.mkdir(f"grade_{grade_level}")

def get_dir_for_grade(grade_level):
    match grade_level:
        case "k":
            return "grade_K"
        case "K":
            return "grade_K"
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
        case "10":
            return "grade_10"
        case "11":
            return "grade_11"
        case "12":
            return "grade_12"
        case _:
            return "grade_99"

for line in fileinput.input(sys.argv[1]):
    student = line.split(sep=' '),
    student_cname = line.split(sep=' ')[0],
    student_name = line.split(sep=' ')[1],
    student_grade_level = line.split(sep=' ')[2],
    stat_verbal = float(line.split(sep=' ')[3])*2,
    stat_logical = float(line.split(sep=' ')[4])*2,
    stat_musical = float(line.split(sep=' ')[5])*2,
    stat_body = float(line.split(sep=' ')[6])*2,
    stat_visual_spacial = float(line.split(sep=' ')[7])*2,
    stat_social = float(line.split(sep=' ')[8])*2,
    stat_introspective =float(line.split(sep=' ')[9])*2,
    stat_nature = float(line.split(sep=' ')[10])*2,
    fig = go.Figure(data=go.Scatterpolar(
        r=[stat_verbal[0], stat_logical[0], stat_musical[0], stat_body[0], stat_visual_spacial[0], stat_social[0], stat_introspective[0], stat_nature[0]],
        theta=['语言智能<br>(Verbal/Linguistic intelligence)',
               '数理逻辑智能<br>(Logical/<br>Mathematical intelligence)',
               '音乐韵律智能<br>(Musical/Rhythmic intelligence)',
               '身体运动智能<br>(Bodily/Kinesthetic intelligence)',
               '视觉一空间智能<br>(Visual/Spatial intelligence)',
               '人际社交智能<br>(Inter-personal/Social intelligence)',
               '内省智能<br>(Intra-personal/<br>Introspective intelligence)',
               '自然探索智能<br>(Naturalistic intelligence)'],
        fill='toself'
    ))
    make_radar_plot_image(fig, student_name[0], student_cname[0], student_grade_level[0])
    print(student_name[0]), #Shows which students are printing, good for watching if progress is hanging
