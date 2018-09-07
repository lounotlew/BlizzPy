# WoWAuction - Documentations
> Written by Lewis Kim

### Usage

``WoWAuction`` is a wrapper for realm auction house data in the WoW Community API.

To initialize an instance of ``WoWAuction``:

```python
from blizzpy.wow import WoWAuction

MyAuction = WoWAuction(api_key, realm, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Realms are not case sensitive.

Example:

For auction house data from the realm "Proudmoore" of "en_US",

```python
MyCharacter = WoWAuction(api_key="SOME_API_KEY", realm="proudmoore")
```

Or, for auction house data from the realm "Tarren Mill" of "eu_GB",

```python
MyCharacter = WoWAuction(api_key="SOME_API_KEY", realm="Tarren-Mill", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving realm auction house patch data:_

**1) Raw API auction house data.**

```python
MyAuction.get_auction_data()
```

_*Note: The data returned from_ ``get_auction_data()`` _is very big._

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Timestamp of when the auction data was retrieved.**

```python
MyAuction.get_last_modified()
```

``PARAMS``: None

Returns an ``int`` timestamp of when the data was last retrieved.

**3) Buyout prices of a specific item.**

_*The buyout prices retrieved from the Blizzard API are in copper._

```python
MyAuction.get_buyout_prices(item_id, in_gold=False)
```

``PARAMS``:
- ``item_id``: ``int`` ID of the item to search.
- ``in_gold``: ``boolean``. Return the prices in gold instead of copper if ``True``. 

Returns a dictionary whose keys are item buyout prices (in copper/gold, depending on ``in_gold``), and values the number of those items posted for that buyout price.

e.g. {..., 3000:3, ...} for a buyout price of 3000 copper/gold for 3 counts of the item with ``item_id`` (so, 1000price each).

**4) Auctions posted by a specific player.**

```python
MyAuction.get_auctions_by_player(player_name)
```

``PARAMS``:
- ``player_name``: ``str`` name of the player to search.

Returns a list of dictionaries where each element contains information about each auction posting by ``player_name``.

Keys in returned dictionary:
- ``auc``:
- ``item``:
- ``owner``:
- ``ownerRealm``:
- ``bid``:
- ``buyout``:
- ``quantity``:
- ``timeLeft``:
- ``rand``:
- ``seed``:
- ``context``:

