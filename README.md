# Aeroponics System
### NCSU Sweetpotato Breeding Group 2019

**Purpose**
A library to designed to automate and optimize sweetpoato cutting growth in a greenhouse aeroponics system. 

**Materials**
### Aeroponic System
- Large plastic tub
- High pressure pump
- Plumbing material
- Teejet Spraytip
- Styrafoam

### Electronics
- RaspberryPi with onboard wifi
- DHT22 Temperature and Humidity Sensor
- Photoresistor
- i2c analog to digital converter
- 1N4001 Flyback Diode
- 12v DC Powersupply

**Methods**
### Setup
1. Download the most current version of [Raspbian-Light ] (https://www.raspberrypi.org/downloads/raspbian/)
      -Full Raspbian will work but light is reccommended to prevent excessive background processes and high heat on the processor
2. Copy the unzipped .img file onto a microSD card with atleast 4gb of memory
      - For Windows and Mac [balenaEtcher] (https://www.balena.io/etcher/) is reccomended
      - Linux users can install by running the following command with the proper path to the .img, substituting sdX for the correct mount location of the microSD (check via 'lsblk'), and root priviledges. Don't run dd unless you are sure you're calling the correct locations.
      `dd bs=4M if=~/Downloads/2019-09-26-raspbian-buster-lite.img of=/dev/sdX conv=fsync`
3. Unplug the flashed microSD and reinsert it into the computer. Navigate to the new /boot folder.
4. Create a file to enable ssh on boot. This allows remote login to send commands over the intranet.
      - Windows & Mac use a file browser, right click in /boot/ and create a new text file, leave it empty, and save as "ssh" removing any file extensions such as .txt
      - Linux run `touch ssh` from command line in the mounted /boot/ directory
5. Configure the wifi network. These settings should work for most networks. Contact your network administrator if you are unsure. 
      - Windows and Mac right click and create a file with the following contents, save as wpa_supplicant.conf in /boot/
      - Linux run the command `sudo nano wpa_supplicant.conf` from the correct directory and enter the following. Use ctrl + o and ctrl + x to write the file and exit
      ```
      {
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
     ssid="Your network name/SSID"
     psk="Your WPA/WPA2 security key"
     key_mgmt=WPA-PSK
}
}
      ``` 
      - The pi will write these values in the correct directory on first boot
6. Unmount the microSD and insert it into the Pi. Apply 5v of power through the microUSB port and wait 2 minutes for the pi to run its initial boot process. 
7. Log into your router to check attached devices and identify the Pi's IP Address. We will use this to remotely log in.
  - Alternatively you can boot the Pi with a monitor attached and run the command `ifconfig` and search for the line below wlan0 that writes out `inet X.X.X.X`
  - If wifi is not an option for initial set up, ssh over usb is possible but not yet tested. 
8. From a bash terminal (Mac or Linux) or Windows 10 command line run `ssh pi@IP_ADDRESS` with IP_ADDRESS being replaced with the IP found earlier
9. The default for the Pi is **pi** and the password is **raspberry**. Use these to log in initially.
10. For security the password should be changed by running `sudo passwd` and following the prompts.
11. Update your respositories and upgrade software to the latest versions with 
```
sudo apt-get update
sudo apt-get upgrade
```
12. Most software needed for this project comes on the Pi by default, but we will need to use github to download the code. Run
```
sudo apt-get install git
sudo git clone (Copy and Paste the gitURL from this page)
```
13. Set the code to Autostart.
