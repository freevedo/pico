let mess;
// Create a client instance
var hostname = "82.165.23.150";
var port = 9001;
var clientId = "testmqtt";
client = new Paho.MQTT.Client(hostname, port, clientId);

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({
  onSuccess: onConnect,
  userName: "client1",
  password: "client1",
});

// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("serreLaafi2");
  message = new Paho.MQTT.Message("Hello");
  message.destinationName = "serreLaafi";
  client.send(message);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:" + responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  let values = JSON.parse(message.payloadString);

  console.log("onMessageArrived:" + message.payloadString);
  let pico = document.getElementById("picow");
  let ds18b20 = document.getElementById("ds18b20");
  let dht11Temp = document.getElementById("dht11Temp");
  let dht11Hum = document.getElementById("dht11Hum");
  pico.innerHTML = values["picoTemp"] + " &#8451;";
  ds18b20.innerHTML = values["digitalTemp"] + " &#8451;";
  dht11Temp.innerHTML = values["dht11Temp"] + " &#8451;";
  dht11Hum.innerText = values["dht11Hum"] + "%";
}
