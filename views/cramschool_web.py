#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:52:32 2020

@author: linxiangling
"""

from flask import Blueprint, render_template

cramschool_web=Blueprint('cramschool_web', __name__)

@cramschool_web.route("/cramschool")
def cramschool():
    return render_template("cramschool.html")

@cramschool_web.route("/cramschool_attendence")
def cramschool_attendence():
    return render_template("cramschool_attendence.html")

@cramschool_web.route("/cramschool_classroom")
def cramschool_classroom():
    return render_template("cramschool_classroom.html")

@cramschool_web.route("/cramschool_course")
def cramschool_course():
    return render_template("cramschool_course.html")

@cramschool_web.route("/cramschool_makeup_class")
def cramschool_makeup_class():
    return render_template("cramschool_makeup_class.html")

@cramschool_web.route("/cramschool_staffstudent")
def cramschool_staffstudent():
    return render_template("cramschool_staffstudent.html")

