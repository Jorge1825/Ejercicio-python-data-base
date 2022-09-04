    
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP
import modelo.users as users





class EnviarCorreo:
    
    def __init__(self,correoCliente="NULL@NULL.COM"):
        self.correoCliente = correoCliente
        self.contrasena = users.User("","",self.correoCliente).ConsultarPass()  

          
    def enviarCorreo(self):
        
        try:
            msg = MIMEMultipart("plain")
            msg["From"] = "pruebapersonal182@outlook.com"
            msg["To"] = self.correoCliente
            msg["Subject"] = "Recuperacion de contraseña MYNOTE"

            msg.attach(MIMEText("""Hemos detectado que presenta incovenientes para iniciar sesión en su cuenta MYNOTE.
                                \n A continuacion encontrará la contraseña de acceso a su cuenta MYNOTE.\n\nCONTRASEÑA: {0} \nGracias por utilizar nuestros servicios.\nCualquier duda o consulta no dude en contactarnos.
                                """.format(self.contrasena), 'plain'))
                                
            



            #adjntar una iamgen
            """ image_file = open(r'./Proyecto practico/modelo/img.jpg','rb').read()
            pic = MIMEImage(image_file)
            pic.add_header('Content-Disposition','attachment',filename='mynote.jpg')
            msg.attach(pic) """
            
            
            
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
        
        
        
            

            smtp = SMTP("smtp.office365.com", 587)
            smtp.starttls()
            smtp.login("pruebapersonal182@outlook.com", "1825Jorge")
            smtp.sendmail("pruebapersonal182@outlook.com",
                        self.correoCliente, msg.as_string())
            smtp.quit()
            
            print("\n==================================================================")
            print("Correo enviado,por favor verifique su bandeja de entrada o de spam")
            print("==================================================================")

        except:
            print("Critical error, sistema no disponible")




