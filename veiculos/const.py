
COLORS = (
    (1,'Preto'),
    (2,'Branco'),
    (3,'Vermelho'),
    (4,'Prata'),
)

##PODERIA COLOCAR AS ESCOLHAS DENTRO DO CÓDIGO (models.py) SE QUISESSE
##EM CIMA DO 'COR' PODENDO TER ESCOLHAR NUMERAL COMO FOI FEITA OU ESCOLHA DE TEXTO

##EXEMPLO:
#DENTRO DA CLASS VEICULO
    #CorDoCarro = models.TextChoices('CorDoCarro', 'PRETO BRANCO ETC.'),
    #cor = models.CharField(choices=CorDoCarro.choises, null=False, blank=False, default=1)
