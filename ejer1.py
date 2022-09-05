from mailjet_rest import Client
import os
api_key = '5b31c4ecaf1a928e06c296724708a8e3'
api_secret = '7aaef943931c72a0bf57b4c16081b3c3'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "jlroa82@misena.edu.co",
        "Name": "Jorge Luis"
      },
      "To": [
        {
          "Email": "jlroa82@misena.edu.co",
          "Name": "Jorge"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())






            
                
                htmlFile = """\
                <html>
                    <head></head>
                    <body>
                    <br>
                    <br>
                        <img src="cid:image1">
                        
                    </body>
                </html>
                """
                htmlpart = MIMEText(htmlFile,'html','utf-8')
                msg.attach(htmlpart)

                #Muestra imágenes en el cuerpo
                imagenDirectory = './Proyecto practico/modelo/img/img.png'
                image = MIMEImage(open(imagenDirectory,'rb').read(),imagenDirectory.split('.')[-1])
                # Definir ID de imagen, citar en texto HTML
                image.add_header('Content-ID','<image1>')
                msg.attach(image)
            
            



