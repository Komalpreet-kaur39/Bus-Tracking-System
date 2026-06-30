#include <WiFi.h>
#include <HTTPClient.h>
#include <TinyGPS++.h>

// Wi-Fi credentials
const char *ssid = "realme 9 5G";  // Replace with your Wi-Fi SSID
const char *password = "12345678"; // Replace with your Wi-Fi password

// Static IP config
// IPAddress local_IP(192, 168, 225, 91);  // Static IP (same subnet as your PC)
// IPAddress gateway(192, 168, 225, 1);    // Your router's gateway IP (usually 192.168.225.1)
// IPAddress subnet(255, 255, 255, 0);     // Subnet mask

// GPS on Serial2 (TX=17, RX=16)
HardwareSerial gpsSerial(2);
TinyGPSPlus gps;

// GPS coordinates storage
float latitude = 0.0;
float longitude = 0.0;
unsigned long lastPostTime = 0; // To store last time data was sent

void setup()
{
  // Start serial communication
  Serial.begin(115200);

  // Start GPS serial communication
  gpsSerial.begin(9600, SERIAL_8N1, 16, 17); // RX, TX

  Serial.println("Starting setup...");

  // Set static IP before WiFi.begin
  Serial.print("Setting static IP...");
  // if (!WiFi.config(local_IP, gateway, subnet)) {
  //   Serial.println("STA Failed to configure static IP");
  // } else {
  //   Serial.println("Static IP set successfully.");
  // }

  // Connect to Wi-Fi
  Serial.print("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  Serial.println("Local IP:" + WiFi.localIP());

  // Wait for the Wi-Fi to connect
  int retries = 0;
  while (WiFi.status() != WL_CONNECTED && retries < 20)
  {
    delay(500);
    Serial.print(".");
    retries++;
  }

  if (WiFi.status() == WL_CONNECTED)
  {
    Serial.println("\nWiFi Connected!");
    Serial.print("ESP32 Local IP Address: ");
    Serial.println(WiFi.localIP());
  }
  else
  {
    Serial.println("\nFailed to connect to WiFi");
    return; // Exit setup() if WiFi is not connected
  }
}

void updateGPS()
{
  // Check if data is available from the GPS (non-blocking)
  if (gpsSerial.available() > 0)
  {
    gps.encode(gpsSerial.read());

    // If GPS has a valid fix, get the coordinates
    if (gps.location.isValid())
    {
      latitude = gps.location.lat();
      longitude = gps.location.lng();

      // Print coordinates to the Serial Monitor
      Serial.println("New GPS Coordinates:");
      Serial.print("Lat: ");
      Serial.println(latitude, 6); // Print latitude with 6 decimal places
      Serial.print("Lng: ");
      Serial.println(longitude, 6); // Print longitude with 6 decimal places
    }
  }
}

void loop()
{
  // Update GPS coordinates if new data is available
  updateGPS();

  // Only send the data if 3 seconds have passed
  if (millis() - lastPostTime > 3000)
  {
    lastPostTime = millis(); // Update the last post time

    // Send data to Django server if WiFi is connected
    if (WiFi.status() == WL_CONNECTED)
    {
      HTTPClient http;
      String url = "http://192.168.173.91:8000/save_location/";


      Serial.println("Sending data to Django server...");

      // Start HTTP request
      http.begin(url);
      http.addHeader("Content-Type", "application/json");

      // Create JSON payload
      String json = "{\"bus_id\": \"3\", \"latitude\": " + String(latitude, 6) +
                    ", \"longitude\": " + String(longitude, 6) + "}";

      // Send HTTP POST request
      int httpCode = http.POST(json);
      Serial.print("HTTP POST code: ");
      Serial.println(httpCode);

      // Check if the request was successful
      if (httpCode == 200)
      {
        Serial.println("Data sent successfully!");
      }
      else
      {
        Serial.print("Failed to send data. HTTP Code: ");
        Serial.println(httpCode);
      }

      // End HTTP request
      http.end();
    }
    else
    {
      Serial.println("WiFi not connected! Cannot send data.");
    }
  }

  delay(100); // A short delay before checking GPS data again
}
