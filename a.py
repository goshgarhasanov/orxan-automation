import base64
ss=open('cpyoxl.png','rb')
aa=ss.read()
sonEncode=base64.b64encode(aa).decode('utf-8')
print(sonEncode)

'''

'''