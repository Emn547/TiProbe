# TiProbe
This project includes the class for the Schnider stepper motor class and the measurment procedure script (includes the Schnider stepper motor class as well)
## Schnider LMDCM572 Step Motor Operation and Commands
### Setting Up The Communication with the motor
The communication is done via serial channel. There is a serial to USB adapter for the schnider motor. After connecting it to the USB port, one can find the serial port associated with the motor using the Device Manager window in the Control Panel under Ports:
![image](https://github.com/Emn547/TiProbe/assets/29408499/d9eb4d22-46c1-4093-b3a1-e0e517ec2c96)

In this case the serial channel is COM3. As such, this is the serial port that will be used in the code.

## Stepper Motor Commands
### Data Query Translator
#### *__query(self, query)__* 
Translates the query from string to bytes  and outputs the response of the serial channel<br>


### Command Writer Function
#### *__serial_write(self, command, number_of_trys=3)__*
Translates the command from string to bytes and writes it to the serial channel<br>


### Data Query Functions
#### *__get_all(self)__*
Returns all of the stepper motor's parapeters (position, acceleration, etc.)
#### *__get_v(self)__*
Returns the motor's real time velocity value
#### *__get_vi(self)__*
Returns the motor's initial velocity value 
#### *__get_vf(self)__*
Returns the motor's final velocity value 
#### *__get_vm(self)__*
Returns the motor's maximum velocity value 
#### *__get_pos(self)__*
Returns the motor's real time position value
#### *__get_encoder(self)__*
Returns the motor's encoder mode
#### *__get_echo(self)__*
Returns the motor's echo mode
#### *__is_moving(self)__*
Returns a flag if the motor is moving or not


### System Configuration Functions
#### *__set_echo(self, mode)__*
This function sets the echo mode (valid mode values = {0,1,2,3}).<br>
Echo mode configuration: the range of values for the echo mode is: 0,1,2,3.<br>
        0 – the user input and the system output are presented at the buffer.<br>
        1 – only the user input is presented at the buffer<br>
        2 – only the system output is presented at the buffer<br>
        3 – the user input and the system output are presented after hitting the return (“enter”) button<br>

#### *__set_escFlag(self, flag)__*
This function sets the escape flag value (valid flag values = {0,1,2,3}).
Escape flag configuration: configures the escape flag (entering the escape flag will stop both the program and the motor)<br> 
        0 – escape flag set to respond to CTRL+E<br> 
        1 – escape flag set to respond to ESC keypress (default)<br> 
        2 – escape flag set to respond to addressable CTRL+E (party mode)<br> 
        3 – escape flag set to respond to addressable ESC keypress (party mode) (party mode = several motors are controlled by the same computer)<br>


### Movement Configuration Functions
#### *__set_vi(self, initial_velocity)__*
Sets the initial velocityof the motor (input range: 1-5000000)

#### *__set_vf(self, final_velocity)__*
Sets final revolution velocity (input range: 1-5000000)

#### *__set_vm(self, max_velocity)__*
Sets the maximum revolution velocity of the engine movement procedure (range: 1-5000000)
        
#### *__set_accel(self, acceleration)__*
Sets the motor's acceleration  (input range: 1-1000000000)

#### *__set_decel(self, deceleration)__*
Sets the motor's deceleration (input range: 1–1000000000)

#### *__encoder_mode(self, mode)__*
Enables/disables encoder function (valid mode values = {0,1}).
        0 - sets the revolution resolution to 56,000 steps per revolution
        1 - sets the resolution resolution to 4,000 steps per revolution

__Note:__ in order to get a high resolution using the MA and MR motion functions one must define moderate values for acceleration, initial velocity, 
maximum velocity and deceleration. Setting high values for those parameters can lead to a step deviation (evenseveral steps).

### Movement Control Functions
#### *__move_abs(self, absolute_position)__*
Moves the motor to an absolute position specified by the user (input range: signed 32 bit)
 
#### *__move_rel(self, distance)__*
Moves the motor relatively to to its initial current position (input range: signed 32 bit)

#### *__move_prev(self, value)__*
Moves the motor according to previous movement command with the user's input (value)

#### *__move(self, speed)__*
Moves the motor constantly with a constant input speed (input range: -+ 5000000)




        



