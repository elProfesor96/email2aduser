# email2aduser

## Description

Email list parser to AD user common format. 

Common format: sharon.r.whorthy@example.com -> swhorthy

Common format: sharon.whorthy@example.com   -> swhorthy

Common format: swhorthy@example.com         -> swhorthy


Great for REDTEAM when you have a lot of emails from OSINT tools 
and need to get AD userformat for bruteforce or spraying or 
connecting to external/internal services, etc.

## Manual use from git clone

- Print help msg
```bash
python3 email2aduser.py -h
```
or
```bash
chmod +x email2aduser.py
./email2aduser.py -h
```
- Usage:
```bash
./email2aduser -f input_file.txt -o output_file.txt
```

## Automatic install

- From https://github.com/elProfesor96/email2aduser/releases , download .deb latest release
```bash
sudo apt update
sudo apt install ./email2aduser-latest-release.deb
```
```bash
email2aduser -h
```


