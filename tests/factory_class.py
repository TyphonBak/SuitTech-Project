import factory
from app.BLL.models.cliente import Cliente

class ClienteFactory(factory.Factory):
    class Meta:
        model = Cliente

    nome = factory.Faker('name', locale='pt_BR')
    cpf = factory.Faker('numerify', text='###.###.###-##')
    email = factory.Faker('email', locale='pt_BR')
    logradouro =  factory.Faker('street_name', locale='pt_BR')
    cep = factory.Faker('numerify', text='#####-###')
    numero = factory.Faker('pyint', min_value=1, max_value=9999)
    cidade = factory.Faker('city', locale='pt_BR')
    estado = factory.Faker('state', locale='pt_BR')
