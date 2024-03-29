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
`aws cloudformation create-stack --stack-name cloudfront-distribution-deploy --template-body file://cft/cloudfront_cft.yml`

`aws cloudformation update-stack --stack-name cloudfront-distribution-deploy --template-body file://cft/cloudfront_cft.yml`

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

# Steps to Install a Serverless Framework Python API
I started this then deleted it. But saving these steps for the future


To install:
```shell
cd zachmanno.io
npm install --save-dev serverless-wsgi serverless-python-requirements
npm install --save-dev serverless-dynamodb-local
brew install virtualenv
brew update && brew upgrade pyenv
pyenv install 3.8.9
pyenv virtualenv 3.8.9 zach-manno-dot-io
# check which virtualenvs you have installed
pyenv virtualenvs
pyenv activate zach-manno-dot-io
# to deactivate
# pyenv deactivate
pip3 install flask
pip3 install boto3
pip3 freeze > requirements.txt
```

# Check 'backend' folder for Serverless Rust Weather API and Node Page Views API


