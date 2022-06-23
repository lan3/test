import requests

'''
发送接口
'''


# get请求方法
def send_get(url, params, headers):
    response = requests.get(url=url, params=params, headers=headers)
    return response


# post请求方法
def send_post(url, params, headers):
    response = requests.post(url=url, json=params, headers=headers)
    return response


# 根据不同请求方式判断调用的方法
def send_requests(method, url, params, headers):
    if method == 'GET':
        try:
            response = send_get(url, params, headers)
            print("已调用接口。")
            return response
        except Exception as e:
            print("接口调用失败！错误信息为：", e)
    elif method == 'POST':
        try:
            response = send_post(url, params, headers)
            print("已调用接口。")
            return response
        except Exception as e:
            print("接口调用失败！错误信息为：", e)

    else:
        print("请求方式错误！")
