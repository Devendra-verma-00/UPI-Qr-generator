import qrcode

upi_id= input("Enter your UPI Id for grnerate QR :")

phone_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20 Name&mc=1234 '
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20 Name&mc=1234 '
google_pay_url= f"upi://pay?pa={upi_id}&pn=Recipient%20 Name&mc=1234 "

phone_pay_url=qrcode.make(phone_pay_url)
paytm_url=qrcode.make(paytm_url)
google_pay_url=qrcode.make(google_pay_url)


phone_pay_url.save('phone_pay_Qr.png')
paytm_url.save('paytmQr.png')
google_pay_url.save('googlePayQr.png')


phone_pay_url.show()
paytm_url.show()
google_pay_url.show()