import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org/messages",
        auth=("api", "8598ba9cde175f797c60edb63230e8a3-102c75d8-ae039287"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxdf0686a9196242e6bc7cfd605a329a55.mailgun.org>",
              "to": "ZhangCary250@gmail.com",
              "subject": "Hello Cary Zhang",
              "text": "Congratulations Cary Zhang, you just sent an email with Mailgun! You are truly awesome!"})


if __name__ == "__main__":
    send_simple_message()
