import hashlib
import pandas as pd

class CertificateVerifier:
    def __init__(self):
        self.hashes_file = "certificate_hashes.csv"
        
    def verify(self, cert_path):
        """Verifica a autenticidade do certificado"""
        try:
            # Calcular hash atual
            current_hash = self.calculate_hash(cert_path)
            
            # Buscar no registro
            df = pd.read_csv(self.hashes_file)
            match = df[df["Hash"] == current_hash]
            
            if not match.empty:
                print("\n✅ Certificado válido!")
                print(f"Nome: {match['Nome'].values[0]}")
                print(f"Email: {match['Email'].values[0]}")
                print(f"Hash completo: {current_hash}")
            else:
                print("\n⚠️ Certificado não reconhecido ou alterado!")

        except FileNotFoundError:
            print("Erro: Arquivo de registro não encontrado!")
        except Exception as e:
            print(f"Erro na verificação: {str(e)}")

    def calculate_hash(self, file_path):
        """Calcula hash do arquivo"""
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

if __name__ == "__main__":
    verifier = CertificateVerifier()
    certificado = input("Digite o caminho completo do certificado: ").strip()
    
    if os.path.exists(certificado):
        verifier.verify(certificado)
    else:
        print("Erro: Arquivo não encontrado!")
