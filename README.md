# TiProbe
This project includes the class for the Schnider stepper motor class and the measurment procedure script (includes the Schnider stepper motor class as well)
## Schnider LMDCM572 Step Motor Operation and Commands
### Setting Up The Communication with the motor
The communication is done via serial channel. There is a serial to USB adapter for the schnider motor. After connecting it to the USB port, one can find the serial port associated with the motor using the Device Manager window in the Control Panel under Ports:
![image](https://github.com/Emn547/TiProbe/assets/29408499/d9eb4d22-46c1-4093-b3a1-e0e517ec2c96)

In this case the serial channel is COM3. As such, this is the serial port that will be used in the code.

### Stepper Motor Commands
#### query(self, query)
Translates the query from string to bytes  and outputs the response of the serial channel
#### serial_write(self, command, number_of_trys=3)
Translates the command from string to bytes and writes it to the serial channel

