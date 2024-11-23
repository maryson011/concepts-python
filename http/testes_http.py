from typing import Literal, TypeAlias, get_args
import httpx # type: ignore
import respx # type: ignore


URL_COTACAO = 'https://economia.awesomeapi.com.br/json/last/{}'
Moeda: TypeAlias = Literal['EUR', 'USD']

def contacao(moeda: Moeda):
    code = f'{moeda}-BRL'
    try:
        response = httpx.get(URL_COTACAO.format(code))
        data = response.json()[code.replace('-', '')]
        return f'Última cotação {data['high']}'
    except KeyError:
        return f'Código de moeda invalido. Use {get_args(Moeda)}'
    except httpx.InvalidURL:
        return f'Código de moeda inválido. Use {get_args(Moeda)}'
    except httpx.ConnectError:
        return 'Erro de conexão, tente mais tarde.'
    except httpx.TimeoutException:
        return 'Erro de conexão, tente mais tarde.'

@respx.mock
def test_dolar():
    # Arange
    mocked_response = httpx.Response(
        200, json={'USDBRL': {'high': 6.105}}
    )
    respx.get(
        URL_COTACAO.format('USD-BRL')
    ).mock(mocked_response)

    # Act
    result = contacao('USD')
    # Assert
    assert result == 'Última cotação 6.105'


@respx.mock
def test_moeda_errada():
    mocked_response = httpx.Response(200, json={})

    respx.get(
        URL_COTACAO.format('MDT-BRL')
    ).mock(mocked_response)

    result = contacao('MDT')

    assert (
        result == "Código de moeda invalido. Use ('EUR', 'USD')"
    )

def test_erro_timeout(respx_mock):
    respx_mock.get(
        URL_COTACAO.format('USD-BRL')
    ).mock(side_effect=httpx.TimeoutException)

    result = contacao('USD')

    assert result == 'Erro de conexão, tente mais tarde.'