string text = "id;routeId;driverId;workload;timeId;conductorId;year;\n";
string routeText = "routeId;route;\n";
string driverText = "driverId;driver;\n";
string timeText = "timeId;time;\nTrue;Day;\nFalse;Night;\n";
string conductorText = "conductorId;conductor;\n";


int count = 100;

for (int id = 1; id <= count; id++)
{
    int routeId = new Random().Next(1, count + 1);
    string driverId = $"Driver_{id}";
    int workload = new Random().Next(1, count + 1);
    bool timeId = Convert.ToBoolean(new Random().Next(0, 2));
    int conductor = new Random().Next(1, count + 1);
    int year = new Random().Next(1970, 2023);
    text += $"{id};{routeId};{driverId};{workload};{timeId};{conductor};{year};\n";


    string route = $"Route_{id}";
    routeText += $"{id};{route};\n";

    string driver = $"Driver_{id}";
    driverText += $"{id};{driver};\n";
    
    string conductorId = $"Conductor_{id}";
    conductorText += $"{id};{conductorId};\n";
}

File.WriteAllText("../output.csv", text);
File.WriteAllText("../route.csv", routeText);
File.WriteAllText("../driver.csv", driverText);
File.WriteAllText("../time.csv", timeText);
File.WriteAllText("../conductor.csv", conductorText);