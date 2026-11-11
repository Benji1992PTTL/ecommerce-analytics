# Dicionário de dados e regras de negócio

## Modelo semântico

| Tabela | Grão | Chave / ligação | Utilização |
|---|---|---|---|
| `dim_calendar` | Uma linha por data | `Date` | Segmentação temporal |
| `dim_customers` | Um registo por `customer_id` | `customer_id` | Geografia e identificação de clientes |
| `dim_products` | Um registo por `product_id` | `product_id` | Categoria e atributos de produto |
| `dim_sellers` | Um registo por `seller_id` | `seller_id` | Geografia do vendedor |
| `mart_order_sales` | Uma linha por encomenda | `order_id` | Receita, encomendas, ticket médio |
| `mart_product_sales` | Uma linha por artigo da encomenda | `order_id` + `order_item_id` | Receita e unidades por categoria/vendedor |
| `mart_payments` | Uma linha por registo de pagamento | `order_id` + `payment_sequential`* | Meios de pagamento e prestações |
| `mart_reviews` | Uma linha por registo de avaliação | `review_id` / `order_id`* | Satisfação e avaliações |
| `mart_deliveries` | Uma linha por encomenda | `order_id` | Prazos e pontualidade |

*Chaves indicadas para interpretação; a unicidade efetiva de pagamentos e avaliações deve ser validada nos dados. `customer_id` identifica o registo de cliente associado à encomenda; `customer_unique_id` permite reconhecer clientes recorrentes.*

## Relações

- `dim_calendar[Date]` → `[purchase_date]` nos cinco factos.
- `dim_customers[customer_id]` → `[customer_id]` nos cinco factos.
- `dim_products[product_id]` → `mart_product_sales[product_id]`.
- `dim_sellers[seller_id]` → `mart_product_sales[seller_id]`.
- Todas 1:* com filtro numa só direção, da dimensão para o facto.

## Indicadores comerciais

| Medida | Definição |
|---|---|
| `Total Revenue` | Soma de `mart_order_sales[product_value]` com `status = delivered` e `item_count > 0` |
| `Product Revenue` | Soma de `mart_product_sales[item_price]` com `status = delivered` |
| `Freight Revenue` | Soma do frete de encomendas entregues elegíveis; separado da receita de produtos |
| `Total Order Value` | `Total Revenue + Freight Revenue` |
| `Delivered Orders` | Contagem distinta de `order_id` com `status = delivered` e `item_count > 0` |
| `All Orders` | Contagem distinta de todas as encomendas |
| `Average Order Value` | `Total Revenue / Delivered Orders`; não inclui frete |
| `Items Sold` | Soma de `item_count` das encomendas entregues elegíveis |
| `Unique Customers` | Contagem distinta de `customer_unique_id` em encomendas entregues elegíveis |
| `Revenue YoY %` | Variação relativa face ao período homólogo |
| `Revenue MoM %` | Variação relativa face ao mês anterior |

**Referência sem filtros:** `Total Revenue` = `Product Revenue` = R$ 13.221.498,11; `Delivered Orders` = 96.478; `All Orders` = 99.441; `Average Order Value` ≈ R$ 137,04. Diferenças entre factos sob filtros de categoria podem ser legítimas.

## Indicadores operacionais

| Indicador | Interpretação / cuidado |
|---|---|
| `Total Payments` | Soma de valores de transações; inclui potencialmente frete e várias linhas por encomenda |
| `Average Installments` | Média de prestações dos registos de pagamento no contexto selecionado |
| `Average Review Score` | Média das pontuações de avaliação disponíveis |
| `Positive Reviews %` / `Low Reviews %` | Percentagens segundo os critérios definidos nas medidas DAX; verificar limiares antes de os citar externamente |
| `Average Delivery Days` | Média de `DATE_DIFF('day', purchased_at, delivered_at)`; dias corridos entre compra e entrega |
| `Late Delivery Rate` | Proporção de entregas assinaladas como atrasadas na medida DAX; verificar denominador de entregas elegíveis |
| `is_late_delivery` | 1 se entrega efetiva posterior à data estimada; 0 se dentro do prazo; `NULL` quando faltam datas |
| `days_vs_estimate` | Diferença em dias entre data estimada e data efetiva de entrega |

**Precisão temporal:** `is_late_delivery` compara timestamps completos, ao passo que `days_vs_estimate` usa diferenças em dias. Por isso, um atraso inferior a um dia pode ser sinalizado como atraso, mas apresentar `0` dias na diferença.

## Pareto 80/20

**Categorias:** barras = `Product Revenue` por `dim_products[category_name_en]`; linha = `Category Cumulative Revenue %`; universo = categorias incluídas no contexto dos filtros.

**Estados:** barras = `Delivered Orders` por `dim_customers[state]`; linha = `State Cumulative Orders %`; universo = estados incluídos no contexto dos filtros.

A regra de 80% é um **limiar de análise**, não uma garantia de que exatamente 20% dos elementos geram 80% do resultado. As medidas acumuladas existentes usam comparação `>=` ao valor corrente; em caso de empates, podem agrupar elementos na mesma posição da curva. A flag 80% pode incluir o elemento que ultrapassa o limiar.

## Cuidados de leitura

1. Todos os factos são segmentados temporalmente por **data de compra**, incluindo entregas e avaliações.
2. O estado de `dim_customers` é do **cliente**; o estado de `dim_sellers` é do **vendedor**.
3. O número de pagamentos não equivale ao número de encomendas.
4. A contagem de avaliações não equivale necessariamente à contagem de encomendas.
5. Evitar comparar períodos incompletos sem contextualização.

## Resultados observados de satisfação

- `Average Score On Time`: **4,21/5** — encomendas entregues até à data estimada.
- `Average Score Late`: **2,57/5** — encomendas entregues após a data estimada.
- Diferença observada: **1,64 pontos**; comparação descritiva, sem inferência causal.
