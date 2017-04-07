# -*- coding: UTF-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')  # 实例化蓝本

from . import views
