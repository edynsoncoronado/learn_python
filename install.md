# Install Python3.8
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
```

**How to update default Python version on Ubuntu?**
1. To view the different versions on your computer:
```
ls /usr/bin/python*
```
2. Copy the version you want. I my case, I copied /usr/bin/python3.8
3. Open .barshrc file and scroll to the end. Paste the copied python version on the last line. 
```
alias python = “usr/bin/python3.8”
```
