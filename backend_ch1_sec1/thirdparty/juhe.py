import requests
import json

def weather(cityname):
    '''
    :param cityname:
    :return:天气情况
    '''
    #
    # key = '9a3e1fa6cb79d69f1594af5cb219a469'
    key = 'fe9121d3dd9d008e61af30524bb10e10'
    # api = 'http://v.juhe.cn/weather/index'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' +params
    # print(url)
    # response = requests.get(url=url)
    # print(response.text)
    # print(type(response.text))
    # json_data = json.loads(response.text)#把接口返回数据load为json
    # result = json_data.get('result')
    # print(result)
    # sk = result.get('realtime')
    text = '{"temperature": "23", "humidity": "60", "info": "多云", "wid": "01", "direct": "东风", "power": "4级", "aqi": "58"}'
    sk = json.loads(text)
    print(sk)
    response = dict()
    response['temperature'] = sk.get('temperature')
    print(sk.get('temperature'))
    response['info'] = sk.get('info')
    response['power'] = sk.get('power')
    response['direct'] = sk.get('direct')
    response['humidity'] = sk.get('humidity') # 湿度
    response['aqi'] = sk.get('aqi')

    return response

if __name__  ==  '__main__':
    data = weather('南京')