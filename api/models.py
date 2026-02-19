from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    descricao = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField()
    horimetro = models.IntegerField()


class Medicao(models.Model):
    tipo = models.CharField(max_length=100)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)


class MedicaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    medicao = models.ForeignKey(Medicao, on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)