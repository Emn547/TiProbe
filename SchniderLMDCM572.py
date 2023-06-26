import serial
import time

# -----------------------------------SCHNIDER_STEPPER_MOTOR_CLASS---------------------------------- #

class SchniderLMDCM572:
    # --------------------stepper_motor_serial_build_function_and_configuration----------------- #
    def __init__(self, port, baudrate):
        """sets the serial channel for the engine"""
        self.port = serial.Serial(port, baudrate, timeout=1)
        self.port.close()
        self.port.open()

    # ------------------------------------data_query_translator---------------------------------#
    def query(self, query):
        """translates the query from string to bytes and outputs the response of the serial channel"""
        self.port.reset_output_buffer()
        self.port.reset_input_buffer()
        query = query + '\r\n'
        query_bytes = bytes(query, 'utf-8')
        write_command_length = self.port.write(query_bytes)
        if write_command_length != len(query):
            raise Exception("serial write error!")
        time.sleep(0.2)
        self.port.read(write_command_length)
        response = self.port.readline()
        response = response.decode('utf-8')
        self.port.read()
        return response[:len(response) - 1]

    # ----------------------------------command_writer_function---------------------------------#
    def serial_write(self, command, number_of_trys=3):
        """translates the command from string to bytes and writes it to the serial channel"""
        self.port.reset_output_buffer()
        self.port.reset_input_buffer()
        command = command + '\r\n'
        command_bytes = bytes(command, 'utf-8')
        time.sleep(0.2)
        failed = True
        for i in range(number_of_trys):
            self.port.write(command_bytes)
            self.port.flush()
            if self.port.read(len(command_bytes)) != command_bytes:
                raise Exception("shit")
            res = self.port.read(2)
            if res == bytes('>\n', 'utf-8'):
                failed = False
                break
            print("Failed sending! Retry #%d" % i)
        if failed:
            raise Exception("Failed sending!")

    # -----------------------------------data_query_functions-----------------------------------#
    def get_all(self):
        """get all the motor's parameters values"""
        return self.query("PR AL")

    def get_v(self):
        """get the motor's real time velocity value"""
        return self.query("PR V")

    def get_vi(self):
        """gets the motor's initial velocity value"""
        return self.query("PR VI")

    def get_vf(self):
        """gets the motor's final velocity value"""
        return self.query("PR VF")

    def get_vm(self):
        """gets the motor's maximum velocity"""
        return self.query("PR VM")

    def get_pos(self):
        """gets the motor's real time velocity value"""
        return self.query("PR P")

    def get_encoder(self):
        """gets the motor's encoder mode"""
        return self.query("PR EE")

    def get_echo(self):
        """gets the motor's echo mode"""
        return self.query("PR EM")

    def is_moving(self):
        """flags if the motor is moving or not"""
        if float(self.query("PR MV")) == 1:
            return True
        else:
            return False

    # -------------------------------------system setting functions-----------------------------#
    def set_echo(self, mode):
        """Echo mode configuration: the range of values for the echo mode is: 0,1,2,3.
        mode values = {0,1,2,3}
        0 – the user input and the system output are presented at the buffer.
        1 – only the user input is presented at the buffer
        2 – only the system output is presented at the buffer.
        3 – the user input and the system output are presented after hitting the return (“enter”) button"""
        self.serial_write("EM " + str(mode))

    def set_escFlag(self, flag):
        # set escape flag (flag values = {0,1,2,3})
        """escape flag configuration: configures the escape flag. Entering the escape flag will stop both the program
        and the motor. 0 – escape flag set to respond to CTRL+E 1 – escape flag set to respond to ESC keypress (
        default) 2 – escape flag set to respond to addressable CTRL+E (party mode) 3 – escape flag set to respond to
        addressable ESC keypress (party mode) (party mode = several motors are controlled by the same computer,
        sometimes appears as “hagiga” mode). """
        self.serial_write("ES " + str(flag))

    # ----------------------------------movement setting functions------------------------------#
    def set_vi(self, initial_velocity):
        """set initial velocity (range: 1-5000000)"""
        self.serial_write("VI " + str(initial_velocity))

    def set_vf(self, final_velocity):
        """set final revolution velocity (range: 1-5000000)"""
        self.serial_write("VF " + str(final_velocity))

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

    # ----------------------------------movement control functions------------------------------#
    def move_abs(self, absolute_position):
        """move to an absolute position (range - signed 32 bit)"""
        self.serial_write("MA " + str(absolute_position))

    def move_rel(self, distance):
        """move relatively to your current position (range - signed 32 bit)"""
        self.serial_write("MR " + str(distance))

    def move_prev(self, value):
        """move according to previous movement command"""
        self.serial_write("-" + str(value))

    def move(self, speed):
        """move constantly with a constant input speed (range +- 5000000)"""
        self.serial_write("SL " + str(speed))
