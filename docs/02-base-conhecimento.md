# Base de Conhecimento

O Grana.ai utiliza quatro fontes de dados principais para personalizar a experiência do usuário:

## 1. Estrutura de Dados
| Arquivo | Formato | Função |
| :--- | :--- | :--- |
| `transacoes.csv` | CSV | Histórico de compras, categorias e datas. |
| `perfil_investidor.json` | JSON | Nível de tolerância ao risco e objetivos (ex: reserva de emergência). |
| `produtos_financeiros.json`| JSON | Catálogo de opções para recomendação consultiva. |
| `historico_atendimento.csv`| CSV | Contexto de dúvidas anteriores para evitar repetições. |

## 2. Estratégia de Contexto
Para garantir a precisão, os dados são processados via **Pandas** no backend e os resumos estatísticos (ex: soma de gastos por categoria) são enviados ao modelo de linguagem como contexto prioritário.