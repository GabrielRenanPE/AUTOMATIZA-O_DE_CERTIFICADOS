# Automação de Geração e Envio de Certificados

Este projeto em Python automatiza a criação e envio de certificados personalizados para eventos, cursos e treinamentos, eliminando tarefas manuais e agilizando o processo.

## Descrição

A ideia central é utilizar um modelo de certificado em imagem e, por meio da manipulação automatizada, inserir dados específicos dos participantes. Após a criação dos certificados, o sistema realiza o envio individualizado via e-mail, garantindo rapidez e precisão na distribuição dos certificados.

## Funcionalidades

- **Leitura de Dados:**  
  Importa listas de participantes a partir de arquivos CSV ou Excel, utilizando a biblioteca [pandas](https://pandas.pydata.org/).

- **Geração Automática de Certificados:**  
  Utiliza a biblioteca [Pillow (PIL)](https://python-pillow.org/) para editar um modelo de certificado, inserindo dinamicamente nomes e outras informações personalizadas.

- **Exportação em PDF/JPG:**  
  Gera e salva os certificados automaticamente no formato desejado.

- **Envio Automático por E-mail:**  
  Utiliza a biblioteca [yagmail](https://github.com/kootenpv/yagmail) para enviar os certificados individualmente aos participantes.

- **Gerenciamento de Arquivos:**  
  Organiza e salva os certificados gerados utilizando o módulo [os](https://docs.python.org/3/library/os.html).

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Pandas:** Processamento e leitura de dados.
- **Pillow (PIL):** Manipulação de imagens para geração dos certificados.
- **Yagmail:** Automação do envio de e-mails.
- **OS:** Organização dos arquivos gerados.

## Benefícios

- **Automatização:** Elimina o trabalho manual na geração e envio de certificados.
- **Precisão:** Reduz erros e inconsistências no preenchimento de dados.
- **Agilidade:** Permite um envio rápido e eficiente para os participantes.
- **Organização:** Facilita o controle e a gestão dos certificados emitidos.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Como Utilizar

1. **Prepare os Dados:**  
   Organize um arquivo CSV ou Excel com os dados dos participantes.

2. **Configure o Modelo:**  
   Ajuste o modelo de certificado (imagem) definindo os campos que serão preenchidos automaticamente.

3. **Execute o Script Principal:**

   ```bash
   python main.py
   ```

## Contribuição

Contribuições são muito bem-vindas! Se você deseja sugerir melhorias ou implementar novas funcionalidades, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações ou dúvidas, entre em contato:

- **Email:** seu-email@example.com
- **LinkedIn:** [Seu Perfil](https://www.linkedin.com/in/seu-perfil/)

---

Esta estrutura ajuda a tornar o README mais claro, organizado e amigável para quem deseja utilizar ou contribuir com o projeto.
