# EnduranceTest_Rpi_InfluxDB

In this Repo, we are detecting the Btn Pressed in order to use it in the RET.
```
cd Repo_BtnMasher_Rpi/
```

The main method that is used is called  BtnMasherApplication.py and is calling the other small module.
```
sudo python BtnMasherApplication.py
```

The function is able to detect the Btn pressed and write the button where pressed in InfluxDB meanwhile a logfile is generated in case any issue happens.

For now, the only thing that is logged into the logfile is the info that is written in InfluxDB: but we can add some warning and error for postprocessing (for instance, when a btn is pressed two time in a raw this could be a warning). 

# With the databases log
In a new terminal:

```sudo systemctl start influxdb```
```sudo systemctl start telegraf``` just using influxdb for now but might be useful for looking deeper in the data afterwards
```sudo systemctl start chronograf```
```influx```

