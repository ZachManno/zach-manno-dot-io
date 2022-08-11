# Rust Lambda API
Followed instructions here for startup:

https://github.com/awslabs/aws-lambda-rust-runtime


To deploy:


```shell
cargo zigbuild --release --target aarch64-unknown-linux-gnu

cp ./target/aarch64-unknown-linux-gnu/release/rust_backend_function ./build/bootstrap

sam deploy --parameter-overrides WeatherApiKey=the_key
```
To deploy locally:
```shell
sam local start-api --parameter-overrides WeatherApiKey=the_key

curl --request GET --url 'http://127.0.0.1:3000/weather' 
```

To test:
```shell
# Call directly:
aws lambda invoke  --cli-binary-format raw-in-base64-out \
  --function-name sam-app-HelloWorldFunction-ft3RDw5Whbua \
  --payload '{"firstName": "Zach"}' \
  output.json

# Or call via API gateway (url is an output of sam deploy, it can change)
curl --request GET --url 'https://ml20kezqk5.execute-api.us-east-1.amazonaws.com/weather'
```
