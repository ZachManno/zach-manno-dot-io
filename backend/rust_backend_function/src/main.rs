use lambda_runtime::{service_fn, LambdaEvent, Error};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let func = service_fn(func);
    lambda_runtime::run(func).await?;
    Ok(())
}

async fn func(event: LambdaEvent<Value>) -> Result<Value, Error> {
    let (event, _context) = event.into_parts();
    let first_name = event["firstName"].as_str().unwrap_or("world");

    Ok(
        json!(
            { "message": format!("Weather is {}", "here!") }
        )
    )
}

async fn call_weather_api() -> Result<Response, Error> {
    // Build the client using the builder pattern
    let client = reqwest::Client::new();

    // Perform the actual execution of the network request
    let response = client
        .get("https://api.openweathermap.org/data/2.5/weather?\
            appid=dcafd716328a8a378ffa82beeaedae52\
            &q=Philadelphia%2CUSA&units=imperial")
        .header("Accept", "application/json, text/plain, */*")
        .header("Referer", "https://magiceden.io/")
        .header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
        .send().await;

    return response;
}