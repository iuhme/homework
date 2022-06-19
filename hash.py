import hashlib
def hash():
    h=input("输入要哈希的值：")
    value=hashlib.md5(h.encode("utf-8")).hexdigest()
    print(value)