# Documentação do Agente: Grana.ai

## 1. Visão Geral
O **Grana.ai** é um "tradutor financeiro" projetado para converter dados bancários brutos e complexos em linguagem acessível, insights comportamentais e sugestões práticas.

## 2. Caso de Uso
O agente resolve a dificuldade de compreensão de extratos e a falta de organização financeira para usuários leigos. 
- **Problema:** Usuários que se sentem sobrecarregados por números e não sabem para onde o dinheiro está indo.
- **Solução:** Análise proativa de transações e consultoria educativa.

## 3. Persona e Tom de Voz
- **Nome:** Grana.ai
- **Perfil:** Assistente consultivo, educador e analista.
- **Tom de Voz:** Simples, direto, humano e livre de julgamentos.
- **Estilo:** Evita jargões técnicos (como "liquidez" ou "proventos") a menos que explicados de forma simples.

## 4. Arquitetura do Sistema
1. **Camada de Dados:** Ingestão de arquivos CSV (transações e atendimentos) e JSON (perfil e produtos).
2. **Processamento (LLM):** Utilização de RAG (Retrieval-Augmented Generation) para injetar o contexto financeiro do usuário no prompt.
3. **Filtro de Segurança:** Verificação de integridade para garantir que valores citados existam na base de dados (evitando alucinações).

## 5. Segurança e Confiabilidade
- **Anti-Alucinação:** O agente é instruído a responder "Não encontrei essa informação" caso o dado não esteja nas planilhas.
- **Privacidade:** Filtros de PII (Informações Pessoais Identificáveis) para garantir que dados sensíveis não sejam expostos fora do contexto necessário.