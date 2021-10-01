# Banco de imagens
Banco de imagens que suporta diferentes tipos de arquivos e permite fazer upload e download desses arquivos. Os arquivos devem ser salvos no disco do servidor (Sua máquina utilizada para o desenvolvimento representa o servidor).

## Rotas

> GET /download/<file_name>

- Faz download de um aquivo buscando pelo nome.

> GET /download-zip
- Faz download de uma pasta, usando query_params (file_extension, compression_ratio) para especificar o tipo de arquivo para baixar todos compactados e também a taxa de compressão.

    Ex: /download-zip?file_type=png&compression_rate=1

>GET /files
- Lista todos os arquivos sem filtro de tipo.

>GET /files/<extension>
- Lista todos os arquivosde acordo dom o tipo que foi especificado na url.

>POST /upload
- Tem a função de enviar um arquivo por um Multipart Form com o valor sendo o arquivo a ser enviado.