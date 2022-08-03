using MQTTnet.Client;
using MQTTnet;
using Newtonsoft.Json;

namespace Monitoring
{
    public static class Program
    {
        public static void Main(String[] args)
        {
            var mqttFactory = new MqttFactory();

            string? address = Environment.GetEnvironmentVariable("BROKER_ADDRESS"),
                topic = Environment.GetEnvironmentVariable("BROKER_TOPIC"),
                deviceAddress = Environment.GetEnvironmentVariable("DEVICE_ADDRESS");
            if (address == null)
                address = "127.0.0.1";
            if (topic == null)
                topic = "edgex-tutorial";
            if (deviceAddress == null)
                deviceAddress = "http://127.0.0.1:48082/api/v1/device/name/SmartHouseProject/command/color";

            var mqttClient = mqttFactory.CreateMqttClient();

            var mqttClientOptions = new MqttClientOptionsBuilder()
                .WithTcpServer(address)
                .Build();

            mqttClient.ApplicationMessageReceivedAsync += e =>
            {
                string s = System.Text.Encoding.UTF8.GetString(e.ApplicationMessage.Payload);
                SensorDataMessage m = JsonConvert.DeserializeObject<SensorDataMessage>(s);

                string color = "";
                if(m.Readings?.Count > 0)
                    color = Evaluate(m.Readings[0]);
                if (!String.IsNullOrEmpty(color))
                {
                    Console.Write(color + "\t");
                    HttpClient client = new HttpClient();
                    HttpResponseMessage rm = client.PutAsync(deviceAddress,
                            new StringContent(JsonConvert.SerializeObject(
                                new
                                {
                                    color
                                }),
                                System.Text.Encoding.UTF8,
                                "application/json")).Result;
                    Console.WriteLine(rm.Content.ReadAsStringAsync().Result);
                }

                return Task.CompletedTask;
            };

            mqttClient.ConnectAsync(mqttClientOptions, CancellationToken.None).Wait();

            Console.WriteLine("MQTT client connected!");

            var mqttSubscribeOptions = mqttFactory.CreateSubscribeOptionsBuilder()
                .WithTopicFilter(f => { f.WithTopic(topic); })
                .Build();

            mqttClient.SubscribeAsync(mqttSubscribeOptions, CancellationToken.None).Wait();

            Console.WriteLine("MQTT client subscribed to topic!");
            Thread.Sleep(Timeout.Infinite);
        }

        public static string Evaluate(SensorDataReading r)
        {
            string ret = "";
            switch(r.Name)
            {
                case ("generator"):
                    int g = Int16.Parse(r.Value);
                    if (g > 355)
                        ret = "";
                    break;
                case ("dishwasher"):
                    int d = Int16.Parse(r.Value);
                    if (d > 3)
                        ret = "dishwasher";
                    break;
                case ("microwave"):
                    int m = Int16.Parse(r.Value);
                    if (m > 5)
                        ret = "microwave";
                    break;
                case ("tvairconditioner"):
                    int t = Int16.Parse(r.Value);
                    if (t > 3 && t < 5 && t > 330)
                        ret = "tv";
                    break;
                case ("washingmachine"):
                    int w = Int16.Parse(r.Value);
                    if (w > 75)
                        ret = "washingmachine";
                    break;
                default:
                    break;
            }
            return ret;
        }
    }
}