# Hands-On: IOT with Machine Learning


### Stage 1

- Introduction to Arduino, Raspberry Pico and ESP32 @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c3806c942ac7bfa0ac0dbc?pvs=21)

- Introduction to Arduino IDE, Thonny @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380f5bdb7dd0befcc3dee?pvs=21)

- Introduction to Raspberry Family, Architecture and PINS. @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380da84bde8f0894e9fa6?pvs=21)

### Stage 2

- Writing a Blink LED program @Sakib Dalal
- Write code for internal temperature read program @Sakib Dalal
- Writing code for storing timestamp and temperature into csv file @Sakib Dalal

### Stage 3

- Introduction to PowerBI @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380b68310fc9f2896b5d7?pvs=21)

- Visualising csv file into PowerBI @Harshit Rawal

[Page](https://www.notion.so/Page-23df289269c380b898a7c53b593410a2?pvs=21)

### Stage 4

- Introduction to Kaggle @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c3803d99e1cd2029c50252?pvs=21)

- Create account for Kaggle @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380d58559dc3a93cb76e6?pvs=21)

- Uploading csv dataset to Kaggle @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c3802093bff26342ab798f?pvs=21)

### Stage 5

- Introduction to Kaggle code @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380ae8ef8d8ab2d3afdc7?pvs=21)

- using pandas dataframe to import csv file @Sakib Dalal
- using matplotlib to visualise csv data @Sakib Dalal
- Introduction to ML and Scikit Learn @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c38020a188d07def365984?pvs=21)

- Introduction to Train Test Split, Normalization (Standard Scaling) and Linear Regression. @Harshit Rawal -

