

#Boa referencia
#https://forum.numer.ai/t/model-diagnostics-risk-metrics/900

def  get_metrics_dicts(values):


    #OK
    dict_Model_Name = {"Metrica": "Model_Name", 
                        "Valor":  values['Model_Name'] ,
                        "Categoria": "Performance", 
                        "Range_Aceitavel": "NA", 
                        "Descricao": "Nome do Modelo" }

    #OK 
    dict_Max_Drawdown = {"Metrica": 'Max_Drawdown', 
                         "Valor": values['Max_Drawdown'], 
                         "Categoria": "Risk", 
                         "Range_Aceitavel": "[0.004%..2%]", 
                         "Descricao": "Perda máxima em uma era" }

    #OK
    dict_Avg_corr = {"Metrica": 'Validation_Mean', 
                     "Valor": values['Validation_Mean'], 
                     "Categoria": "Performance", 
                     "Range_Aceitavel": "[3.6%..4.4%] 4.8%, overfitting", 
                     "Descricao": "Média spearman corr por era" }

    #OK
    dict_Median_corr = {"Metrica": 'Median_corr', 
                        "Valor": values['Median_corr'], 
                        "Categoria": "Estatistica", 
                        "Range_Aceitavel": "[3.6%..4.4%] Dentro do range de médias", 
                        "Descricao": "Mediana spearman corr por era" }

    #OK
    dict_Variance = {"Metrica": 'Variance', 
                     "Valor":  values['Variance'], 
                     "Categoria": "Estatistica", 
                     "Range_Aceitavel": "[0..] Próximo a zero", 
                     "Descricao": "Variancia spearman corr por era" }

    #OK
    dict_Std_Dev = {"Metrica": 'Std_Dev', 
                    "Valor": values['Std_Dev'], 
                    "Categoria": "Risk", 
                    "Range_Aceitavel": "[0..] Próximo a zero", 
                    "Descricao": "Std spearman corr por era" }

    #OK
    dict_AR1 = {"Metrica": 'AR(1)', 
                "Valor": values['AR(1)'], 
                "Categoria": "Estatistica", 
                "Range_Aceitavel": "[0..] Próximo a zero", 
                "Descricao": "AR(1) pearson corr eras[:-1] e eras[1:]" }

    #OK
    dict_Skewness = {"Metrica": 'Skewness', 
                     "Valor":   values['Skewness'], 
                     "Categoria": "Estatistica", 
                     "Range_Aceitavel": "[0..1]", 
                     "Descricao": "Skewness, central moment **3" }

    #OK
    dict_Exc_Kurtosis = {"Metrica": 'Exc_Kurtosis', 
                         "Valor": values['Exc_Kurtosis'], 
                         "Categoria": "Estatistica", 
                         "Range_Aceitavel": "[-1..0]", 
                         "Descricao": "Kurtosis central moment **4" }


    #OK
    dict_Std_Error_Mean = {"Metrica": 'Std_Error_Mean', 
                           "Valor": values['Std_Error_Mean'], 
                           "Categoria": "Estatistica", 
                           "Range_Aceitavel": "[0..] Menor que o std", 
                           "Descricao": "std/sqrt(n) measures how far the sample mean of the data is likely to be from the true population mean." }

    #OK
    dict_Sharpe = {"Metrica": 'Validation_Sharpe', 
                  "Valor": values['Validation_Sharpe'], 
                  "Categoria": "Performance", 
                  "Range_Aceitavel": "Post[>1 good, >1.2 very good][5..25] Iniciantes entre 1 e 2, competidores 14, 24", 
                  "Descricao": "Média da correlacoa por era / std corr por era, anualizado" }




    #OK
    dict_Smart_Sharpe = {"Metrica": "Smart_Sharpe", 
                         "Valor": values['Smart_Sharpe'], 
                         "Categoria": "Financeira", 
                         "Range_Aceitavel": "Pouco menor que o shape", 
                         "Descricao": "Sharpe * auto_corr_penalty" }

    #OK
    dict_Numerai_Sharpe = {"Metrica": "Numerai_Sharpe", 
                          "Valor": values['Numerai_Sharpe'], 
                          "Categoria": "Financeira", 
                          "Range_Aceitavel": "Pouco menor que o sharpe", 
                          "Descricao": "sharpe menos transaction costs" }


    #OK
    dict_Adj_Sharpe = {"Metrica": 'Adj_Sharpe', 
                       "Valor": values['Adj_Sharpe'], 
                       "Categoria": "Financeira", 
                       "Range_Aceitavel": "Prox ao sharpe [5..25]", 
                       "Descricao": "Adjusted Sharpe Ratio adjusts for skewness and kurtosis by incorporating a penalty factor for negative skewness and excess kurtosis" }

    #ok
    dict_VaR_10 = {"Metrica": 'VaR_10', 
                    "Valor": values['VaR_10%'], 
                    "Categoria": "Financeira", 
                    "Range_Aceitavel": "[-0.1..0]", 
                    "Descricao": "Identificar exposicao ao risco || fornece um intervalo de confiança sobre a probabilidade de exceder um certo limite de perda." }




    #OK    
    dict_Sortino_Ratio = {"Metrica": 'Sortino_Ratio', 
                          "Valor": values['Sortino_Ratio'], 
                          "Categoria": "Financeira", 
                          "Range_Aceitavel": "Prox ao sharpe [5..25]", 
                          "Descricao": "Sortino ratio as an alternative to Sharpe for doing hyperparameter selection, \
                                        because it makes sense to me to only penalize downside volatility/variance" }

                         

    #OK
    dict_Smart_Sortino_Ratio = {"Metrica": 'Smart_Sortino_Ratio', 
                                "Valor": values['Smart_Sortino_Ratio'], 
                                "Categoria": "Financeira", 
                                "Range_Aceitavel": "Pouco abaixo do sortino", 
                                "Descricao":  "Sortino Ratio penalizado" }

    #OK
    dict_Payout = {"Metrica": 'Payout', 
                   "Valor": values['Payout'], 
                   "Categoria": "Leaderboard", 
                   "Range_Aceitavel": "[3.6%..4.4%] ", 
                   "Descricao": "Retira as 25% piores e melhores eras corr" }

    #OK
    dict_Feat_exp_std = {"Metrica": 'Feat_exp_std (val)', 
                       "Valor": values['Feat_exp_std'], 
                       "Categoria": "Estatistica", 
                       "Range_Aceitavel": "[8%..x%]", 
                       "Descricao": "Std das features exposures, example_preds 0.0765" }

    #OK
    dict_Feat_exp_max = {"Metrica": 'Feat_exp_max (val)', 
                       "Valor": values['Feat_exp_max'], 
                       "Categoria": "Risk", 
                       "Range_Aceitavel": "[0.10..0.20] com neutralizacao cai pra .15", 
                       "Descricao": "feature com maior exp" }



    
    metrics_dicts_list = [dict_Model_Name
                             ,dict_Max_Drawdown
                             ,dict_Avg_corr
                             ,dict_Median_corr
                             ,dict_Variance
                             ,dict_Std_Dev
                             ,dict_AR1
                             ,dict_Skewness
                             ,dict_Exc_Kurtosis
                             ,dict_Std_Error_Mean
                             ,dict_Sharpe
                             ,dict_Smart_Sharpe
                             ,dict_Numerai_Sharpe
                             ,dict_Adj_Sharpe
                             ,dict_VaR_10
                             ,dict_Sortino_Ratio
                             ,dict_Smart_Sortino_Ratio
                             ,dict_Payout
                             ,dict_Feat_exp_std
                             ,dict_Feat_exp_max
                             ]


    return metrics_dicts_list







