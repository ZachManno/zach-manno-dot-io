# zach-manno-dot-io
Zach Manno's personal website!

## Steps to Get Started
```commandline
brew install node

npm install -g serverless

serverless create -t hello-world -n zach-manno-io -p zachmanno.io

cd zachmanno.io

serverless plugin install -n serverless-s3-sync

```

## To install HTML Bootstrap Template
Source - https://github.com/StartBootstrap/startbootstrap-blog-home
```shell
cd template

npm i startbootstrap-blog-home

npm install
npm start # This shows the site in your local
npm run build
cp -R dist/ ../static/ # Copy to static S3 folder
cd ../
serverless deploy
```

# CDN Deploy
`aws cloudformation create-stack --stack-name cloudfront-distribution-deploy --template-body file://cft/cft.yml`

`aws cloudformation update-stack --stack-name cloudfront-distribution-deploy --template-body file://cft/cft.yml`

# Resources
Use OAI - https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/

# Utility Script to Create a New Blog Post
To create a new blog post, a new blog HTML file must be created and the blog.html and index.html
files need to be updated. The generate_new_blogpost.py script does this automatically. To use:

- cd to the `scripts` directory
- Download the blog header image you want to include for this blog and copy it to this scripts directory
- Run the python script in the scripts directory giving the date and blog header:
    - `python3 generate_new_blogpost.py --post-date 2022-03-27 --post-title "Generating A New Blogpost" --post-header-image new-blogpost-sample-pic.jpeg`
    - see `usage` in the generate_new_blogpost.py script for usage details
- Edit the html files to fill in the last details (look for "TODO"s that were generated)

# Blog Styling Examples

### List
```
<ul class="fs-5 mb-4">
    <li> Create an AWS account and download the AWS CLI</li>
    <li> Install the <a href="https://www.serverless.com/">Serverless Framework</a> to deploy an S3
        bucket
    </li>
</ul>
```

### Code Block
For any code block add the [syntax highlighting library](https://highlightjs.org/usage/) 
to the html:
```
<link rel="stylesheet"
      href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/default.min.css">
<script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
```

It will autohighlight any code but if you want to specify a language, add a class with one 
of the [supported languages](https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md) 

Python code block:
```
    <pre>
        <code class="language-python">

import time
# Comment
scoreboard_index = 0
while True:
    time.sleep(2)
       </code>
    </pre>
```

Yaml code block:
```
   <pre>
       <code class="language-yaml">

# The `provider` block defines where your service will be deployed
provider:
  name: aws
  runtime: nodejs12.x

resources:
  Resources:

plugins:
  - serverless-s3-sync

custom:
  siteName: zachmanno.io
  s3Sync:
    - bucketName: ${self:custom.siteName}
      localDir: static

      </code>
   </pre>
```

# Serverless Rust API
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


