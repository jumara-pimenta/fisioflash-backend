from rest_framework import serializers
from clinica import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'first_name', 'last_name', 'sexo', 'password', 'user_type', 'cpf', 'rg', 'telefone', 'rua', 'numero', 'bairro', 'cep', 'data_nascimento', 'registro_profissional', 'curriculo', 'minibio']
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
                minibio=validated_data.get('minibio'),
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
    servico_fisioterapeuta_id = serializers.PrimaryKeyRelatedField(queryset=models.ServicoFisioterapeuta.objects.all(), write_only=True, source='servico_fisioterapeuta')
    servico_fisioterapeuta = serializers.SerializerMethodField()

    class Meta:
        model = models.CasoClinico
        fields = ['id', 'descricao', 'paciente', 'servico_fisioterapeuta', 'servico_fisioterapeuta_id', 'situacao']

    def get_servico_fisioterapeuta(self, obj):
        # Retorna uma descrição mais detalhada do serviço e fisioterapeuta
        return {
            "fisioterapeuta": {
                "id": obj.servico_fisioterapeuta.fisioterapeuta.id,
                "nome": f"{obj.servico_fisioterapeuta.fisioterapeuta.first_name} {obj.servico_fisioterapeuta.fisioterapeuta.last_name}",
                "email": obj.servico_fisioterapeuta.fisioterapeuta.email,
            },
            "servico": {
                "id": obj.servico_fisioterapeuta.servico.id,
                "especialidade": obj.servico_fisioterapeuta.servico.especialidade,
            }
        }


class ServicoFisioterapeutaSerializer(serializers.ModelSerializer):
    fisioterapeuta = UserSerializer(read_only=True) 
    fisioterapeuta_id = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.filter(user_type='FIS'), write_only=True, source='fisioterapeuta')  
    servico = ServicoSerializer(read_only=True) 
    servico_id = serializers.PrimaryKeyRelatedField(queryset=models.Servico.objects.all(), write_only=True, source='servico')  

    class Meta:
        model = models.ServicoFisioterapeuta
        fields = '__all__'

class SolicitacaoAtendimentoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.ReadOnlyField(source='paciente.get_full_name') 
    fisioterapeuta_nome = serializers.ReadOnlyField(source='fisioterapeuta.get_full_name')
    descricao_caso_clinico = serializers.ReadOnlyField(source='caso_clinico.descricao')
    especialidade_servico = serializers.ReadOnlyField(source='servico.especialidade')

    class Meta:
        model = models.SolicitacaoAtendimento
        fields = ['id', 'paciente', 'paciente_nome', 'fisioterapeuta', 'fisioterapeuta_nome', 'servico', 'especialidade_servico', 'status', 'data_solicitacao', 'caso_clinico', 'descricao_caso_clinico']