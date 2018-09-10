# D3Profile - Documentations
> Written by Lewis Kim

### Usage

``D3Profile`` is a wrapper for Diablo 3 profile data in the D3 Community API.

To initialize an instance of ``D3Profile``:

```python
from blizzpy.d3 import D3Profile

MyProfile = D3Profile(api_key, battle_tag, locale="en_US", token=None):
```

Supported locales: "en_US", "en_GB", "ko_KR".

``battle_tag`` is the profile's Battle.net tag, with a "-" replacing "#". For instance, the Battle Tag "JoeShmoe#1111" becomes "JoeShmoe-1111".

Example:

```python
MyProfile = D3Profile(api_key="SOME_API_KEY", battle_tag="JoeShmoe-1111")
```

Or,

```python
MyProfile = D3Profile(api_key="SOME_API_KEY", ladder_id="JoeShmoe-1111", locale="en_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

There are currently only methods for fetching raw API data in ``D3Profile``.

#### _Retrieving profile data:_

**1) Raw API profile data.**

```python
MyProfile.get_profile_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving hero data:_

**1) Raw API hero data.**

```python
MyProfile.get_hero_data(hero_id)
```

``PARAMS``:
- ``hero_id``: ``int`` ID of the hero to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving hero items data:_

**1) Raw API hero items data.**

```python
MyProfile.get_hero_items_data(hero_id)
```

``PARAMS``:
- ``hero_id``: ``int`` ID of the hero whose items are to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving follower items data:_

**1) Raw API follower items data.**

```python
MyProfile.get_follower_items_data(hero_id)
```

``PARAMS``:
- ``hero_id``: ``int`` ID of the hero whose followers' items are to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

