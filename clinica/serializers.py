from rest_framework import serializers
from clinica import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'first_name', 'last_name', 'sexo', 'password', 'user_type', 'cpf', 'rg', 'telefone', 'rua', 'numero', 'bairro', 'cep', 'data_nascimento', 'registro_profissional', 'curriculo']
        extra_kwargs = {'password': {'write_only': True}}  # Garante que a senha não será retornada

    def create(self, validated_data):
        try:
            username = validated_data.get('username', validated_data['email'])
            user = models.User(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                username=username,
                user_type=validated_data['user_type'],
                data_nascimento=validated_data.get('data_nascimento'),
                sexo=validated_data['sexo'],
                cpf=validated_data['cpf'],
                rg=validated_data['rg'],
                telefone=validated_data['telefone'],
                rua=validated_data['rua'],
                numero=validated_data['numero'],
                bairro=validated_data['bairro'],
                cep=validated_data['cep'],
                registro_profissional=validated_data.get('registro_profissional'),
                curriculo=validated_data.get('curriculo'),
            )
            user.set_password(validated_data['password'])  # Encripta a senha corretamente
            user.save()
            return user
        except Exception as e:
            raise serializers.ValidationError(f"Erro ao criar o usuário: {str(e)}")

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servico
        fields = '__all__'


class CasoClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CasoClinico
        fields = '__all__'

class ServicoFisioterapeutaSerializer(serializers.ModelSerializer):
    fisioterapeuta = UserSerializer(read_only=True)  # Usado para retornar os dados completos no output
    fisioterapeuta_id = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.filter(user_type='FIS'), write_only=True, source='fisioterapeuta')  # Usado para o input (aceitar ID)
    servico = ServicoSerializer(read_only=True)  # Usado para retornar os dados completos no output
    servico_id = serializers.PrimaryKeyRelatedField(queryset=models.Servico.objects.all(), write_only=True, source='servico')  # Usado para o input (aceitar ID)

    class Meta:
        model = models.ServicoFisioterapeuta
        fields = '__all__'

class SolicitacaoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SolicitacaoAtendimento
        fields = '__all__'