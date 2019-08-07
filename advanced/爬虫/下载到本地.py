import os
# from six.moves import urllib
import sys
import urllib

DATA_URL = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
filename = DATA_URL.split('/')[-1]


def _progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> Downloading %s %.1f%%' % (filename,
                                                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()


filepath, _ = urllib.request.urlretrieve(DATA_URL, filename, _progress)
print()
