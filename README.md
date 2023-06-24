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
This function sets the echo mode (valid mode values = {0,1,2,3}).
Echo mode configuration: the range of values for the echo mode is: 0,1,2,3.
        0 – the user input and the system output are presented at the buffer.
        1 – only the user input is presented at the buffer
        2 – only the system output is presented at the buffer.
        3 – the user input and the system output are presented after hitting the return (“enter”) button

#### *__set_escFlag(self, flag)__*
This function sets the escape flag value ( valid flag values = {0,1,2,3}).
Escape flag configuration: configures the escape flag (entering the escape flag will stop both the program and the motor) 
        0 – escape flag set to respond to CTRL+E 
        1 – escape flag set to respond to ESC keypress (default) 
        2 – escape flag set to respond to addressable CTRL+E (party mode) 
        3 – escape flag set to respond to addressable ESC keypress (party mode) (party mode = several motors are controlled by the same computer)

### Movement Configuration Functions
#### *__set_vi(self, initial_velocity)__*
Sets the initial velocityof the motor (input range: 1-5000000)

#### *__set_vf(self, final_velocity)__*
Sets final revolution velocity (input range: 1-5000000)

    def set_vm(self, max_velocity):
        """set final revolution velocity (range: 1-5000000)"""
        self.serial_write("VM " + str(max_velocity))

    def set_accel(self, acceleration):
        """set acceleration (range – 1000000000)"""
        self.serial_write("A " + str(acceleration))

    def set_decel(self, deceleration):
        """set deceleration (range – 1000000000)"""
        self.serial_write("D " + str(deceleration))

    def encoder_mode(self, mode):
        """enable/disable encoder function (mode = {0,1})
            If mode = 0 then the resolution is 56,000 steps per revolution, if mode = 1 the resolution is 4,000 steps
            per revolution. Note: in order to get a high resolution using the MA and MR motion function one must define
            moderate values for A, VI, VM and D. High values of those parameters can lead to a step deviation (even
            several steps). For getting even higher precision (wanna get high?) the encoder resolution needs to be set
            to mode = 0 (more steps per revolution)."""
        self.serial_write("EE " + str(mode))


        



