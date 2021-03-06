token_symbols = {
    "DAI": {"address": 0x6B175474E89094C44DA98B954EEDEAC495271D0F, "decimals": 18},
    "USDC": {"address": 0xA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48, "decimals": 6},
    "MKR": {"address": 0x9F8F72AA9304C8B593D555F12EF6589CC3A579A2, "decimals": 18},
    "LINK": {"address": 0x514910771AF9CA656AF840DFF83E8264ECF986CA, "decimals": 18},
    "BAT": {"address": 0x0D8775F648430679A709E98D2B0CB6250D2887EF, "decimals": 18},
    "WBTC": {"address": 0x2260FAC5E5542A773AA44FBCFEDF7C193BC2C599, "decimals": 8},
    "USDT": {"address": 0xDAC17F958D2EE523A2206206994597C13D831EC7, "decimals": 6},
    "APE": {"address": 0x4d224452801ACEd8B2F0aebE155379bb5D594381, "decimals": 18},
    "QNT": {"address": 0x4a220E6096B25EADb88358cb44068A3248254675, "decimals": 18},
    "TUSD": {"decimals": 18},
    "DERC": {"address": 0x9fa69536d1cda4A04cFB50688294de75B505a9aE, "decimals": 18},
    "UFO": {"address": 0x249e38Ea4102D0cf8264d3701f1a0E39C4f2DC3B, "decimals": 18},
    "BNT": {"address": 0x1F573D6FB3F13D689FF844B4CE37794D79A7FF1C, "decimals": 18},
    "PAX": {"address": 0x8E870D67F660D95D5BE530380D0EC0BD388289E1, "decimals": 18},
    "LUNA": {"address": 0xd2877702675e6cEb975b4A1dFf9fb7BAF4C91ea9, "decimals": 18},
    "KNC": {"address": 0xDD974D5C2E2928DEA5F71B9825B8B646686BD200, "decimals": 18},
    "ETH": {
        'address': 0xdd974d5c2e2928dea5f71b9825b8b646686bd200,
        "decimals": 18
    },
}

orfeed_list_providers = ["UNISWAPBYSYMBOLV1",
                         "UNISWAPBYSYMBOLV2", "KYBERBYSYMBOLV1"]


def init_dict_token_dex():
    token_dex = {}
    for token in token_symbols:
        token_dex[token] = {}
        for provider in orfeed_list_providers:
            token_dex[token][provider] = 0
    return token_dex
