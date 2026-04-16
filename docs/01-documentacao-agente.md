# 📄 Documentação do Agente — Grana.ai

## Caso de Uso

### Problema
Muitas pessoas têm acesso aos seus dados financeiros, como extratos e históricos de transações, mas não conseguem transformar essas informações em decisões práticas.

Elas não sabem identificar padrões de gasto, entender se estão economizando corretamente ou prever quando vão atingir seus objetivos financeiros.

👉 O problema não é falta de dados, mas falta de interpretação.

---

### Solução
O Grana.ai resolve esse problema ao combinar análise de dados com inteligência artificial para gerar insights claros e acionáveis.

O sistema:
- Processa dados financeiros reais (CSV/JSON)
- Calcula saldo, média de gastos e economia mensal
- Estima o tempo necessário para atingir metas financeiras
- Utiliza IA para traduzir esses dados em linguagem simples

👉 Além de responder perguntas, o agente gera insights proativos sobre o comportamento financeiro do usuário.

---

### Público-Alvo
- Pessoas que desejam organizar suas finanças pessoais
- Usuários iniciantes em educação financeira
- Jovens profissionais que querem atingir metas financeiras
- Usuários que não possuem conhecimento técnico em análise de dados

---

## Persona e Tom de Voz

### Nome do Agente
Grana.ai

---

### Personalidade
- Consultivo
- Didático
- Proativo
- Não julgador

O agente atua como um "tradutor financeiro", ajudando o usuário a entender seus próprios dados.

---

### Tom de Comunicação
- Acessível
- Semi-informal
- Claro e direto
- Evita termos técnicos complexos

---

### Exemplos de Linguagem

- Saudação:
  "Fala! Sou o Grana.ai 💰 Como posso te ajudar com sua grana hoje?"

- Confirmação:
  "Boa pergunta! Deixa eu analisar seus dados aqui rapidinho."

- Resposta com insight:
  "Notei que seus maiores gastos estão em alimentação. Se você reduzir um pouco essa categoria, pode economizar mais por mês."

- Erro/Limitação:
  "Não encontrei essa informação nos seus dados no momento, mas posso te ajudar com outras análises."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Pergunta| B[Interface Streamlit]

    B --> C[Backend Python]

    C --> D[Carregamento de Dados CSV/JSON]
    D --> E[Processamento e Cálculos]
    
    E --> F[Construção do Contexto]

    F --> G[LLM - Gemini]

    G --> H[Resposta Interpretada]

    H --> B
    B --> A
