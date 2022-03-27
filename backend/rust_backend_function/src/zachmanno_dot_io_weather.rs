use serde_derive::Deserialize;
use serde_derive::Serialize;

#[derive(Default, Debug, Deserialize, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct ZachMannoDotIoWeatherResponse {
    pub temp: String,
    #[serde(rename = "iconUrl")]
    pub icon_url: String,
    #[serde(rename = "errMsg")]
    pub err_msg: String,
}