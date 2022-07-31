#!/usr/bin/env bash

# USAGE:
# To SAM deploy to local:
# ./build_deploy.sh 9b49d5c002ebf33cb9a996e8a465af03 local
#
# To SAM deploy to prod:
# ./build_deploy.sh 9b49d5c002ebf33cb9a996e8a465af03 prod
#
# To invalidate Cloudfront cache after SAM deploying
# ./build_deploy.sh 9b49d5c002ebf33cb9a996e8a465af03 prod invalidate

cargo zigbuild --release --target aarch64-unknown-linux-gnu
cp ./target/aarch64-unknown-linux-gnu/release/rust_backend_function ./build/bootstrap
echo "weather api key: $1";
#sam local start-api --parameter-overrides WeatherApiKey=$1
if [[ $2 = local ]] ; then
  echo "SAM deploying to local"
  sam local start-api --parameter-overrides WeatherApiKey="$1" > /dev/null 2>&1 &
  process_id=$!
  echo "Test the API here:"
  echo "http://127.0.0.1:3000/weather"
  echo "Command to kill:"
  echo "kill $process_id"
else
  echo "SAM deploying to prod"
  sam deploy --parameter-overrides WeatherApiKey="$1"
fi

if [[ $3 = invalidate ]] ; then
  echo "Invalidating cloudfront"
  aws cloudfront create-invalidation --distribution-id E17KDNZ2L2XBX1 --paths "/*"
fi

