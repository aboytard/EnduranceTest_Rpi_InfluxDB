# EnduranceTest_Rpi_InfluxDB
The main method that is used is called  BtnMasherApplication.py and is calling the other  module.
```
sudo python Repo_BtnMasher_Rpi/Socket_Server/BtnMasherApplication.py
```

The function is able to detect the Btn pressed and write the button where pressed in InfluxDB meanwhile a logfile is generated in case any issue happens.

For now, the only thing that is logged into the logfile is the info that is written in InfluxDB: but we can add some warning and error for postprocessing (for instance, when a btn is pressed two time in a raw this could be a warning). 

# Start Influxdb
In a new terminal:

start influx
```sudo systemctl start influxdb```

start telegraf:
```sudo systemctl start telegraf```

 just using influxdb for now but might be useful for looking deeper in the data afterwards
```sudo systemctl start chronograf```

go into the influx command line interface:
```influx```

# Once in the influxdb interface
A database has one or more series. Each serie is a time-rodered of value/timestamp pais that shares a measurement, tag-set and field-key

show the databases:
```show databases```

Use the databases of our choise
```show *Name of the databases*```

Vizualise the information : Can also be seen directly in the writing_influxDB.py code
Show the measurements:
```show measurements```

Show the field keys:
```show FIELD KEYS```

Select information:
```select *field keys name* from *measurements*```

Having the right time printed in a readable way: (when you start a influx terminal)
```precision rfc3339```



