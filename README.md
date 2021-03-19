<<<<<<< HEAD
# Aeroponics System
## NCSU Sweetpotato Breeding Group 2019


### Purpose

A library to designed to automate and optimize sweetpoato cutting growth in a greenhouse aeroponics system.


### Materials

**Aeroponic System**
- Large plastic tub
- High pressure pump
- Plumbing material
- Teejet spray tip
- Styrafoam

**Electronics**
- RaspberryPi with onboard wifi
- DHT22 Temperature and Humidity Sensor
- Photoresistor
- i2c analog to digital converter
- 1N4001 Flyback Diode
- 12v DC Powersupply

### Methods

**Setup**
1. Download the most current version of [Raspbian-Light ] (https://www.raspberrypi.org/downloads/raspbian/)
      -Full Raspbian will work but light is recommended to prevent excessive background processes and high heat on the processor

2. Copy the unzipped .img file onto a microSD card with atleast 4gb of memory
      - For Windows and Mac [balenaEtcher] (https://www.balena.io/etcher/) is recommended
      - Linux users can install by running the following command with the proper path to the .img, substituting sdX for the correct mount location of the microSD (check via 'lsblk'), and root privileges. Don't run dd unless you are sure you're calling the correct locations.
      - `dd bs=4M if=~/Downloads/2019-09-26-raspbian-buster-lite.img of=/dev/sdX conv=fsync`

3. Remove the flashed microSD and reinsert it into the computer. Navigate to the new /boot folder.

4. Create a file to enable ssh on boot. This allows remote login to send commands over the intranet.
      - **Windows & Mac** use a file browser, right click in /boot/ and create a new text file, leave it empty, and save as "ssh" removing any file extensions such as .txt
      - **Linux** run `touch ssh` from command line in the mounted /boot/ directory

5. Configure the wifi network. These settings should work for most networks. Contact your network administrator if you are unsure.
      - **Windows and Mac** right click and create a file with the following contents, save as wpa_supplicant.conf in /boot/
      - **Linux** run the command `sudo nano wpa_supplicant.conf` from the correct directory and enter the following. Use ctrl + o and ctrl + x to write the file and exit
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
     ssid="Your network name/SSID"
     psk="Your WPA/WPA2 security key"
     key_mgmt=WPA-PSK
}
```
  - The pi will write these values in the correct directory on first boot

6. Unmount the microSD and insert it into the Pi. Apply 5v of power through the microUSB port and wait 2 minutes for the pi to run its initial boot process.

7. Log into your router to check attached devices and identify the Pi's IP Address. We will use this to remotely log in.
    - Alternatively you can boot the Pi with a monitor attached and run the command `ifconfig` and search for the line below wlan0 that writes out `inet X.X.X.X`
    - If wifi is not an option for initial set up, ssh over usb is possible but not yet tested.

8. From a bash terminal (Mac or Linux) or Windows 10 command line run `ssh pi@IP_ADDRESS` with IP_ADDRESS being replaced with the IP found earlier. All commands entered in this terminal from here on will be executed on the Pi. If the session is terminated, an ssh connection must be reestablished.

9. The default login credentials for the Pi is **pi** and the password is **raspberry**.

10. For security the password should be changed by running `sudo passwd` and following the prompts. The characters you type will not appear on the screen but they are being recorded.

11. Update your respositories and upgrade software to the latest versions with
```
sudo apt-get update
sudo apt-get upgrade
```
12. Most software needed for this project comes on the Pi by default, but we will need to use github to download the code. Run:
```
sudo apt-get install git
sudo git clone (Copy and Paste the gitURL from this page)
```
13. Install pip to download neccesary libraries for running the sensors. In this example we will be using python3.
 ```
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip3 install --upgrade pip3 setuptools wheel
```
14. Install the required libraries on the Pi.
```
sudo pip3 install Adafruit_DHT

```

15. This project uses Google Drive and Google Sheets API to record data directly to the cloud. This is technically an optional step but it is by far the best free option to be able to log data long term and remotely check the status of the aeroponics system.
      -First we must acquire a license from a developer account to use Google's back end services. This can be a complicated process but is documented extensively through [this spreeadsheet guide] (http://gspread.readthedocs.org/en/latest/oauth2.html) and [Google's documentation] (https://developers.google.com/identity/protocols/OAuth2)
      - Once logged in to Google's Developer API, create a project, and navigate to the OAUTH screen and create a new  Service Account Key. This will create a .json file you will need to download and put in to the working directory of the project. Our code will pull the email address Google created to communicate with the backend of our spreadsheet.


sudo pip3 install gspread oauth2client

13. Set the code to Autostart.
=======
# aeroponics
>>>>>>> 10307f311cfcec86922bf124526ae6f7f3cd9c3d
