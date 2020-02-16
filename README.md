# aws-mfa-updater
Easily update profile information via [MFA Vitual Device](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_credentials_mfa_enable.html) to the Credentials file. 

Created to make the [AWS Toolkit](https://aws.amazon.com/ko/about-aws/whats-new/2018/11/introducing-aws-toolkit-for-pycharm/) easy to use

I tried to use the AWS Toolkit but my account had to be MFA certified.

There is already a well-designed tool like [link](https://gist.github.com/tokyowizard/f911c794a3e5ad260b54aeac430859f0)

But I wrote a script because I wanted the Credentials file to be automatically updated.

Update the following information in the `aws_mfa_updater.py` file as appropriate.
```python
PROFILE_NAME = 'infra'
ARN_OF_THE_MFA_DEVICE = 'MFA_DEVICE_SERIAL'
SESSION_DURATION = 50400
```

## Setup
```shell script
$ pip install -r requirements.txt
```

## Usage
Passing MFA Tokens as Parameters
```shell script
$ python aws_mfa_updater.py {MFA_TOKEN}
```
You can see the infra profile added to the `~/.aws/credentials` file.
```
[default]
aws_access_key_id = xxxx
aws_secret_access_key = xxxx

[infra]
aws_access_key_id = xxxx
aws_secret_access_key = xxxx
aws_session_token = xxxx
```