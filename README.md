# XATU - Bot de Automação no WhatsApp para Organização de Partidas de Futebol

## Visão Geral

XATU é um script em Python projetado para automatizar o processo de envio de mensagens de confirmação de presença em partidas de futebol no WhatsApp. O script utiliza a biblioteca pywhatkit para enviar mensagens instantâneas para contatos individuais ou grupos.

## Recursos

- Envia uma mensagem personalizável de confirmação de presença para um contato ou grupo específico.
- Permite a parametrização por meio de um arquivo `.env` para personalização fácil.
- Calcula automaticamente e seleciona a próxima sexta-feira como data padrão para o evento.

## Pré-requisitos

- Python 3.x instalado.
- Pip instalado.
- Pacotes Python necessários instalados. Instale as dependências usando:

    ```bash
    pip install python-dotenv pywhatkit pyautogui
    ```

## Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/seunome/seurepositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seurepositorio
    ```

3. Crie um arquivo `.env` no diretório raiz com os seguintes parâmetros:

    ```
    MODE="Modo de envio de mensagem (grupo ou contato)"
    CONTACT_ID="Número do WhatsApp ou ID do grupo"
    ```

4. Execute o script:

    ```bash
    python xatu.py
    ```

## Parâmetros

- **MODE**: Modo de envio de mensagem, pode ser "grupo" ou "contato".
- **CONTACT_ID**: Número do WhatsApp ou ID do grupo.

## Uso

- O script calculará automaticamente a data da próxima sexta-feira para a partida de futebol.
- A mensagem personalizável inclui detalhes como localização, data, horário, valor do pagamento antecipado, chave PIX e responsável pela chave PIX.
- Suporta o envio de mensagens para contatos individuais ou grupos com base no modo especificado.

## Agradecimentos

- Inspirado no Pokémon "Xatu" por suas previsões oportunas e automação.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
