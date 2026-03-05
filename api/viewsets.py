from rest_framework import viewsets
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de marca",
        responses={200: MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de marca",
        responses={200: MarcaSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de marca conforme ID",
        responses={200: MarcaSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de marca conforme dados passados, para o ID informado",
        responses={200: MarcaSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de marca conforme ID informado",
        responses={200: MarcaSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de modelo",
        responses={200: ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de modelo",
        responses={200: ModeloSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de modelo conforme ID",
        responses={200: ModeloSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de modelo conforme dados passados, para o ID informado",
        responses={200: ModeloSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de modelo conforme ID informado",
        responses={200: ModeloSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de veiculo",
        responses={200: VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de veiculo",
        responses={200: VeiculoSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de veiculo conforme ID",
        responses={200: VeiculoSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de veiculo conforme dados passados, para o ID informado",
        responses={200: VeiculoSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de Veiculo conforme ID informado",
        responses={200: VeiculoSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.all()
    serializer_class = UnidadeMedidaSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de unidade de medida",
        responses={200: UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de unidade de medida",
        responses={200: UnidadeMedidaSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de unidade de medida conforme ID",
        responses={200: UnidadeMedidaSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de unidade de medida conforme dados passados, para o ID informado",
        responses={200: UnidadeMedidaSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de unidade de medida conforme ID informado",
        responses={200: UnidadeMedidaSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = Medicao.objects.all()
    serializer_class = MedicaoSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de medição",
        responses={200: MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de medição",
        responses={200: MedicaoSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de medição conforme ID",
        responses={200: MedicaoSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de medição conforme dados passados, para o ID informado",
        responses={200: MedicaoSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de medição conforme ID informado",
        responses={200: MedicaoSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = MedicaoVeiculo.objects.all()
    serializer_class = MedicaoVeiculoSerializer

    @swagger_auto_schema(
        operation_description="retorna informacoes de medição veiculo",
        responses={200: MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de medição veiculo",
        responses={200: MedicaoVeiculoSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="cria um registro de tipo de medição veiculo conforme ID",
        responses={200: MedicaoVeiculoSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="altero o tipo de medição veiculo conforme dados passados, para o ID informado",
        responses={200: MedicaoVeiculoSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="apaga o registro de tipo de medição veiculo conforme ID informado",
        responses={200: MedicaoVeiculoSerializer()}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)