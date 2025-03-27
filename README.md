Projeto: Automação de Geração e Envio de Certificados

Descrição:
Este projeto em Python visa automatizar o processo de criação e envio de certificados personalizados para eventos, cursos e treinamentos. 
Ele utiliza um modelo de certificado em imagem, preenche dinamicamente os dados dos participantes e realiza o envio automático por e-mail.

Funcionalidades:
Leitura de Dados: Importação de uma lista de participantes a partir de um arquivo CSV ou Excel usando pandas.
Geração Automática de Certificados: Uso da biblioteca PIL (Pillow) para editar um modelo de imagem e inserir os nomes dos participantes e outras informações personalizadas.
Exportação em Arquivo PDF/JPG: Os certificados são gerados e salvos automaticamente no formato desejado.
Envio Automático por E-mail: Utilização da biblioteca yagmail para enviar os certificados individualmente via e-mail.
Gerenciamento de Arquivos: Uso do módulo os para organizar e salvar os certificados gerados.

Tecnologias Utilizadas:
PIL (Pillow) → Manipulação de imagens e inserção de texto nos certificados.
Pandas → Leitura e processamento de dados de participantes a partir de arquivos CSV ou Excel.
Yagmail → Envio automático de e-mails com os certificados anexados.
OS → Gerenciamento e organização dos arquivos gerados.

Benefícios:
Eliminação do trabalho manual na geração de certificados.
Redução de erros e inconsistências no preenchimento.
Agilidade no envio automático para os participantes.
Organização e controle eficiente dos certificados emitidos.
