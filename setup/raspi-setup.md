# flash sd card
`rpi-imager`
- raspbian os
- enable ssh, add wifi credentials
- user roombanator

# on local

```
hostname -I
nmap -sn 192.168.XXX.0/24
ssh roombanator@192.168.XXX.YYYY
```

# on raspi

## enable UART
(see https://raspberrytips.com/enable-uart-on-raspberry-pi/) 

```
sudo raspi-config
```
    > Select Interface Options 
    > Serial Port 
    > Yes (enable Serial Port and Console)

 
## setup code
```
cd ~
git clone https://github.com/FlurinArner/anand-hackathon.git
cd anand-hackathon
python3 -m venv .venv
. .venv/bin/activate
which python
which pip
pip install --upgrade pip
pip install -r requirements.txt
```

## ensure autostart
```
crontab -e
```
select editor, then add a line with
```
@reboot /home/roombanator/anand-hackathon/.venv/bin/python /home/roombanator/anand-hackathon/src/main.py 
```

verify with 
```
crontab -l
```

## transfer SD

finally, shutdown and move flash to installed hardware
```
sudo shutdown -h now
```

and POWER ON!
