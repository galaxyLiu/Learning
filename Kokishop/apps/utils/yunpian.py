#!/user/bin/env python
# -*- coding:utf-8 -*-


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            'api_key': self.api_key,
            'mobile': mobile,
            'text': '【刘慧】您的验证码是{}。如非本人操作，请忽略本短信'.format(code)
        }


if __name__ == '__main__':
    yun_pian = YunPian("")
    yun_pian.send_sms('2021','')
