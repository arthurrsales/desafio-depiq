# Dashboard de Exportações - Produtos com Indicação Geográfica

Projeto desenvolvido para o desafio prático do processo seletivo de estágio na Coordenação-Geral de Propriedade Intelectual (CGPI / DEPIQ / MDIC).

## Visão Geral
Painel web interativo desenvolvido em Python para visualizar e analisar os dados de exportação de 5 produtos brasileiros que possuem registro de Indicação Geográfica (IG) no INPI.

### Produtos e IGs Analisadas:
- Café do Cerrado Mineiro (IG: Cerrado Mineiro)
- Vinhos do Vale dos Vinhedos (IG: Vale dos Vinhedos)
- Cachaça de Paraty (IG: Paraty)
- Manga do Vale do São Francisco (IG: Vale do São Francisco)
- Mel do Oeste de Santa Catarina (IG: Oeste de Santa Catarina)

## Tecnologias Utilizadas
- Python
- Streamlit: Construção do painel e interface web.
- Pandas: Manipulação e estruturação dos dados.
- Plotly Express: Visualização gráfica interativa das exportações por país.

## Como Executar o Projeto Localmente
1. Clone o repositório para o seu computador.
2. Instale as dependências listadas no projeto:

   ```bash
   py -m pip install -r requirements.txt
   ```
3. Execute com o Streamlit:

```bash
py -m streamlit run app.py
```


## Uso de Ferramentas de Inteligência Artificial

A IA foi empregada como suporte técnico para:

Auxílio na estruturação inicial do layout visual do dashboard;

Revisão e otimização da documentação técnica.

Toda a seleção dos dados de Indicação Geográfica (IG), a validação da lógica de filtragem em Python e a execução final da aplicação foram conduzidas de forma independente.