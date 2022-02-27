# Installation

1. Clone repo
    ```shell
    git clone git@github.com:giocaizzi/surfingcrypto.git
    ```
2. Install requirements.

    ```shell
    pip install -r requirements.txt
    ```

3. Install package with `pip`
   ```shell
   pip install .
   ```
## Configuration

`surfincrypto` submodules require a `surfingcrypto.Config` object to set path directories to appropriate `config_folder` and `data` folders to store private credentials and other generic data.

   * `config_folder` : required
   * `data_folder` - *optional*. If not provided is searched in parent of   `config_folder` or created.

```python
from surfingcrypto import Config
parent="/Users/giorgiocaizzi/Documents/GitHub/surfingcrypto/"

configuration=Config(
    parent+"config",
    parent+"data"
    )
```

To use the package, at least a `config.json` file containing `coins` configuration is required. It can also contain private keys for authentication within other modules.

```json
{
    "coins":
    {
        "BTC":"",
        "ETH":"",
        "MATIC":"",
        "ADA":"",
        "SOL":""
    },
    "telegram":
    {
        "token":"XXXXXXXXXX"
    },
    "coinbase":
    {
        "key":"XXXXXXXXXX",
        "scrt":"XXXXXXXXXX"
    }
    
}
```

### Other (optional) requirements

1. A list of users' info must be supplied to `surfincrypto.telegram_bot` to be used in `channel_mode`. This is specified by adding in the `config_folder` directory a file named `telegram_users.csv` containing - at least - chat IDs (required) and usernames (optional) to keep track of users following the bot. 
```
chat_id,username,date_joined
XXXXXXXX,giocaizzi,2021-11-08 18:10:14+00:00
XXXXXXXX,None,2021-11-08 18:10:14+00:00
```
This file will be updated by the bot in case of interaction with new users.