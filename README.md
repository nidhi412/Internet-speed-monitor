#  Internet Speed Monitor (Raspberry Pi)

##  Overview
This project is a **Raspberry Pi-based Internet Speed Monitoring System**. The system continuously tracks internet performance metrics such as **download speed, upload speed, ping, and jitter**, and provides both **visual dashboards** and **hardware-based feedback**.

The system automates speed testing, stores results over time, and allows users to monitor network performance in real time.

---

##  Features
- Automated internet speed testing using Speedtest CLI  
- Real-time data collection and logging  
- Time-series data storage using InfluxDB  
- Interactive dashboards using Grafana  
- LED-based visual feedback for network performance  
- Cron-based automation for continuous monitoring  

---

##  Technologies Used

###  Software
- Python  
- Speedtest CLI (Ookla)  
- InfluxDB  
- Grafana  
- Linux (Raspberry Pi OS)  

###  Hardware
- Raspberry Pi 3  
- LED  
- Resistor  
- Jumper wires  

---

##  System Architecture
Speedtest CLI → Python Script → InfluxDB → Grafana Dashboard → LED Output


---

##  How It Works

### 1. Speed Testing
The system uses Speedtest CLI to measure:
- Download speed  
- Upload speed  
- Ping  
- Jitter  

---

### 2. Python Script
A Python script:
- Executes the speed test command  
- Extracts relevant data (download, upload, ping, jitter)  
- Formats and stores the results  

---

### 3. Data Storage
- Data is stored in **InfluxDB**, a time-series database  
- Organized for efficient retrieval and analysis  

---

### 4. Visualization
- Grafana is used to create dashboards  
- Displays real-time and historical internet performance data  

---

### 5. Automation
- A **cron job** runs the script at regular intervals (e.g., every minute)  
- Enables continuous and automated monitoring  

---

### 6. LED Feedback
- LED connected to Raspberry Pi GPIO  
- Blinking speed represents network performance:
  - Faster blinking → higher download speed  
  - Slower blinking → lower speed  

---

##  Repository Contents
- `speedtest.py` → Main script to collect and log internet speed data  
- `Speedtest_initial.py` → Initial version of speed testing script  
- `led_blink.py` → LED control based on internet speed   
- Project report/documentation files    

---

##  Notes
- Designed to run on a Raspberry Pi  
- Ensure correct file paths (e.g., `/home/pi/speedtest/`)  
- LED requires proper GPIO wiring with resistor  
- Speedtest CLI must be installed before running scripts  

---

##  Future Improvements
- Integrate InfluxDB for time-series data storage  
- Add Grafana dashboards for visualization  
- Develop GUI for better user interaction  
- Implement alert system (email/SMS notifications)  
- Add additional LEDs for upload and ping indicators  

---

##  Applications
- Home network monitoring  
- Small business network diagnostics  
- Real-time performance tracking  
- Network troubleshooting and optimization  

