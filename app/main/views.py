# -*- coding: UTF-8 -*-
from . import main

from flask import Flask, render_template, flash, redirect, url_for, request, current_app


@main.route('/', methods=['GET', 'POST'])
def train():
    return render_template('index.html')

