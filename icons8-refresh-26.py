import base64
with open("icon.py",'a') as f:
    f.write(f"refreshicon={base64.b64encode(open('icons8-refresh-26.png','rb').read())}")