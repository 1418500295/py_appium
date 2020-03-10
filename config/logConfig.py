import logging
import sys


class LogConfig():

    def get_log(self):
        # 创建一个日志器logger并设置其日志级别为DEBUG
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.DEBUG)
        # 将结果写入日志文件
        handler = logging.FileHandler("../report/app.log", encoding="utf-8")
        # 创建一个流处理器handler并设置其日志级别为DEBUG
        handler.setLevel(logging.DEBUG)

        # 创建一个格式器formatter并将其添加到处理器handler
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        # # 将日志输出到控制台

        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        # 为日志器logger添加上面创建的处理器handler
        logger.addHandler(handler)
        logger.addHandler(console)

        return logger

