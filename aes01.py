# -*- coding:utf-8 -*-
from flask import Flask
from numpy import pad

from encrypt import prpcrypt
import base64

from Crypto import Random
from Crypto.Cipher import AES
app = Flask(__name__)


@app.route('/')
def hello_world():
    # aes = prpcrypt("1234567890123456")
    # encode = aes.encrypt("a")
    # print ("encode:"+encode)
    #
    # decode = aes.decrypt("2CYdnm+7gvCxxiXvwgZKsA==")
    # print ("decode:"+decode)

    # bkey = "1234567890123456"
    # print(bkey)
    # raw = "a"
    #
    # iv = "0102030405060708";
    # print("iv=" + iv)
    # cipher = AES.new(bkey, AES.MODE_CBC, iv)
    # ciphertext = cipher.encrypt(raw)
    # print(ciphertext)

    iv = "0102030405060708"
    pc = prpcrypt('1234567890123456', iv)  # 初始化密钥 和 iv
    import sys

    e = pc.encrypt('a')  # 加密 + base64



    d = pc.decrypt(e)  # 解密 +deBase64
    print "加密:", e
    print "解密:", d
    print "长度:", len(d)
    return 'Hello World!!'


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True, port=8889)
