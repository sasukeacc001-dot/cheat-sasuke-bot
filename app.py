from flask import Flask, render_template_string

app = Flask(__name__)

config = {
    "site_name": "Cheat Sasuke Glory Bot",
    "whatsapp": "94756242612",
    "group_link": "https://chat.whatsapp.com/JuvaI7lb9cX7sxIkzoHth7",
    "credit_price": 1300
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #000; color: #fff; text-align: center; font-family: sans-serif; padding: 20px; }
        .card { border: 2px solid #ff4500; border-radius: 15px; padding: 20px; background: #111; max-width: 400px; margin: auto; }
        .btn-topup { background: #25D366; color: #fff; padding: 15px; display: block; text-decoration: none; border-radius: 10px; font-weight: bold; margin-top: 20px; }
        .price { color: #ff4500; font-size: 24px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🔥 {{ c.site_name }} 🔥</h1>
    <div class="card">
        <p class="price">1 CREDIT = {{ c.credit_price }} LKR</p>
        <input type="text" placeholder="Guild ID" style="width:90%; padding:10px; margin-bottom:10px; border-radius:5px; border:none;">
        <select style="width:96%; padding:10px; margin-bottom:10px; border-radius:5px;"><option>Singapore Server</option></select>
        <button style="width:100%; padding:12px; background:#ff4500; border:none; color:#000; font-weight:bold; border-radius:5px; cursor:pointer;">PLACE ORDER</button>
        
        <a href="https://wa.me/{{ c.whatsapp }}?text=Hello%20Admin,%20I%20want%20to%20buy%201%20Credit%20for%201300%20LKR" class="btn-topup">
            💰 TOP-UP VIA WHATSAPP
        </a>
    </div>
    <br>
    <a href="{{ c.group_link }}" style="color:#25D366; text-decoration:none; font-weight:bold;">Join WhatsApp Group</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, c=config)

if __name__ == "__main__":
    app.run()
