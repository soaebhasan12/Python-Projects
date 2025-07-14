import lxml
import smtplib
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

app_password = "utiipfxkrjaagwgf"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").getText().strip()

BUY_PRICE = 200.0


if price_as_float < BUY_PRICE:     
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("saibuhasan22@gmail.com", app_password)
        connection.sendmail(
            from_addr="saibuhasan22@gmail.com",
            to_addrs="soaebhasan04@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
    print("Email sent successfully!")
else:
    print("Price is too high. No email sent.")