[Page](https://www.notion.so/Page-23df289269c380f68613e0a773a09ea8?pvs=21)

- Implementation of train test split on dataset @Sakib Dalal
- Implementation of Linear Regression and finding accuracy of model @Sakib Dalal
- Conclusion @Harshit Rawal

## SP

- Raspberry pico W Blynk App, LED control with Relay Module (Home Automation): https://www.youtube.com/watch?v=K37b4zIFrho
- Raspberry pico W OLED display GPS tracker: https://toptechboy.com/raspberry-pi-pico-gps-tracker-with-oled-display/
- Raspberry pico bluetooth car: https://www.instructables.com/Simple-Bluetooth-Controlled-Car-Raspberry-Pi-Pico/
- Raspberry pico W ChatGPT: https://www.instructables.com/How-to-Set-Up-ChatGPT-on-a-Raspberry-Pi-Pico-W/

## Other Projects

- Raspberry Pi NAS (Network-Attached Storage): https://www.youtube.com/watch?v=gyOHTZvhnxY
- ChatGPT on Raspberry Pi (No Internet Needed): https://www.youtube.com/watch?v=N0718RfpuWE
- Raspberry Pi AI Voice Assistant: https://www.youtube.com/watch?v=XvbVePuP7NY
- Sign Language Translator With Viam And Raspberry Pi Zero**:** https://www.youtube.com/watch?v=ByrtJx1cG8o

## Blink Code - 01

```python
from machine import Pin
import time

# Use GPIO 25 for external LED (change if using another pin)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)     # Turn LED ON
    time.sleep(1)    # Wait 1 second
    led.value(0)     # Turn LED OFF
    time.sleep(1)    # Wait 1 second
```

---

```python
from machine import Pin
import time
```

✅ **Explanation**:

- `machine` is a MicroPython module that provides access to hardware components.
- `Pin` is used to control GPIO (General Purpose Input Output) pins.
- `time` module is used to add delays with `sleep()`.

---

```python
# Use GPIO 25 for external LED (change if using another pin)
led = Pin(25, Pin.OUT)
```

✅ **Explanation**:

- `Pin(25, Pin.OUT)` sets **GPIO pin 25** as an **output pin**.
- `led` is now a **Pin object** you can control (like turning the LED on/off).
- Note: On the Raspberry Pi Pico, **GPIO 25 is connected to the onboard LED**.

---

```python
while True:
```

✅ **Explanation**:

- This starts an **infinite loop** so the LED will blink continuously.

---

```python
    led.value(1)     # Turn LED ON
```

✅ **Explanation**:

- `led.value(1)` sets the pin **HIGH (3.3V)** → LED turns **ON**.

---

```python
    time.sleep(1)    # Wait 1 second
```

✅ **Explanation**:

- Pauses the program for **1 second**, keeping the LED ON.

---

```python
    led.value(0)     # Turn LED OFF
```

✅ **Explanation**:

- `led.value(0)` sets the pin **LOW (0V)** → LED turns **OFF**.

---

```python
    time.sleep(1)    # Wait 1 second
```

✅ **Explanation**:

- Pauses for another second before the loop repeats, keeping the LED OFF.

---

### 🔁 Final Behavior:

The LED connected to **GPIO 25** (or onboard LED) will:

- Turn ON for 1 second
- Turn OFF for 1 second
- Repeat forever (blinking)

Let me know if you want to control this blink with a button or change the speed.

## Internal Temperature Read - 02

```python
import machine
import time

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2)
    print("Temperature: ",temperature)
    time.sleep(0.1)
```

---

### ✅ Code:

```python
import machine
import time

```

✅ **Explanation**:

- `machine`: MicroPython module to interact with hardware (like ADC, Pin, etc.).
- `time`: Used for delays with `sleep()`.

---

```python
sensor_temp = machine.ADC(4)

```

✅ **Explanation**:

- On the **RP2040 chip** (used in Pico), **ADC channel 4** is connected internally to the **temperature sensor**.
- So `machine.ADC(4)` creates an ADC object to read from the **internal temperature sensor**.

---

```python
conversion_factor = 3.3 / 65535

```

✅ **Explanation**:

- The ADC (Analog-to-Digital Converter) has **16-bit resolution**, so its values range from `0` to `65535`.
- The Pico runs at **3.3V**, so this formula converts the raw ADC value to **voltage in volts (V)**.

---

```python
while True:

```

✅ **Explanation**:

- An **infinite loop** to continuously read and print the temperature.

---

```python
    reading = sensor_temp.read_u16() * conversion_factor

```

✅ **Explanation**:

- `read_u16()` gives a 16-bit (0–65535) raw ADC value.
- Multiplying it by `conversion_factor` converts it to a **voltage** in **volts**.

---

```python
    temperature = round(27 - (reading - 0.706)/0.001721, 2)

```

✅ **Explanation**:

- This converts the voltage reading to **temperature in Celsius** using the formula provided by the RP2040 datasheet:
    
    T=27−(Vsense−0.706)0.001721T = 27 - \frac{(V_{sense} - 0.706)}{0.001721}
    
    Where:
    
    - `0.706 V` is the voltage at 27°C
    - `0.001721 V/°C` is the slope (change in voltage per °C)
- `round(..., 2)` limits the result to **2 decimal places**.

---

```python
    print("Temperature: ", temperature)

```

✅ **Explanation**:

- Displays the temperature in the console (e.g., `Temperature: 32.75`)

---

```python
    time.sleep(0.1)

```

✅ **Explanation**:

- Waits **0.1 seconds** (100ms) before reading the next value.

---

### 🌡️ Final Output:

It prints the **CPU’s internal temperature** every 0.1 seconds like:

```
Temperature: 32.75
Temperature: 32.74
...

```

## Read Temp and Store as CSV - 03

```python
import machine
import time

# --- Constants ---
FILENAME = "temperature_data.csv"
LOG_INTERVAL_SEC = 10  # Log every 10 seconds
LED_PIN = "LED"  # Onboard LED pin

# --- Hardware Setup ---
sensor_temp = machine.ADC(4)
led = machine.Pin(LED_PIN, machine.Pin.OUT)
conversion_factor = 3.3 / 65535

# --- Functions ---
def get_temperature():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    return round(temperature, 2)

def log_temperature(filename, timestamp, temperature):
    try:
        with open(filename, 'a') as f:
            f.write(f"{timestamp},{temperature}\n")
    except Exception as e:
        print(f"[ERROR] Writing to file failed: {e}")

def blink_led(duration_ms=100):
    led.value(1)
    time.sleep_ms(duration_ms)
    led.value(0)

def initialize_csv(filename):
    try:
        with open(filename, 'w') as f:
            f.write("timestamp_ms,temperature_celsius\n")
        print(f"[INFO] '{filename}' created successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to create file: {e}")

# --- Initialize ---
initialize_csv(FILENAME)

# --- Main Loop ---
print("[INFO] Starting temperature logging...")
try:
    while True:
        temp = get_temperature()
        ts = time.ticks_ms()
        log_temperature(FILENAME, ts, temp)
        print(f"[LOG] {ts} ms | Temp: {temp} °C")
        blink_led(200)
        time.sleep(LOG_INTERVAL_SEC)
except KeyboardInterrupt:
    print("\n[INFO] Program stopped by user.")
except Exception as e:
    print(f"[FATAL] Unexpected error: {e}")
    time.sleep(5)

```

🔁 **Continuously read** the **internal temperature sensor**,

📁 **Log each reading to a CSV file** with a timestamp, and

🖥️ **Print the result to the console** every 2 seconds.

---

## 🧠 High-Level Functionality

This script:

1. Initializes the internal temperature sensor.
2. Creates a CSV file and writes the column headers.
3. Repeatedly:
    - Reads the temperature.
    - Adds a timestamp.
    - Logs the data to the CSV file.
    - Displays it on the serial console.

---

### ✅ Import required modules

```python
import machine
import time
```

- `machine`: Allows you to interact with hardware (like ADC).
- `time`: Provides functions for delays (`sleep`) and timestamps (`ticks_ms`).

---

### 🌡 Sensor Setup

```python
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
FILENAME = "temperature_data.csv"
```

- `ADC(4)`: Accesses the internal **temperature sensor** of the RP2040 chip.
- `conversion_factor`: Converts 16-bit ADC value (0–65535) into voltage.
- `FILENAME`: The name of the CSV file where temperature data will be stored.

---

### 📝 Create the CSV file and write a header

```python
try:
    with open(FILENAME, 'w') as f:
        f.write("timestamp_ms,temperature_celsius\n")
    print(f"'{FILENAME}' created successfully.")
except Exception as e:
    print(f"Error creating file: {e}")
```

- `open(FILENAME, 'w')`: Opens the file in **write mode**, creating it fresh each time the Pico boots.
- Writes the CSV column headers: `timestamp_ms` and `temperature_celsius`.
- Catches and prints any file creation errors.

---

### 🔁 Repeating the reading and logging process

```python
while True:
    try:
```

- Starts an infinite loop that continues until manually interrupted (like pressing Ctrl+C).

---

### 🧮 Read the temperature

```python
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = round(27 - (reading - 0.706) / 0.001721, 2)
```

- `read_u16()`: Gets the raw ADC value.
- Multiplied by `conversion_factor` to get voltage.
- Converts the voltage into temperature using this RP2040 formula:
    
    T=27−(V−0.706)0.001721T = 27 - \frac{(V - 0.706)}{0.001721}
    
- `round(..., 2)` keeps only 2 decimal places.

---

### ⏱ Timestamp

```python
        timestamp = time.ticks_ms()
```

- Gets the number of milliseconds since the Pico was powered on.

---

### 💾 Append the reading to the file

```python
        with open(FILENAME, 'a') as f:
            f.write(f"{timestamp},{temperature}\n")
```

- Opens the file in **append mode** so new data is added at the end.
- Logs the reading and its timestamp as a new CSV row.

---

### 🖨 Print to console

```python
        print(f"Temperature: {temperature} °C | Logged to {FILENAME}")
```

- Displays each temperature reading and confirms it was saved to the file.

---

### ⏳ Wait before next reading

```python
        time.sleep(2)
```

- Waits **2 seconds** before repeating the loop.
- Helps reduce file size and prevents sensor spam.

---

### 🛑 Graceful Exit & Error Handling

```python
    except KeyboardInterrupt:
        print("Program stopped.")
        break
```

- Allows you to stop the program manually with Ctrl+C.

```python
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)
```

- Handles other runtime errors (e.g., file write failure).
- Waits 5 seconds before retrying to avoid repeated crashes.

---

## 📊 Sample Output

**Console:**

```
Temperature: 28.41 °C | Logged to temperature_data.csv
```

**CSV File:**

```
timestamp_ms,temperature_celsius
1003,28.41
3005,28.42
...
```

---