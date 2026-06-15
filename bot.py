import requests

def send_alert(data):
    # Apna Token aur Chat ID yahan update karein
    token = "YOUR_TOKEN_HERE"
    chat_id = "YOUR_CHAT_ID_HERE"
    msg = f"🚨 **Zone Detected!**\nSymbol: {data['Symbol']}\nType: {data['Type']}\nProximal: {data['Proximal']:.2f}\nDistal: {data['Distal']:.2f}"
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}&parse_mode=Markdown")
