# Arquivos CSS - Perfil do Investidor

Este projeto utiliza uma estrutura de CSS modular e organizada. Todos os arquivos CSS estão localizados em:
`djangoapp/questionario/static/css/`

## Estrutura de Arquivos CSS

### 1. **base.css**
- **Propósito**: Estilos globais e base para toda a aplicação
- **Contém**:
  - Gradiente de fundo do body
  - Estilos para navbar
  - Estilos base para cards
  - Botões primários
  - Footer
  - Seção hero

### 2. **home.css**
- **Propósito**: Estilos específicos para a página inicial
- **Contém**:
  - `.home-hero` - Card principal da home com backdrop filter
  - `.home-features` - Seção de recursos com hover effects
  - `.profile-type-icon` - Ícones dos tipos de perfil
  - `.feature-icon` - Ícones dos recursos
  - `.btn-start-quiz` - Botão especial para iniciar questionário
  - `.time-estimate` - Seção de tempo estimado
  - `.profile-showcase` - Área de exibição dos perfis

### 3. **questionario.css**
- **Propósito**: Estilos específicos para a página do questionário
- **Contém**:
  - `.questionario-container` - Container principal
  - `.questionario-card` - Card principal com backdrop filter
  - `.questionario-header` - Cabeçalho com gradiente
  - `.progress-section` - Seção da barra de progresso
  - `.question-container` - Container das perguntas
  - `.question-example` - Exemplo de pergunta com borda tracejada
  - `.form-check` - Estilos para radio buttons com hover
  - `.question-navigation` - Área de navegação
  - `.info-cards` - Cards informativos
  - `.btn-submit-disabled` - Estado desabilitado do botão

### 4. **resultado.css**
- **Propósito**: Estilos específicos para a página de resultado
- **Contém**:
  - `.resultado-container` - Container principal
  - `.resultado-card` - Card principal do resultado
  - `.resultado-header` - Cabeçalho com gradiente verde
  - `.profile-icon` - Ícone grande do perfil
  - `.profile-title` - Título do perfil
  - `.profile-characteristics` - Características por perfil (conservador, moderado, arrojado)
  - `.recommendations-grid` - Grid de recomendações
  - `.recommendation-card` - Cards de recomendação
  - `.recommendation-title` - Títulos coloridos por tipo
  - `.action-buttons` - Área dos botões de ação
  - `.next-steps-card` - Card dos próximos passos
  - `.step-icon` e `.step-item` - Estilos dos passos

## Como Usar

### 1. **Template Base**
O arquivo `base.html` carrega automaticamente o `base.css`:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/base.css' %}">
```

### 2. **Templates Específicos**
Cada template carrega seu CSS específico no bloco `extra_css`:
```html
{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/home.css' %}">
{% endblock %}
```

## Funcionalidades CSS

### 1. **Gradientes**
- Body: Gradiente diagonal azul/roxo
- Botões: Gradientes personalizados
- Cards: Backdrop filter com transparência

### 2. **Animações**
- Hover effects em cards
- Transições suaves em botões
- Transform effects nos elementos interativos

### 3. **Responsividade**
- Todos os estilos são responsivos
- Uso de classes Bootstrap complementadas com CSS customizado
- Grid system do Bootstrap mantido

### 4. **Temas por Perfil**
- **Conservador**: Verde (#28a745)
- **Moderado**: Amarelo/Laranja (#ffc107)
- **Arrojado**: Vermelho (#dc3545)

## Manutenção

Para adicionar novos estilos:

1. **Estilos globais**: Adicione em `base.css`
2. **Estilos específicos**: Crie/edite o arquivo CSS correspondente à página
3. **Novos templates**: Crie um novo arquivo CSS e referencie no template

## Estrutura de Classes

### Convenções de Nomenclatura:
- `.page-specific-container` - Containers principais
- `.component-name` - Componentes específicos
- `.element-modifier` - Modificadores de elementos
- `.state-disabled` - Estados especiais

Esta estrutura garante manutenibilidade, organização e facilita futuras atualizações do design.
