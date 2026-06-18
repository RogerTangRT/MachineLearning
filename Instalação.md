# Instalação do Ambiente Jupter

1. Instalar Python (se não tiver)
Baixe de python.org
Marque "Add Python to PATH" durante a instalação
2. Instalar Jupyter via terminal
Abra o terminal do VS Code (Ctrl+`) e execute:
``` Console
pip install jupyter notebook ipykernel
```
3. Instalar a extensão Jupyter no VS Code
Abra o VS Code
Vá para Extensions (Ctrl+Shift+X)
Procure por "Jupyter"
Instale a extensão oficial da Microsoft

4. Configurar o kernel Python
No terminal do VS Code, execute:
```Console
python -m ipykernel install --user
```
5. Abrir/criar notebooks
Abra qualquer arquivo .ipynb (como seus arquivos 0203b.ipynb, etc.)
VS Code pedirá para selecionar um kernel
Selecione o Python que acabou de instalar
Pronto! Você pode executar as células
```Console
pip install --user jupyter
```
