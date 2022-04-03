const AWS = require("aws-sdk");

const dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json",
    "X-Custom-Header": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, PATCH, DELETE",
    "Access-Control-Allow-Headers": "X-Requested-With,content-type"
  };

  try {
  console.log('Event: ', event);
    switch (event.routeKey) {
      case "DELETE /count":
        await dynamo
          .delete({
            TableName: "zachmanno-dot-io-traffic-count",
            Key: {
              id: event.pathParameters.id
            }
          })
          .promise();
        body = `Deleted item ${event.pathParameters.id}`;
        break;
//      case "GET /count/{id}":
//        body = await dynamo
//          .get({
//            TableName: "zachmanno-dot-io-traffic-count",
//            Key: {
//              id: event.pathParameters.id
//            }
//          })
//          .promise();
//        break;
      case "GET /count":
      console.log("here1")
        body = await dynamo
          .scan({ TableName: "zachmanno-dot-io-traffic-count" })
          .promise();
        break;
      case "PUT /count/increment":
        let requestJSON = JSON.parse(event.body);
        console.log("Got request to put items. Id: ", requestJSON.id, "count: ", requestJSON.number)

        currentCountBody = await dynamo
          .scan({ TableName: "zachmanno-dot-io-traffic-count" })
          .promise();

        currentCount = currentCountBody.Items[0].count;

        await dynamo
          .put({
            TableName: "zachmanno-dot-io-traffic-count",
            Item: {
              id: requestJSON.id,
              count: currentCount + requestJSON.number
            }
          })
          .promise();
        body = `Put item ${requestJSON.id}`;
        const updatedCount = {
            server: currentCountBody.Items[0].id,
            count: currentCount + requestJSON.number
        }
        body = updatedCount;
        break;
      default:
        console.log("here2")
        throw new Error(`Unsupported route: "${event.routeKey}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }

  return {
    statusCode,
    body,
    headers
  };
};

