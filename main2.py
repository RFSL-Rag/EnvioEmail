import smtplib
from email.mime.text import MIMEText as mt
from email.mime.multipart import MIMEMultipart as mp

def enviar_email():
  try:
    remetente="ronaldinhotestes@gmail.com"
    senha="wzbm nqsk hxpf irgj"
    destinatario="prof.altamira13@gmail.com"

    titulo="Importando Bibliotecas - Ronaldo Figueiredo Simões Leal"
    mensagem=mp()
    mensagem["From"]=remetente
    mensagem["To"]=destinatario
    mensagem["Subject"]=f"{titulo}"
    

    corpo_email="""\
    <html>
      <body>

      <header>
        <h1>
          Trabalho de Python sobre envio de e-mails.
        </h1>
        <p>
          O programa tem a função de ensinar sobre a importação de bibliotecas e funções específicas, assim como a tarefa de enviar um e-mail possuindo uma tabela formatada em html.
        </p>
        <p>
          O motivo do envio deste e-mail é para validação do trabalho e como foi solicitado na documentação.
        </p>
      </header>
        <table border = "1">
          <tr>
            <th> Biblioteca </th>
            <th> Função </th>
          </tr>
          <tr>
            <td> smtplib</td>
            <td> Biblioteca que permite utilizar o protocolo SMTP para envios de e-mail</td>
          </tr>
          <tr>
            <td> email.mime.text </td>
            <td>Sua principal função é criar objetos de e-mail com conteúdo de texto</td>
          </tr>
          <tr>
            <td> email.mime.multipart </td>
            <td> Utilizado para criar e-mails com múltiplas partes (ou seções), permitindo que um e-mail contenha diferentes tipos de conteúdo, como texto simples, HTML e anexos.</td>
          </tr>
        </table>
        <br>

        <img src= "https://i.cbc.ca/1.6713656.1679693029!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/this-is-fine.jpg" />
      </body>
    </html>
    """
  
    mensagem.attach(mt(corpo_email, "html"))

    servidor = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print("O e-mail foi enviado com sucesso!")

  except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação! Verifique o e-mail e a senha.")
  
  except smtplib.SMTPConnectError:
    print("Falha de conexão! Não foi possível se conectar ao servidor SMTP.")

  except smtplib.SMTPDataError:
    print("Erro ao enviar os dados do e-mail.")

  except Exception as e:
    print(f"Erro ao enviar o email: {str(e)}")
  
  finally:
    try:       
      servidor.quit()
    
    except:
      pass


enviar_email()
