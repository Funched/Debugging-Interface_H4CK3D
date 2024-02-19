# Debugging-Interface_H4CK3D
Hack The Box Debugging Interface Challenge Walkthrough
This challenge from the HTB indicates that the asynchronous serial debugging interface was accessed while running and that some messages transmitted over this interface were intercepted. It is requested to analyze this traffic and find the flag.

There is a file called debugging_interface_signal.sal. This file contains the captured traffic. Let's start analyzing!

![image](https://github.com/Funched/Debugging-Interface_H4CK3D/assets/135317904/b46b2a3f-f693-4568-90b3-e4d18e490003)

This is an archived file and contains "digital-0.bin" and "meta.json"

After extraction, we can analyze them with the **string** command to access sensitive information. 

![image](https://github.com/Funched/Debugging-Interface_H4CK3D/assets/135317904/94fbbb41-995e-4800-b72f-e374bd3aeeb0)

We couldn't find anything that useful string inside of meta.json.

Let's check the digital-0.bin file.

![image](https://github.com/Funched/Debugging-Interface_H4CK3D/assets/135317904/8341f181-70cf-45c0-a09e-542db2f9f80f)

There is <salae> in the strings, but the rest of the strings don't make much sense.

It is time to research.

Bingo!

Salae is a logic analyzer used to analyze protocols such as I2C, SPI, Serial, etc.

We can use Salae software to analyze debugging_interface_signal.sal file. 

After the installation, we will see an interface like this. We can import the file as shown on the image.

![image](https://github.com/Funched/Debugging-Interface_H4CK3D/assets/135317904/573d5726-e5fd-4ff6-83ba-be810b69e2a8)


There are square waves...
We still haven't found any useful information. We need to configure the analyzer and start analyzing the signals.

![image](https://github.com/Funched/Debugging-Interface_H4CK3D/assets/135317904/1f804618-92a2-42db-b774-37a0d7b900e0)

Now we have hexadecimal data corresponding to each square pulse. We have to export hex data and convert it to ASCII format. 
