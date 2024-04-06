# VFS Appointment Bot

A script to check appointment slots for VFS.

By default, it runs every 2 minutes and check for visa slots at VFS website and notifies the user by SMS/call/Telegram. <br/>
The interval can be changed in the config.

## Usage

`python vfs_appointment_bot/vfs_appointment_bot.py`

** Please refer to the screenshot for more details regarding the inputs.

![VFS Appointment Form Screenshot](./assets/vfs-appointment-form.png)

## Dependencies

1. Install Firefox Browser on your machine if not already installed.
2. `geckodriver` (instructions to install geckodriver are written below)
3. Setup client for Twilio/Telegram or both:
    - Create an account on Twilio to get text and call alerts. Sign up [here](https://www.twilio.com/try-twilio) for a trial account to get credits upto worth $10, OR
    - Create a new bot via Telegram and add it to a chat group where you want it to post messages to notify you. Check [this simple tutorial out](https://medium.com/codex/using-python-to-send-telegram-messages-in-3-simple-steps-419a8b5e5e2) if you don't know how to create a new bot and get its credentials. Once bot is created you need to add its credentials in `config/config.ini` file.


## Installing geckodriver

1. Run these the commands:

    - Linux (as an example) : `wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz`

    (You can find the download URL to the latest release of geckodriver on Github. Check out [their latest release here](https://github.com/mozilla/geckodriver/releases) for your machine.)

2. Extract the file with

    `tar -xvzf geckodriver*`

3. Make it executable (note this shouldn't be necessary, unless the unzipped file doesn't have the execute bits set):

    `chmod +x geckodriver`

4. Add the driver to your PATH in ~/.bashrc so other tools can find it:

    `export PATH=$PATH:/path-to-extracted-file/geckodriver`



