#encoding:utf-8
# -*- coding:utf-8 -*-
from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES
import base64

class prpcrypt():
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        # 补位
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, text):
        text = self.pad(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 目前AES-128 足够目前使用
        ciphertext = cryptor.encrypt(text)
        # 把加密后的字符串转化为16进制字符串
        # return b2a_hex(ciphertext)
        return base64.b64encode(ciphertext)
        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt(self, text):
        str = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        # plain_text = cryptor.decrypt(a2b_hex(text))
        plain_text = cryptor.decrypt(str)
        return self.unpad(plain_text.rstrip('\0'))