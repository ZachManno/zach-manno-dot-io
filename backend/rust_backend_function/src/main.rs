mod weather;
mod lambda_gateway;

use lambda_runtime::{service_fn, LambdaEvent, Error};
use serde_json::{json, Value};
use std::env;
use std::future::Future;
use reqwest::{Error as req_err, Response};
use crate::weather::WeatherResponse;
use crate::lambda_gateway::{LambdaResponse, LambdaResponseBuilder};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let func = service_fn(func);
    lambda_runtime::run(func).await?;
    Ok(())
}

async fn func(event: LambdaEvent<Value>) -> Result<LambdaResponse, Error>  {
    let (event, _context) = event.into_parts();
    //let first_name = event["firstName"].as_str().unwrap_or("world");
    let weather_api_key = env::var("API_KEY").unwrap();
    let weather_data = call_weather_api(&weather_api_key).await;

    let temp = match weather_data {
        Ok(data) => match data.json::<WeatherResponse>().await {
            Ok(json_parsed_response) => (format!("{}", json_parsed_response.main.temp)),
            Err(json_error) => {
                println!("Problem calling weather api (json parse): {:?}", json_error);
                String::from("")
            }
        },
        Err(error) => {
            println!("Problem calling weather api: {:?}", error);
            String::from("")
        }
    };

    let response = LambdaResponseBuilder::new()
        .with_status(200)
        .with_header("Content-Type", "application/json")
        .with_header("X-Custom-Header", "application/json")
        .with_header("Access-Control-Allow-Origin", "*")
        .with_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, PATCH, DELETE")
        .with_header("Access-Control-Allow-Headers", "X-Requested-With,content-type")
        .with_json(json!(
            {
                "temperature": format!("{}", temp),
                "description": format!("{}", "d"),
                "location": format!("{}", "Philadelphia")
            }
        ))
        .build();

    Ok(response)
}

async fn call_weather_api(api_key: &str) -> Result<Response, reqwest::Error> {
    // Build the client using the builder pattern
    let client = reqwest::Client::new();

    // Perform the actual execution of the network request
    let response = client
        .get(format!("https://api.openweathermap.org/data/2.5/weather?\
            appid={}\
            &q=Philadelphia%2CUSA&units=imperial", api_key))
        .send().await;

    return response;
}