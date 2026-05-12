# curl -s -X POST \
#   'https://www.google.com/maps/_/MapsWizUi/data/batchexecute?rpcids=Qt4aBe&source-path=%2Fmaps%2Fsearch%2FUnited%2BKingdom%2BBusiness%2B%2526%2BInformation%2BConsultant%2F%4052.3864051%2C-3.8193502%2C7z%2Fdata%3D!3m1!4b1&hl=en&_reqid=980576&rt=c' \
#   -H 'authority: www.google.com' \
#   -H 'accept: */*' \
#   -H 'accept-language: en,hi;q=0.9' \
#   -H 'content-type: application/x-www-form-urlencoded;charset=UTF-8' \
#   -H 'origin: https://www.google.com' \
#   -H 'referer: https://www.google.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Linux"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36' \
#   -H 'x-same-domain: 1' \
#   -H 'x-maps-diversion-context-bin: CAE=' \
#   --cookie 'SID=g.a0008ghks0Oyy2_op92BC94cVPYiVr53lWqUFy-eNBQbIvOvUe1HzhPam48IFAaS7DxuP2790gACgYKAawSARASFQHGX2Mi5l11INPIHTBCtX5T03sTFBoVAUF8yKoeP1a-czLmJaW1UdYbwebY0076; HSID=AZqPSwlN15cSRywqs; SSID=ALAHdBF1_TTru5-Ki; APISID=sj2em1SqG9nNpsbt/A_eSF3nyUUuRYj7PD; SAPISID=CANuvst001-B2BjK/AFB673oCK7-NK35GZ' \
#   --data-urlencode 'f.req=[[["/MapsLocationSharingService.GetState","[2,[\"ZNr0aeuwDrWQseMPoYHhiQE\",null,null,null,null,null,81,null,null,null,null,null,null,null,312733],null,null,null,null,\"GiwAhp/Fo1afshD33v6fyTjTwVvQra1iYShZq1jH4BrdZiIFonAGHeqhZ3jhMA==\"]",null,"generic"]]]' \
#   --data-urlencode 'at=AOIuZIX9KOEFY3d_EVY_3ZsipoVc:1777654372269' \
#   --compressed \
#   -o response.json && echo "✅ Done!" && cat response.json

curl -s -X POST \
  'https://www.google.com/maps/_/MapsWizUi/data/batchexecute?rpcids=Qt4aBe&hl=en&rt=c' \
  -H 'content-type: application/x-www-form-urlencoded;charset=UTF-8' \
  -H 'origin: https://www.google.com' \
  -H 'referer: https://www.google.com/maps/search/United+Kingdom+Business+%26+Information+Consultant/' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36' \
  -H 'x-same-domain: 1' \
  --cookie 'SID=g.a0008ghks0Oyy2_op92BC94cVPYiVr53lWqUFy-eNBQbIvOvUe1HzhPam48IFAaS7DxuP2790gACgYKAawSARASFQHGX2Mi5l11INPIHTBCtX5T03sTFBoVAUF8yKoeP1a-czLmJaW1UdYbwebY0076; HSID=AZqPSwlN15cSRywqs; SSID=ALAHdBF1_TTru5-Ki; APISID=sj2em1SqG9nNpsbt/A_eSF3nyUUuRYj7PD; SAPISID=CANuvst001-B2BjK/AFB673oCK7-NK35GZ' \
  --compressed \
  -o response2.json && echo "✅ Done!" && cat response2.json