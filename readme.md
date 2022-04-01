## Instalação

Use o "pip" para instalar as dependências necessárias do projeto

```bash
pip install -r requirements.txt
```

Ultilize o commando abaixo para gerar o arquivo executável que se encontrará na pasta "dist" :

```bash
pyinstaller --onefile  --exclude-module _bootlocale -w -F clean_temp.py
```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)