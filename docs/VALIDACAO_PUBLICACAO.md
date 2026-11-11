# Validação técnica e checklist de publicação

## Testes funcionais comunicados pelo autor

| Teste | Resultado |
|---|---|
| KPIs de referência | Aprovado |
| Seleção de 2017 altera receita e encomendas | Aprovado |
| Seleção de SP em `dim_customers[state]` altera receita e encomendas | Aprovado |
| Seleção de categoria altera `Product Revenue` | Aprovado |
| Limpar slicers repõe os totais | Aprovado |
| Estado do cliente filtra pagamentos e avaliações | Aprovado |
| Pareto por categoria e por estado termina em 100% | Aprovado |

**Alcance:** resultados reportados pelo autor após testes no Power BI Desktop; não equivalem a uma auditoria independente ao ficheiro final modificado localmente.

## Verificações técnicas ainda recomendadas

- [ ] Testar empates exatos nos valores de categorias e estados nos Pareto.
- [ ] Verificar que o Pareto é não decrescente e mantém ordenação por contribuição.
- [ ] Confirmar o denominador de `Late Delivery Rate` e o tratamento de datas em falta.
- [ ] Confirmar ausência de chaves órfãs e duplicações nas dimensões.
- [ ] Confirmar que a execução integral do pipeline funciona numa pasta limpa.
- [ ] Verificar períodos incompletos antes de publicar conclusões YoY/MoM.
- [ ] Confirmar os critérios exatos de avaliações positivas/baixas no DAX final.

## Publicação no GitHub

- [ ] Copiar `README.md` para a raiz e os ficheiros `docs/*.md` para `docs/`.
- [x] Inserir duas screenshots legíveis do relatório e respetivas referências no README.
- [x] Adicionar link para o dataset e identificação da fonte; rever as condições de utilização na página original.
- [ ] Garantir que `data/raw/`, `data/processed/`, `.venv/` e ficheiros temporários não são versionados.
- [ ] Incluir dependências Python com versões testadas (`requirements.txt` ou equivalente).
- [ ] Confirmar que os scripts citados no README estão no repositório.
- [ ] Não publicar caminhos locais absolutos, credenciais ou dados privados.
- [ ] Testar abertura do projeto PBIP e atualização dos CSV numa cópia limpa.
- [x] Preencher os resultados quantitativos fornecidos pelo autor em `ANALISE_NEGOCIO.md` (com limites explicitados).

## Critério de conclusão

O projeto pode ser considerado pronto para portefólio quando a documentação reproduz o comportamento efetivo do modelo publicado, as screenshots correspondem à versão final e o pipeline funciona com os dados de origem colocados nas pastas previstas.

## Contexto dos screenshots

As imagens são exemplos com filtros aplicados e não representam os totais globais. Os resultados de Pareto, categoria líder, estado líder e médias de satisfação foram comunicados pelo autor **sem filtros**.
