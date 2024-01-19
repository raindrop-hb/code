#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 , Inc. All Rights Reserved 
# @Time    : 2023/5/8 21:22
# @Author  : raindrop
# @Email   : 1580925557@qq.com
# @File    : codee.py.py
from flask import Flask, request, jsonify
#from flask_cors import CORS

import os
import requests

app = Flask(__name__)
#CORS(app,resource=r'/*')


@app.route('/',methods=['POST'])
def func():
    if request.method=="POST":
        url=request.form.get("u")
        print("收到链接"+str(url))
        res = {"result": "识别失败"}
        return jsonify(code=0, data=res)


