from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def print1():
    print("hollow")
    return "11"
# python 异步
# 大模型接口协议 ss1
# 后端工程化
# ai工具 code-x 

