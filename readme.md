# **Project Result:**



## 1- deploy by Docker:

###   1-1 redis: store async predict data 
  
###   1-2 celery: submit async predict task
  
###   1-3 web service: provide restful api 

deploy result is below: 


<img width="1495" alt="截屏2025-03-31 17 38 47" src="https://github.com/user-attachments/assets/211ac311-fd06-4cca-a014-ec955cffa67e" />

## 2- curl test result :


 2.1- sync api tested by curl 
```
(base) yuanxiaomin@yuanxiaomindeMacBook-Pro ~ % curl -X POST http://127.0.0.1:8000/titanic_sync/ \ 
  -H "Content-Type: application/json" \
  -d '{
    "Pclass": 3,
    "Sex": "female",
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "C"
  }'
{"probability": 0.9393930219871116}% 

```

  2-2-  async api tested by curl 
  
```
(base) yuanxiaomin@yuanxiaomindeMacBook-Pro ~ % curl -X POST http://127.0.0.1:8000/titanic_async/ \
  -H "Content-Type: application/json" \
  -d '{
    "Pclass": 3,
    "Sex": "female",
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "C"
  }'
{"job_id": "4285cca2-3560-4c62-b9c9-6b9d6fb9e1c8"}%
```

2-3: acquire async predict result 
  ```
(base) yuanxiaomin@yuanxiaomindeMacBook-Pro ~ % curl -X GET http://127.0.0.1:8000/titanic_result/4285cca2-3560-4c62-b9c9-6b9d6fb9e1c8/
{"status": "success", "result": 0.9393930219871116}% 
  ```



# Project Introduction 


## 1- project Restful api:
 i developed 3 restful api :
 
 1- http://127.0.0.1:8000/titanic_sync/    : used for calculate predicion by sync;
 
 2- http://127.0.0.1:8000/titanic_async/   : used for calculate predition by async, and will return job_id immediately, and result will be storaged in redis;
 
 3- http://127.0.0.1:8000/titanic_result/{job_id}/ : used for acquiring prediction that calculated by async api in job id;

 

## 2- project structure:

titanic_project/model: train model and save model;

titanic_project/task:  used for async calculation;

titanic_project/utils: used for data process and model prediction.




# Project build and deploy

## 1- Train model

```
python titanic_project/model/generate_model.py
```

## 2- build by docker
```
docker-compose build

docker-compose up
```


