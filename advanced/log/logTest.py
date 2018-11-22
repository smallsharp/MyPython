import logging

# 普通用法

# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）

# logging.debug('this is a debug message!')
# logging.info('this is a info message!')
# logging.warning('this is a warning message!')
# logging.error('this is a error message!')
# logging.critical('this is a critical message!')


# 配置用法
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
#                     )
# logging.debug('this is a debug message!')
# logging.info('this is a info message!')
# logging.warning('this is a warning message!')
# logging.error('this is a error message!')
# logging.critical('this is a critical message!')


# 输出日志到文件
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "# 配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' # 配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"test.log" # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )
logging.debug('this is a debug message!')
logging.info('this is a info message!')
logging.warning('this is a warning message!')
logging.error('this is a error message!')
logging.critical('this is a critical message!')


# https://www.cnblogs.com/Nicholas0707/p/9021672.html