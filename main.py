import requests
from lxml import etree
import lxml


def get_url(parms):
    url = "https://www.baidu.com/s?ie=UTF-8&wd=" + parms
    return url


def status_out(res):
    '''返回请求网址的各种信息'''
    # 打印请求网址
    print("请求网址 ：", res.url)
    # 打印访问状态
    print("访问状态 :", res.status_code)
    # 打印网页编码
    print("网页编码 :", res.encoding)
    # 打印请求头
    #print("请求头 :\n", res.headers)
    # 打印 cookies
    #print("cookies :", res.cookies)
    # print(res.text)



if __name__=='__main__':

    #设置请求头
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/87.0.4280.141 Safari/537.36',
        "Accept" : 'text/html,application/xhtml+xml,application/xml;\
            q=0.9,image/avif,image/webp,image/apng,*/*;\
            q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'zh-CN,zh;q=0.9',
        "Connection": 'keep-alive'
    }
    #获取网址
    v = input('输入要查询的内容： \n')
    url = get_url(v)
    # 请求网址
    r = requests.get(url,headers=headers)
    selector = lxml.etree.HTML(r.text)

    #打印请求状态
    status_out(r)

    key = []
    value = []
    for i in range(1,11):
        title = selector.xpath('//div[@id="%d"]//h3//text()'%i)
        href = selector.xpath('//div[@id="%d"]/h3//@href'%i)
        key.append(''.join(title).strip())
        value.append(''.join(href))

    d = dict(zip(key,value))
    for k,v in d.items():
        print(k,v)

