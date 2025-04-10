from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import yagmail
import os

# Configurar suas credenciais
EMAIL_USUARIO = "anthonny6613@gmail.com"  # <---- Altere para seu e-mail do Gmail
SENHA_APP_GMAIL = "efax lhna yffa dfhr"  # <---- Use uma senha de aplicativo gerada no Google

class EditCertificate:
    """Classe que cria certificado dinamicamente e envia por email"""

    def __init__(self):
        if not os.path.exists("lista_alunos.xlsx"):
            raise FileNotFoundError("Erro: Arquivo 'lista_alunos.xlsx' não encontrado!")

        if not os.path.exists("template.png"):
            raise FileNotFoundError("Erro: Arquivo 'template.png' não encontrado!")

        self.read_data()
        self.send_email_with_certificate()

    def read_data(self):
        """Lê os dados da planilha Excel"""
        self.df = pd.read_excel("lista_alunos.xlsx")

    def send_email_with_certificate(self):
        """Percorre a lista e gera certificados para cada aluno"""
        for _, row in self.df.iterrows():
            name = row["Nome"]
            email = row["Email"]

            try:
                # Gerar o certificado
                certificate_image = self.create_certificate(name)

                # Enviar e-mail
                self.send_email_generic(name, email, certificate_image)

            except Exception as e:
                print(f"Erro ao processar {name}: {e}")

    def create_certificate(self, name):
        """Cria um certificado personalizado"""
        try:
            imagem = Image.open("template.png")
            draw = ImageDraw.Draw(imagem)

            # Verificar se a fonte existe antes de carregar
            font_path = "calibrib.ttf"
            if not os.path.exists(font_path):
                raise FileNotFoundError(f"Erro: Fonte '{font_path}' não encontrada!")

            font = ImageFont.truetype(font_path, 150)

            # Adicionar o nome ao certificado
            draw.text((625, 950), name, font=font, fill=(0, 0, 0))

            # Salvar o certificado
            certificate_image = f"Certificado_{name}.png"
            imagem.save(certificate_image)
            return certificate_image

        except Exception as e:
            raise Exception(f"Erro ao gerar certificado para {name}: {e}")

    def send_email_generic(self, name, email, certificate_image):
        """Envia o certificado por e-mail"""
        try:
            usuario = yagmail.SMTP(user=EMAIL_USUARIO, password=SENHA_APP_GMAIL)

            assunto = "Certificado de Participação - Evangelizando o SQL"
            conteudo = (
                f"Olá {name},\n\nAqui está o seu certificado de participação. "
                f"\n\nAtenciosamente,\nAdministração Evangelizando SQL"
            )

            usuario.send(
                to=email,
                subject=assunto,
                contents=conteudo,
                attachments=certificate_image,
            )

            print(f"✅ Email enviado para {email} com sucesso!")

        except Exception as e:
            print(f"⚠️ Erro ao enviar email para {email}: {e}")

# Iniciar o processo
start = EditCertificate()

