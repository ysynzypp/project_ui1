# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 9:48
# @Author  : mao
# @Explain :
import os

# 获取工程的父节点系统路基，后续文件的路径从父节点拼接
# BASEPATH = Path.cwd().parent


BASEPATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#   数据存放路径
class path:
    Case = os.path.join(BASEPATH, "date", "case.xlsx")

    Interface = os.path.join(BASEPATH, "date", "Interface.xlsx")

    LogConfig = os.path.join(BASEPATH, "config", "LogConfig.yaml")

    LogDate = os.path.join(BASEPATH, "log")

    EmailConfig = os.path.join(BASEPATH, "config", "EmailConfig.yaml")

    Report = os.path.join(BASEPATH, "report")

    ProjectConfig = os.path.join(BASEPATH, "config", "ProjectConfig.yaml")

    MysqlConfig = os.path.join(BASEPATH, "config", "MysqlConfig.yaml")

    CaseConfig = os.path.join(BASEPATH, "config", "CaseConfig.yaml")



if __name__ == "__main__":
    #print(path.MysqlConfig)
    pass
