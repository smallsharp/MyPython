from basic.fileRW.parseProp.parseTest import ReadConfig
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

ids = PATH('./parseProp/ids.prop')

config = ReadConfig(ids)

print(config.getValue('login', 'user'))
