# coding:utf-8
import logging
import os
import sys  
sys.path.append("../")
basepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
logconfigpath = basepath + "/BaseConfig"+"/LogConfig.yaml"
logdatapath = basepath + "/log"

from common.ReadConfig import Config
from logging.handlers import TimedRotatingFileHandler


class MyLogger(object):
    def __init__(self, logger_name="运行日志"):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config(logconfigpath).get("log")
        # 日志输出名字
        self.logname = c.get('file_name') if c and c.get('file_name') else 'test.log'
        self.logger_error = c.get('file_name_error') if c and c.get('file_name_error') else 'error.log'
        # 保留的日志数量
        self.backup_count = c.get('backup') if c and c.get('backup') else 5
        """ 控制日志输出级别 """
        # 输出到控制台
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'DEBUG'
        # 输出到日志文件中
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'  # 运行文件
        self.file_output_level_error = c.get('file_level_error') if c and c.get('file_level_error') else 'ERROR'
        # 控制日志输出格式
        # 输出到文件中的格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s-s-%(levelname)s-%(message)s'
        self.formatter = logging.Formatter(pattern)
    # 输出到控制台的格式
        con_pattern = c.get('con_pattern') if c and c.get('con_pattern') else '%(asctime)s-%(levelname)s-%(message)s'
        self.formatters = logging.Formatter(con_pattern,datefmt='%Y-%m-%d %H:%M:%S')


    def get_logger(self):
        if not self.logger.handlers:
            # 控制台输出
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatters,)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(logdatapath, self.logname),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler_error = TimedRotatingFileHandler(filename=os.path.join(logdatapath, self.logger_error),
                                                          when='D',
                                                          interval=1,
                                                          backupCount=self.backup_count,
                                                          delay=True,
                                                          encoding='utf-8'
                                                          )
            # 输入到日志文件
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            # ---------------报错文件
            file_handler_error.setFormatter(self.formatter)
            file_handler_error.setLevel(self.file_output_level_error)
            self.logger.addHandler(file_handler_error)
        return self.logger
logger = MyLogger().get_logger()


if __name__=="__main__":
    logger.warning("hdkfdk")


