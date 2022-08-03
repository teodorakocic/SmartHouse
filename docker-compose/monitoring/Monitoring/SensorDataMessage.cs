using Newtonsoft.Json;

namespace Monitoring
{
    public class SensorDataMessage
    {
        public SensorDataMessage(string id = "unknown", string device = "unknown", string origin = "unknown", List<SensorDataReading> readings = null)
        {
            Id = id;
            Device = device;
            Origin = origin;
            Readings = readings; // referenca nije pravilan constructor
        }
        public string Id { get; set; }
        public string Device { get; set; }
        public string Origin { get; set; }
        public List<SensorDataReading> Readings { get; set; }

        public override string ToString()
        {
            return JsonConvert.SerializeObject(this);
        }

    }
}
