# Node Dynamo DB Lambda Function
Lambda function that makes Dynamo DB calls to get and update the Zach Manno Dot IO webserver traffic count

### To Deploy
```shell
sam build
sam deploy
```

### To Get the Current Count
https://9mzlqvh22e.execute-api.us-east-1.amazonaws.com/count

### To increment the count by desired number
```shell
curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"mainwebservercount\", \"number\": 1}" https://9mzlqvh22e.execute-api.us-east-1.amazonaws.com/count/increment
```