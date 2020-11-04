import requests

class HttpUtil():
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def get(self, path, params={}, timeout=30, headers={}):
        url = self.baseURL + path
        try:
            r = requests.get(url, params=params, timeout=timeout, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ''

    def post(self, path, data={}, timeout=3, headers={}):
        url = self.baseURL + path
        try:
            r = requests.post(url, data, timeout=timeout, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ''

if __name__ == '__main__':
    http = HttpUtil('http://314552t5k2.goho.co/index.php/admin/')
    data = {'username': 'admin', 'password': 'admin'}
    result = http.post('login', data=data)
    # print(result)
    token = eval(result)['data']['token']
    headers = {'Authorization': token}
    params = {'id': 1}
    result = http.get('users', params=params, headers=headers)
    print(result)