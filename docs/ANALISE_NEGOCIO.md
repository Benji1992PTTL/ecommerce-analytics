# Análise de negócio — conclusões e próximos passos

## Sumário executivo

O dashboard permite analisar receita de produtos entregues, volume de encomendas, concentração comercial, meios de pagamento, avaliações e entregas. A validação funcional comunicada pelo autor confirmou os KPIs de referência, o comportamento dos filtros e que os dois gráficos Pareto atingem 100% no contexto testado.

**Resultados confirmados no dashboard:** R$ 13.221.498,11 de receita de produtos entregues; 96.478 encomendas entregues elegíveis; ticket médio de R$ 137,04; 99.441 encomendas no total.

Estes números descrevem o dataset histórico e não devem ser apresentados como resultados atuais de uma empresa.

## Questões de negócio que o relatório responde

### 1. A receita está concentrada em poucas categorias?

**Sim, existe concentração relevante:** são necessárias **18 categorias** para atingir pelo menos 80% da receita de produtos entregues. As **18 de 74 categorias** correspondem a **24,3%** do universo considerado, pelo que existe concentração, embora não se verifique literalmente a regra 80/20. A categoria com maior receita é **`health_beauty`**, com **R$ 1.233.131,72**, cerca de **9,33%** da receita total de produtos entregues.

**Implicação:** investigar o desempenho das categorias líderes, distinguindo receita de margem e rentabilidade.

### 2. As encomendas estão concentradas geograficamente?

**Sim:** **6 estados** concentram pelo menos 80% das encomendas entregues. **São Paulo (SP)** lidera com **40.501 encomendas**. Se o universo incluir as 27 unidades federativas brasileiras, os seis estados correspondem a **22,2%** das unidades; esta proporção depende de confirmar o total efetivamente representado.

**Implicação:** analisar procura e qualidade do serviço nas regiões com maior volume, sem confundir estado do cliente com estado do vendedor.

### 3. Como evoluem vendas e ticket médio?

Os indicadores e a série temporal permitem identificar variações ao longo do período coberto. **Não foi apurada nesta documentação uma tendência de crescimento ou sazonalidade**; qualquer conclusão requer comparar períodos equivalentes e assinalar meses incompletos.

### 4. A experiência de entrega está relacionada com a satisfação?

A avaliação média das encomendas **entregues dentro do prazo** é **4,21/5**, face a **2,57/5** nas **entregues após a data estimada**. A diferença é de **1,64 pontos**; a média do grupo atrasado é cerca de **39% inferior** à do grupo pontual, usando a média de 4,21 como referência.

O prazo é a **data estimada de entrega de cada encomenda**, não um limite fixo de dias. A diferença sugere uma associação importante entre pontualidade e satisfação, **sem estabelecer causalidade**. Recomenda-se segmentar por região, categoria e período e verificar os tamanhos das amostras.

### 5. Quais são os meios de pagamento mais utilizados?

As métricas de pagamento permitem avaliar composição por método e prestações. A soma de pagamentos não deve ser interpretada como receita líquida de produtos, porque os pagamentos podem incluir frete e múltiplos registos por encomenda.

## Recomendações analíticas

1. **Concentração:** documentar a percentagem efetiva de categorias e estados que explica 80% do resultado; comparar com o princípio 80/20 sem forçar a conclusão.
2. **Qualidade de serviço:** comparar taxa de atraso e avaliação média por estado e por coorte de compra; investigar apenas diferenças com amostras suficientes.
3. **Evolução temporal:** utilizar meses completos e separar efeitos de volume de encomendas e ticket médio.
4. **Interpretação financeira:** manter receita de produtos, frete e pagamentos como conceitos distintos.

## Resultados globais reportados pelo autor

| Questão | Resultado sem filtros |
|---|---|
| Pareto de categorias | 18 de 74 categorias (24,3%) atingem ≥80% da receita |
| Pareto geográfico | 6 estados atingem ≥80% das encomendas; 27 unidades federativas no Brasil (confirmar cobertura no visual) |
| Maior categoria por receita | `health_beauty` — R$ 1.233.131,72 (~9,33% da receita total) |
| Estado com mais encomendas | SP — 40.501 encomendas |
| Satisfação: dentro do prazo | 4,21/5 |
| Satisfação: atrasadas | 2,57/5 |

**Contexto:** resultados fornecidos pelo autor com filtros limpos. As screenshots incluídas no README apresentam filtros aplicados para demonstração de interatividade e não são evidência dos totais globais.
