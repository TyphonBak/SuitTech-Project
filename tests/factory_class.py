import factory
from app.BLL.models.cliente import Cliente
from app.BLL.models.produto import Produto
from app.BLL.models.venda import Venda
from app.BLL.models.vendedor import Vendedor

class ClienteFactory(factory.Factory):
    class Meta:
        model = Cliente

    nome = factory.Faker('name', locale='pt_BR')
    cpf_cnpj = factory.Faker('numerify', text='###########')
    email = factory.Faker('email', locale='pt_BR')
    logradouro =  factory.Faker('street_name', locale='pt_BR')
    cep = factory.Faker('numerify', text='########')
    numero = factory.Faker('pyint', min_value=1, max_value=9999)
    cidade = factory.Faker('city', locale='pt_BR')
    uf = factory.Faker('state_abbr', locale='pt_BR')
    telefone = factory.Faker('numerify', text='#########')

class ProdutoFactory(factory.Factory):
    class Meta:
        model = Produto

    categoriaID = factory.Faker('pyint', min_value=1)
    nome = factory.Faker('name', locale='pt_BR')
    peso = factory.Faker('numerify', text='##.##')
    altura = factory.Faker('numerify', text='##.##')
    largura = factory.Faker('numerify', text='##.##')
    cor = factory.Faker('color_name', locale='pt_BR')
    material = factory.Faker('word', locale='pt_BR')
    precoCusto = factory.Faker('pyfloat', right_digits=2, min_value=1, max_value=1000)
    precoVendaVarejo = factory.Faker('pyfloat', right_digits=2, min_value=1, max_value=1000)
    precoVendaAtacado = factory.Faker('pyfloat', right_digits=2, min_value=1, max_value=1000)
    imposto = factory.Faker('pyint', min_value=1, max_value=50)
    estoque = factory.Faker('pyint', min_value=1, max_value=10)
    descricao = factory.Faker('sentence')

class VendaFactory(factory.Factory):
    class Meta:
        model = Venda

    idVendedor = factory.Faker('pyint', max_value=5000)
    idCliente = factory.Faker('pyint', max_value=5000)

class VendedorFactory(factory.Factory):
    class Meta:
        model = Vendedor

    nome = factory.Faker('name', locale='pt_BR')
    cpf = factory.Faker('numerify', text='###########')
    email = factory.Faker('email', locale='pt_BR')
