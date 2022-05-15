# Configuration

`surfincrypto` submodules require a `surfingcrypto.Config` object to set coins configuration and to set path directories to appropriate `config_folder` and `data` folders to store private credentials and other data, as time series OHLC data.

   * `config_folder` : required
   * `data_folder` - *optional*. If not provided is created in parent of `config_folder` or created.

```python
from surfingcrypto import Config
parent="/Users/giorgiocaizzi/Documents/GitHub/surfingcrypto/"
coins={
        "BTC":"",
        "ETH":"",
        "MATIC":"",
        "ADA":"",
        "SOL":""
    },
configuration=Config(
    parent+"config",
    )
```

The `config.json` contains private keys for authentication within other modules, such as `surfingcrypto.Portfolio`.

```json
{
    "coinbase":
    {
        "key":"XXXXXXXXXX",
        "scrt":"XXXXXXXXXX"
    },
    "telegram":
    {
        "token":"XXXXXXXXXX"
    }, 
}
```

Additionally, it is possible to store other kind of private information, as third-party API keys, so to easily have them stored as attributes in the `Config` module.