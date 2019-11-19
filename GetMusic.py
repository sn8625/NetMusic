import requests
from lxml import html
import logging
from datetime import datetime

class GetMusicNet(object):
    def __init__(self, url, songpath):
        self.url = url
        self.songpath = songpath

    def DownMusic(self):
        # 生成日志文件
        logging.basicConfig(level=logging.INFO, filename=self.songpath + '/log.txt')

        # 请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

        # 确定URL
        logging.info('【%s】 - 开始解析地址！'% datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # self.LoadLog()
        # print('开始解析地址！')
        gurl = self.url
        murl = gurl.replace('/#/', '/')

        # 外链URL
        base_url = 'https://link.hhtjim.com/163/'

        # 请求
        logging.info('【%s】 - 开始请求地址！'% datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # self.LoadLog()
        result = requests.get(murl, headers=headers).text

        # 筛选数据
        logging.info('【%s】 - 开始解析数据！'% datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # self.LoadLog()
        # print('开始解析数据！')
        dom = html.etree.HTML(result)
        names = dom.xpath('//ul[@class="f-hide"]/li/a/text()')
        ids = dom.xpath('//ul[@class="f-hide"]/li/a/@href')
        # titles = dom.xpath('//ul[@class="f-hide"]/li/b/@title')
        # print(titles)

        # 下载歌曲
        # 获取歌名和歌曲ID
        for num in range(0, len(names)):
            music_name = names[num]
            music_id = ids[num].strip('/song?id=')
            # music_title = titles[num]
            # print(music_name, music_id, music_title)

            music_url = base_url + music_id + '.mp3'
            file_name = music_name + '.mp3'

            logging.info('【%s】 - 开始下载歌曲%s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), file_name))
            # self.LoadLog()
            # print('开始下载歌曲%s' % file_name)
            song = requests.get(music_url).content

            with open('%s/%s' % (self.songpath,file_name), 'wb') as file:
                file.write(song)
                logging.info('【%s】 - 歌曲%s下载完成！' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), file_name))
                # self.LoadLog()
                # print('歌曲%s下载完成！' % file_name)