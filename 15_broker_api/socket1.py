


from alpaca.data.live.crypto import CryptoDataStream
api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key='rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1'
crypto_data_stream_client=CryptoDataStream(api_key,secret_key)
async def crypto_data_stream_handler(data):
    print(data)
symbol=['BTC/USD','ETH/USD']
crypto_data_stream_client.subscribe_trades(crypto_data_stream_handler, *symbol)
# crypto_data_stream_client.subscribe_quotes(crypto_data_stream_handler, *symbol)
crypto_data_stream_client.run()