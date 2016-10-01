import requests
import os.path
class ScrapyBaicizhan():
    def __init__(self, base_url, word_list_path):
        self.base_url = base_url
        self.word_list_path = word_list_path

    def scrapy(self):
        with open(word_list_path, 'r') as f:
            words = f.readlines()
            count = 0
            for word in words:
                word = word.strip('\n')
                if self.word_exsits(word):
                    continue
                urls = self.get_urls(word)
                for url in urls:
                    if self.word_exsits(word):
                        break
                    r = requests.get(url)
                    if r.status_code == 200:
                        with open('videos/%s.mp4' % word, 'wb+') as f:
                            count += 1
                            print("collect %s words" % count)
                            f.write(r.content)
                        break
                    else:
                        continue
            with open('count.txt', 'wa+') as f:
                f.write("collect %s videos of words" %count)

    def get_urls(self, word):
        return_list = []
        add_before = ["music", "noun", "real", "leng"]
        for i in add_before:
            return_list.append(self.base_url + i + '_' + word + '.mp4')
        return return_list
    
    def word_exsits(self, word):
        return os.path.isfile("videos/" + word + '.mp4')

if __name__ == '__main__':
    base_url = "http://ali.baicizhan.com/word_tv/"
    word_list_path = "words.txt"
    scrapy = ScrapyBaicizhan(base_url, word_list_path)
    # url = scrapy.get_urls("seek")
    # r = requests.get(url[-1])
    # print(r.content)
    # print(scrapy.word_exsits("hello"))
    scrapy.scrapy()
    # r=requests.get("http://ali.baicizhan.com/word_tv/leng_seek.mp4")
    # print(r.status_code)