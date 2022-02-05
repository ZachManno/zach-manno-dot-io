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
