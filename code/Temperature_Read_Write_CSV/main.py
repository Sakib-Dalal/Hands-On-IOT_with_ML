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
