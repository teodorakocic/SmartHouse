using Newtonsoft.Json;

namespace Monitoring
{
    public class SensorDataReading
    {
        public SensorDataReading(string id = "unknown", string device = "unknown", string origin = "unknown", string name = "unknown", string valueType = "unknown", string value = "unknown")
        {
            Id = id;
            Device = device;
            Origin = origin;
            Name = name;
            ValueType = valueType;
            Value = value;
        }
        public string Id { get; set; } 
        public string Device { get; set; } 
        public string Origin { get; set; } 
        public string Name { get; set; }
        public string ValueType { get; set; }
        public string Value { get; set; }

        public override string ToString()
        {
            return JsonConvert.SerializeObject(this);
        }
    }
}