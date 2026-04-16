# 📊 Base de Conhecimento — Grana.ai

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Análise de entradas, saídas, saldo, média mensal e padrão de gastos |
| `perfil_investidor.json` | JSON | Definição de perfil financeiro, metas e objetivo principal do usuário |

---

## Adaptações nos Dados

Os dados foram estruturados para permitir análise financeira simples e eficiente.

No arquivo `transacoes.csv`:
- Inclusão de colunas como:
  - `tipo` (entrada/saida)
  - `valor`
  - `categoria`
  - `data`
- Conversão da coluna de data para formato temporal para análise mensal

No arquivo `perfil_investidor.json`:
- Definição de:
  - nome do usuário
  - perfil de investidor
  - objetivo principal (valor da meta)
  - lista de metas financeiras

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados no início da execução do sistema:

- CSV é lido com Pandas
- JSON é carregado como dicionário Python

```python
df = pd.read_csv('data/transacoes.csv')

with open('data/perfil_investidor.json', 'r') as f:
    perfil = json.load(f)