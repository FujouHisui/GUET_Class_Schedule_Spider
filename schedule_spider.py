import requests
from bs4 import BeautifulSoup

sessions = requests.session()
res = requests.get("http://bkjw2.guet.edu.cn/student/public/login.asp")


def login():
        url = 'http://bkjw2.guet.edu.cn/student/public/login.asp'
        form_data = {
            'username': username,  # 学号
            'passwd': password,   # 密码
            'login': '%B5%C7%A1%A1%C2%BC'
        }
        header = {
            'Host': 'bkjw2.guet.edu.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://bkjw2.guet.edu.cn/student/public/login.asp',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.48 Safari/537.36 Edg/74.1.96.24',
            'Upgrade-Insecure-Requests': '1'
        }
        print("正在登陆教务系统...")
        response = sessions.post(url, data=form_data, headers=header)
        print("服务器响应码:",response.status_code)
        if response.status_code == requests.codes.ok:
            print("成功进入教务系统！")
        # with open(r'C:\Users\Hisui\Desktop\get.txt', 'wb') as f:
        #    f.write(response.content)


def get_cookie():
        res = requests.get("http://bkjw2.guet.edu.cn/student/public/login.asp")
        cookie_jar = requests.cookies.RequestsCookieJar()
        for cookie in res.cookies:
            cookie_jar.set(cookie.name,cookie.value)
        # for cookie in res.cookies:
        #    print(cookie.name+"\t"+cookie.value)
        return cookie_jar


def get_schedule(cookie_jar):
        url2 = 'http://bkjw2.guet.edu.cn/student/coursetable.asp'
        form_data2 = {
            'term': '2018-2019_2'
        }

        header = {
            'Host': 'bkjw2.guet.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'http://bkjw2.guet.edu.cn/student/selectterm.asp',
            'Connection': 'keep-alive',
        }
        print("正在获取课表...")
        response = sessions.post(url2, headers=header, data=form_data2, cookies=cookie_jar)
        print("服务器响应码:",response.status_code)
        if response.status_code == requests.codes.ok:
            print("成功获取到课表！")
        save_path = r'C:\Users\Hisui\Desktop\get_schedule.html'
        content = response.content
        with open(save_path, 'wb') as g:
            g.write(response.content)
        print("您的课表已保存到"+save_path)


print("欢迎使用桂林电子科技大学课表获取脚本")
print("请输入学号")
username = input(str)
print("请输入密码")
password = input(str)
login()
get_schedule(get_cookie())
response = requests.get("http://bkjw2.guet.edu.cn/student/public/logout.asp")
print("已登出教务系统")
