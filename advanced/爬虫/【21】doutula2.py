import requests
from urllib import request
from lxml import etree
from queue import Queue
import threading
import re
import os


class Producer(threading.Thread):
    def __init__(self, queue_url: Queue, queue_img: Queue, *args, **kwargs):
        # 注意继承的写法
        super(Producer, self).__init__(*args, **kwargs)
        self.queue_url = queue_url
        self.queue_img = queue_img

    def run(self):
        while True:
            if self.queue_url.empty():
                break
            # 生产者主要功能：从url队列中取出待爬取url，并解析，获取图片数据，存放到img队列中
            url = self.queue_url.get()

            # 解析url，并整理新的数据("img_url","img_name")放入新的队列 self.queue_img中
            self.parse_page(url)

    def parse_page(self, url):
        # url = 'https://www.doutula.com/photo/list/?page={}'.format(page)
        response = requests.get(url)
        html = etree.HTML(response.text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")

        # 判断是否存在imgs文件夹
        if not os.path.exists('./imgs'):
            os.mkdir('imgs')

        for img in imgs:
            name = img.get('alt')
            # 替换图片名称中的特殊字符
            name = re.sub(r'[\?？\.。!！\*]', '', name)
            img_url = img.get('data-original')
            suffix = str(img_url).rsplit('.', maxsplit=1)[-1]
            filename = name + '.' + suffix
            # 将 准备好的数据，放入新的队列中，供消费者使用
            self.queue_img.put((img_url, filename))


class Consumer(threading.Thread):
    def __init__(self, queue_url: Queue, queue_img: Queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.queue_url = queue_url
        self.queue_img = queue_img

    def run(self):
        while True:
            if self.queue_img.empty() and self.queue_url.empty():
                break
            # 消费者主要功能：img队列中读取图片信息，并将其下载到本地
            img_url, filename = self.queue_img.get()
            request.urlretrieve(img_url, filename='imgs/' + filename)
            print(img_url + ' 下载完成!')


def main():
    # 存放待爬取url的队列
    queue_url = Queue(100)
    # 存放待下载图片的队列
    queue_img = Queue(68 * 10)

    # 将 待请求的url放入队列中
    for i in range(1, 10):
        url = 'https://www.doutula.com/photo/list/?page={}'.format(i)
        queue_url.put(url)

    # 多个生产者同时工作
    for i in range(5):
        p1 = Producer(queue_url, queue_img)
        p1.start()

    print('-' * 100)

    # 多个消费者同时工作
    for i in range(5):
        c1 = Consumer(queue_url, queue_img)
        c1.start()

    print('-' * 100)


if __name__ == '__main__':
    main()
