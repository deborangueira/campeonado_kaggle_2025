# campeonado_kaggle_2025
Desenvolvimento de um modelo de machine learning para **prever se uma startup terá sucesso (ativa/adquirida) ou não (fechada).**

O conjunto de dados foi adaptado para fins educacionais e busca promover aprendizado prático em empreendedorismo e modelagem preditiva.

### Base de dados

- Moderadamente desbalanceada

- Inclui informações sobre: 📈 Histórico de rodada de investimento; 🌍 Localização; 🏭 Setor de atuação; 🔗 Conexões estratégicas; 🏆 Marcos alcançados.

- train.csv → conjunto de treinamento com startups + variável alvo (labels)

- test.csv → conjunto de teste (sem a coluna alvo)

- Observações gerais:
    - category_code é uma variável categórica bruta.
    - As demais dummies são binárias 0/1.

**Target**
- Indicador de sucesso

    1 (sucesso) → 597 startups (~64,7%)\
    0 (insucesso) → 326 startups (~35,3%)

**Idades relativas**

- anos desde a fundação até o evento
- contínuo
- 2 casas decimais
- NaN: evento não ocorreu/ está indisponível
- **Legenda**
    1. **age_first_funding_year**: Anos até o primeiro funding
    2. **age_last_funding_year**: Anos até o último funding
    3. **age_first_milestone_year**: Anos até o primeiro milestone
    4. **age_last_milestone_year**: Anos até o último milestone

**Estrutura, histórico e escala de captação**

- **Legenda**
    - **relationships**: Contagem de relações (fundadores, executivos, investidores)
    - **funding_rounds**: Número de rodadas de captação
    - **funding_total_usd**: Total captado (USD) - float64
    - **milestones**: Contagem de marcos relevantes 
    - **avg_participants**: Média de investidores por rodada - float64

**Localização**

- Representam o estado onde a startup está sediada
-  {0,1}.

**Legenda**
- **is_CA**: Califórnia
- **is_NY**: Nova Iorque
- **is_MA**: Massachusetts
- **is_TX**: Texas
- **is_otherstate**

**Setor/mercado (categórica + dummies)**

- category_code: Setor principal declarado -> Requer encoding (One-Hot/Target).
- Indicadores de setor {0,1}
    - is_software
    - is_web,
    - is_mobile
    - is_enterprise
    - is_advertising
    - is_gamesvideo
    - is_ecommerce
    - is_biotech
    - is_consulting
    - is_othercategory

**Sinalizadores de financiamento (rodadas e tipos)**

- **has_VC**: Recebeu venture capital? | {0,1}.
- **has_angel**: Recebeu investimento angel? | {0,1}.
- **has_roundA**: Teve a respectiva rodada? | {0,1}.
- **has_roundB**: Teve a respectiva rodada? | {0,1}.
- **has_roundC**: Teve a respectiva rodada? | {0,1}.
- **has_roundD**: Teve a respectiva rodada? | {0,1}.

**Observações e políticas de dados**

- Faltantes (NaN): principalmente em age_* e outliers de funding_total_usd → tratar no pipeline (ex.: imputação por mediana ou uso de modelos robustos).

- Escalas: variáveis como funding_total_usd, relationships, funding_rounds e avg_participants têm ordens de grandeza diferentes → recomenda-se normalização/padronização (`StandardScaler`) em modelos lineares.

- Balanceamento: verifique a proporção de labels ao treinar; se necessário, use class_weight, threshold tuning ou métricas robustas (AUC/F1).