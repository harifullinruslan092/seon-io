import requests
import json
import webbrowser
import config as conf



headers = {
    'X-API-KEY': conf.LICENSE_KEY
}

payload = {
    "config": {
        "ip": {
          "include": "flags,history,id",
          "version": "v1.1"
        },
        "email": {
          "include": "flags,history,id",
          "version": "v2.2"
        },
        "phone": {
          "include": "flags,history,id",
          "version": "v1.4"
        },
        "ip_api": True,
        "email_api": True,
        "phone_api": True,
        "device_fingerprinting": True,
    },
    "ip": "143.176.244.94",
    "action_type": "account_register",
    "affiliate_id": "",
    "affiliate_name": "",
    "email": "trachsofiia@gmail.com",
    "email_domain": "gmail.com",
    "password_hash": "4545dhfusdhufh34#$@3hjhjshfjdasdasd234@#@3hjhsdjhsj@3hjh",
    "user_fullname": "Trach Sofiia",
    "user_name": "Sofiia",
    "user_id": "",
    "transaction_id": "",
    "user_dob": "",
    "user_category": "",
    "user_account_status": "",
    "user_created": "",
    "user_country": "NL",
    "user_city": "Leersum",
    "user_region": "Utrecht",
    "user_zip": "3956",
    "user_street": "Utrechtse Baan",
    "user_street2": "",
    "session": "84266fdbd31d4c2c6d0665f7e8380fa3",
    "phone_number": "31620820038",
    "transaction_type": "",
    "bonus_campaign_id": "",
    "merchant_id": "",
    "details_url": "",
    "custom_fields": {
    }
}



response = requests.post(conf.API_LINK, headers=headers,
                         data=json.dumps(payload))



print(response.json())
