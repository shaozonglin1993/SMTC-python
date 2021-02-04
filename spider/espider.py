
from bs4 import BeautifulSoup
import requests


url = 'https://blog.csdn.net/tom942067059'


def getSoup(target_url):
    # 定制请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    #尝试获取网页信息，r为Response对象
    r = requests.get(target_url, headers=headers)

    #返回码
    sc = r.status_code
    print(sc)

    # 设置编码格式
    r.encoding = 'utf-8'

    # 网页内容
    context = r.text
    
    # 解析网页
    soup = BeautifulSoup(context, 'lxml')
    return soup


def getContext():
    soup = getSoup(url)

    # 获取<div class='info clear'></div>所有标签项
    h = soup.find_all('div', class_='article-item-box csdn-tracking-statistics')
    #print(h)

    for item in h:
        # get blog URL
        label_url = item.find('a', class_='')
        the_url = label_url.attrs['href']
        print('URL: '+the_url)
        # get blog name
        label_name = item.find('h4', class_='')
        the_name = label_name.text
        print(the_name)

        # get blog publishe time
        label_time = item.find('div', class_='info-box d-flex align-content-center')
        time = label_time.find('span', class_='date')
        the_time = time.text
        print('发布时间：' +the_time)

        # get the read number
        read_num = label_time.find('span', class_='read-num')
        the_read_num = read_num.text
        print('访 问 量：'+the_read_num)
        print('-----------------------------------------------------------------')



if __name__ == "__main__":
    getContext()


 
