No boxplot, observa-se que startups de sucesso apresentam uma mediana maior de relacionamentos do que as de insucesso, sugerindo que ter uma rede mais ampla está associado a melhores resultados. Ainda assim, há sobreposição entre os grupos, indicando que apenas o número de conexões, isoladamente, não garante sucesso, mas pode ser um fator relevante dentro de um conjunto de variáveis.




!!!!!
No boxplot, fica evidente que startups de sucesso tendem a ter uma mediana mais alta de rodadas do que as de insucesso, o que sugere que conseguir atrair múltiplas rodadas de investimento está associado a uma trajetória mais sustentável e promissora. Apesar disso, há sobreposição entre os grupos, indicando que apenas o número de rodadas, isoladamente, não determina o sucesso, mas é um forte indicativo quando analisado em conjunto com outras variáveis.


# Boxplot comparando sucesso x insucesso (coluna 2)
df.boxplot(column=col, by="labels", grid=False, patch_artist=True)
plt.title(f"{col} vs. Sucesso")
plt.xlabel("Label (0 = insucesso, 1 = sucesso)")
plt.ylabel("Número de rodadas de funding")

# Remove título automático extra
plt.suptitle("")

plt.tight_layout()
plt.show()

O boxplot indica que startups de sucesso apresentam uma mediana mais elevada de milestones do que as de insucesso, sugerindo que conquistar e registrar diversos marcos relevantes está associado a maiores chances de prosperar. No entanto, também há sobreposição entre os grupos, o que indica que apenas o número bruto de milestones não garante o sucesso, mas funciona como um bom indicador complementar dentro do conjunto de variáveis.

# Boxplot comparando sucesso x insucesso (coluna 2)
df.boxplot(column=col, by="labels", grid=False, patch_artist=True)
plt.title(f"{col} vs. Sucesso")
plt.xlabel("Label (0 = insucesso, 1 = sucesso)")
plt.ylabel("Número de milestones")

# Remove título automático extra
plt.suptitle("")

plt.tight_layout()
plt.show()

No boxplot, nota-se que startups de sucesso tendem a ter uma mediana mais elevada de participantes do que as de insucesso, sugerindo que a capacidade de atrair um grupo mais amplo de investidores em cada rodada está associada a melhores resultados. Ainda assim, a sobreposição entre os grupos indica que esse fator, isoladamente, não define o sucesso, mas serve como um sinal de validação do mercado que complementa outras variáveis já analisadas.

# Boxplot comparando sucesso x insucesso (coluna 2)
plt.subplot(1,2,2)
df.boxplot(column=col, by="labels", grid=False, patch_artist=True)
plt.title(f"{col} vs. Sucesso")
plt.xlabel("Label (0 = insucesso, 1 = sucesso)")
plt.ylabel("Média de investidores por rodada")

# Remove título automático extra
plt.suptitle("")

plt.tight_layout()
plt.show()