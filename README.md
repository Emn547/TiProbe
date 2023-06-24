# TiProbe
This project includes the class for the Schnider stepper motor class and the measurment procedure script (includes the Schnider stepper motor class as well)
## Schnider LMDCM572 Step Motor Operation and Commands
### Setting Up The Communication with the motor
The communication is done via serial channel. There is a serial to USB adapter for the schnider motor. After connecting it to the USB port, one can find the serial port associated with the motor using the Device Manager window in the Control Panel under Ports:
![image](https://github.com/Emn547/TiProbe/assets/29408499/d9eb4d22-46c1-4093-b3a1-e0e517ec2c96)

In this case the serial channel is COM3. As such, this is the serial port that will be used in the code.

## Stepper Motor Commands
### Data Query Translator
#### <u> query(self, query) <u>
Translates the query from string to bytes  and outputs the response of the serial channel

### Command Writer Function
#### serial_write(self, command, number_of_trys=3)
Translates the command from string to bytes and writes it to the serial channel

### Data Query Function
#### get_all(self)
Returns all of the stepper motor's parapeters (position, acceleration, etc.)
#### get_v(self)
Returns the motor's real time velocity value
#### get_vi(self)
Returns the motor's initial velocity value 
#### get_vf(self)
Returns the motor's final velocity value 
#### get_vm(self)
Returns the motor's maximum velocity value 
#### get_pos(self)
Returns the motor's real time position value
#### get_encoder(self)
Returns the motor's encoder mode
#### get_echo(self)
Returns the motor's echo mode
#### is_moving(self)
Returns a flag if the motor is moving or not

###System Configuration Functions
#### __set_echo(self, mode)__
Echo mode configuration: the range of values for the echo mode is: 0,1,2,3.
        mode values = {0,1,2,3}
        0 – the user input and the system output are presented at the buffer.
        1 – only the user input is presented at the buffer
        2 – only the system output is presented at the buffer.
        3 – the user input and the system output are presented after hitting the return (“enter”) button"""

        



