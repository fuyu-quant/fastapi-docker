# fastapi-docker
<img src="image/FastAPI.png" width="400">
FastAPI dokcer

## Contents
* [Basic docker operations](#basic-docker-operations)
* [FastAPI](#fastapi)
* [Reference](#reference)



## [Basic docker operation](https://github.com/fuyu-quant/dockerfile-for-data-scientists)



## FastAPI

### 起動方法
* コンテナ立ち上げ時に起動
以下のコードをDockerfileに追記
```bash
COPY main.py /root
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8040"]
```

* コマンドによる起動
```bash
docker-compose exec fastapi bash
cd src
uvicorn main:app --reload --host 0.0.0.0 --port 8040
```
* アクセス先
    * http://127.0.0.1:8040/



### Automatic Document Generation
- SwaggerUI
    - http://127.0.0.1:8040/docs
- redoc
    - http://127.0.0.1:8040/redoc



## Reference
* https://buildersbox.corp-sansan.com/entry/tech18_container  
* https://qiita.com/Brutus/items/3133766e14f11d269933