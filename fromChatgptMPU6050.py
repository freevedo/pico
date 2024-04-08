from machine import I2C, Pin
import time

# MPU-6050 I2C address
MPU_ADDR = 0x68

# Create an I2C bus object
i2c = I2C(0,sda=Pin(0), scl=Pin(1))

# Wake up the MPU-6050
i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')

while True:
    # Read the accelerometer data
    accel_data = i2c.readfrom_mem(MPU_ADDR, 0x3B, 6)

    # Convert the data to 16-bit integers
    ax = (accel_data[0] << 8) | accel_data[1]
    ay = (accel_data[2] << 8) | accel_data[3]
    az = (accel_data[4] << 8) | accel_data[5]

    # Print the accelerometer data
    print("Accelerometer:")
    print("x:", ax)
    print("y:", ay)
    print("z:", az)

    # Read the gyroscope data
    gyro_data = i2c.readfrom_mem(MPU_ADDR, 0x43, 6)

        # Convert the data to 16-bit integers
    gx = (gyro_data[0] << 8) | gyro_data[1]
    gy = (gyro_data[2] << 8) | gyro_data[3]
    gz = (gyro_data[4] << 8) | gyro_data[5]

    # Print the gyroscope data
    print("Gyroscope:")
    print("x:", gx)
    print("y:", gy)
    print("z:", gz)

    # Sleep for a bit
    time.sleep(0.5)

