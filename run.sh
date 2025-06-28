#!/bin/bash

# Script para executar o projeto Perfil do Investidor
# Uso: ./run.sh

echo "🚀 Iniciando Perfil do Investidor..."

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado. Criando..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
fi

# Ativar ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📦 Instalando/verificando dependências..."
pip install -r requirements.txt

# Ir para o diretório do Django
cd djangoapp

# Executar migrações
echo "🗄️ Executando migrações..."
python manage.py migrate

# Executar servidor
echo "🌐 Iniciando servidor Django..."
echo "📱 Acesse: http://127.0.0.1:8000"
echo "🛑 Para parar o servidor, pressione Ctrl+C"
python manage.py runserver
