
# Decoy

Python program that was created to mitigate damages caused by laptop and computer theft which often lead to personal information being exposed. Due to Google Chrome's password autosave feature, we have reason to believe that unauthorized accessors would instinctively open a browser such as Google Chrome to access personal information. To combat this, Decoy conceals itself as a web browser in plain sight in the hopes of catching unauthorized usage. 
## Features

- Location detection of unauthorized access (IP address, City, Longitude, Latitude)
- Webcam access to take picture of unauthorized accessor
- Email notification upon unauthorized access
- Slack notifications of unauthorized usage


## Installation

Install Python dependencies

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SLACK_URL`

`EMAIL_USERNAME`

`EMAIL_PASSWORD`

## Deployment

To deploy Decoy run

```bash
  python app.py
```


## Authors

- [@JackyL0218](https://github.com/JackyL0218)
- [@ansonwong250](https://github.com/ansonwong250)
- [@jacky-h-nguyen](https://github.com/jacky-h-nguyen)

