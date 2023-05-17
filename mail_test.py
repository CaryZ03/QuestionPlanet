import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org/messages",
        auth=("api", "key-768b5b09ca15e3c73881617406651be8"),
        data={"from": "Excited User <mailgun@sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org>",
              "to": "ZhangCary250@gmail.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})


if __name__ == '__main__':
    send_simple_message()
