# Website (D3.js) for Raspberry Pi temperature and humidity (DHT11)




# Setup hardware

```
# DHT-11
._________________.
|.................|__ 4 -> GND (-) -> Ground
|.................|__ 3 -> Into nowhere 
|.................|__ 2 -> Resistor (4,7kOhm) -> GPIO 4 {Resistor End to 3V3 Power}
|_________________|__ 1 -> 3V3 Power (+) -> Power
```

![Connect DHT-11 on the Board to R-PI (GPIO)](/images/Connect_DHT-11_to_R-PI.png "Connect DHT-11 on the Board to R-PI (GPIO)")


# Install AdafruitDHT Library
## Adafruit Python DHT Sensor Library
Do some preperation
```bash
sudo apt-get update
sudo apt-get install build-essential python-dev
```

Clone the GitHub Repository
```bash
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
```

Install the script from repository
```bash
cd Adafruit_Python_DHT/
```
```bash
sudo python setup.py install
```

## Got an error?
```bash
Traceback (most recent call last):
  File "setup.py", line 1, in <module>
    from setuptools import setup, find_packages, Extension
ImportError: No module named setuptools
```

Install pythonX-setuptools
```bash
# To install setuptools on Debian:
sudo apt-get install python3-setuptools

# For an older version of Python (Python 2.x):
sudo apt-get install python-setuptools
```

## First test with AdafruitDHT
Go to example folder
```bash
cd examples
sudo ./AdafruitDHT.py 11 4
```
The first parameter (11) indicates which sensor was used (22 for the DHT22) and the second, to which GPIO it is connected (not the pin number, but the GPIO number). 

```bash
# This produces an output like the following:
emp=24.0*  Humidity=41.0%
```

> Attention: The sensors are only ready every two seconds. Be careful not to start a query every second.

# Add AdafruitDHT Library to projects
To integrate the Raspberry Pi humidity library into other (Python) projects, you only need the following:
```py
import Adafruit_DHT

# ...

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#...
```


# Use it
You can use the script [Write data into csv-file](scripts/dht11_to_csv.py)

# Crontab
## Want to run it on crontab? (e.g. every hour, day, ...)
> 💡 Executive file must be (`sudo chmod +x name-of-csv-file.xyz`)

Add this to `crontab -e`

```markdown
# Every 5min
5 * * * * python /home/pi/PATH/TO/SCRPT
```

## Need sudo?

**Use root's crontab**

Run the following command:

```bash
sudo crontab -e
```

## Syntax

```bash
#### Syntax
The syntax is:
1 2 3 4 5 /path/to/command arg1 arg2
OR
1 2 3 4 5 /root/backup.sh

Where,

1: Minute (0-59)
2: Hours (0-23)
3: Day (0-31)
4: Month (0-12 [12 == December])
5: Day of the week(0-7 [7 or 0 == sunday])
/path/to/command – Script or command name to schedule

Easy to remember format:
* * * * * command to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```



# Install webserver on raspberry pi    
> How to setup a website on the raspberry. Only with open source software

>💡 Nginx is running on Port 80, make sure nothing else is running there! (Apache 2, PiHole,..)
## Update

```bash
# Make sure everything is up to date
apt-get update
apt-get upgrade
```

## Setup

1. Install Nginx

```bash
sudo apt install nginx
```

2. Check if it works

```bash
# On Raspberry PI
curl localhost

# On any other maschine
curl <IP-of-Raspberry-Pi>
```

## **Automatically start nginx on boot**

We just issue the following command to make sure the nginx webserver is always started on bootup:

```bash
sudo update-rc.d -f nginx defaults;
```


## Edit HTML-File

Go to `/var/www/html/` and edit everything you want. You have to use sudo!


# Use d3.js
> 💡 CSV-file must be in the same folder!
> CSV-file must be (`sudo chmod +x name-of-csv-file.csv`)

You can find the HTML-file [here](index.html)
And the JS-files [here (index.js)](js/index.js) and [here (grid.js)](js/grid.js)


## Example CSV

```python
Date,Disk_usage,CPU,Memory,CPU_TEMP,DHT11_Temperature,DHT11_Humidity
2021-12-02 20:05:05.336617,14.7,0.0,0,23.8,15.0,60.0
2021-12-02 20:08:18.767502,14.7,0.0,0,23.5,17.0,61.0
2021-12-02 20:09:30.924323,14.7,5.1,0,23.4,20.0,62.0
```
