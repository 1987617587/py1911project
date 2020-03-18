import time

from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature

# 带有时间限制 expires_in+时间秒数
id = 1001

# 序列化
seria_util = TimedJSONWebSignatureSerializer("hellopy1911", expires_in=3)
serstr = seria_util.dumps({"id": id}).decode("utf-8")
print(serstr)
time.sleep(5)
# 反序列化
try:
    seria_util = TimedJSONWebSignatureSerializer("hellopy1911")
    obj = seria_util.loads(serstr)
    print(obj)
    print(obj["id"])
except SignatureExpired as e:
    print(e, "过期了")
except BadSignature as e:
    print(e, "密钥错误")
