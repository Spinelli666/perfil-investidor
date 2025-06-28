# Perfil do Investidor - Aplicação Django

Uma aplicação web desenvolvida em Django para determinar o perfil de investidor através de um questionário personalizado.

## Estrutura do Projeto

```
perfil-investidor/
├── venv/                    # Ambiente virtual Python
├── djangoapp/              # Pasta principal do projeto Django
│   ├── manage.py
│   ├── perfil_investidor/  # Configurações do projeto
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── questionario/       # Aplicação principal
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── tests.py
│       ├── static/         # Arquivos estáticos
│       │   └── css/
│       │       ├── base.css
│       │       ├── home.css
│       │       ├── questionario.css
│       │       ├── resultado.css
│       │       └── README.md
│       └── templates/
│           └── questionario/
│               ├── base.html
│               ├── home.html
│               ├── questionario.html
│               └── resultado.html
├── requirements.txt
└── README.md
```

## Características

- **Framework**: Django 5.2.3
- **Frontend**: Bootstrap 5.3.0 com design responsivo
- **CSS**: Estrutura modular separada em arquivos específicos
- **Perfis de Investidor**: Conservador, Moderado e Arrojado
- **Interface**: Design moderno com gradientes e animações
- **Arquivos Estáticos**: Organizados na pasta `static/css/`

## Como Executar

### 1. Configurar o Ambiente Virtual

```bash
# Na pasta principal do projeto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Executar Migrações

```bash
cd djangoapp
python manage.py migrate
```

### 3. Criar Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 4. Executar o Servidor

```bash
python manage.py runserver
```

### 5. Acessar a Aplicação

Abra seu navegador e acesse: `http://127.0.0.1:8000`

## Funcionalidades

### Página Inicial
- Design atrativo com apresentação dos perfis de investidor
- Botão para iniciar o questionário
- Cards informativos sobre os benefícios

### Questionário
- Template preparado para receber as perguntas
- Barra de progresso dinâmica
- Validação de preenchimento completo
- Design responsivo

### Resultado
- Exibição do perfil determinado
- Características detalhadas de cada perfil
- Recomendações de investimentos
- Sugestões de próximos passos

## Próximos Passos

Para completar a aplicação, você pode:

1. **Adicionar as perguntas específicas** no template `questionario.html`
2. **Implementar a lógica de cálculo** do perfil nas views
3. **Criar modelos** para armazenar respostas no banco de dados
4. **Adicionar autenticação** para usuários salvarem seus resultados
5. **Implementar relatórios** e histórico de questionários

## Tecnologias Utilizadas

- Python 3.x
- Django 5.2.3
- Bootstrap 5.3.0
- Bootstrap Icons
- HTML5/CSS3
- JavaScript

## Licença

Este projeto foi desenvolvido para fins educacionais e pode ser livremente utilizado e modificado.

## Estrutura CSS

O projeto utiliza uma arquitetura CSS modular com arquivos separados:

### Arquivos CSS
- **`base.css`**: Estilos globais (gradientes, navbar, cards, botões)
- **`home.css`**: Estilos específicos da página inicial
- **`questionario.css`**: Estilos do formulário de questionário
- **`resultado.css`**: Estilos da página de resultados

### Localização
Todos os arquivos CSS estão em: `djangoapp/questionario/static/css/`

### Como Funciona
- O template `base.html` carrega automaticamente `base.css`
- Cada template específico carrega seu CSS correspondente usando `{% block extra_css %}`
- Bootstrap 5.3 é usado como base, com customizações específicas

### Recursos Visuais
- Gradientes personalizados
- Animações suaves
- Hover effects
- Backdrop filters
- Temas coloridos por perfil de investidor