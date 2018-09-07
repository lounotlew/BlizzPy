# WoWPVP - Documentations
> Written by Lewis Kim

### Usage

``WoWPVP`` is a wrapper for the current-season PVP leaderboard data in the WoW Community API.

If the current season is not active, then ``WoWPVP`` will not return any data.

To initialize an instance of ``WoWPVP``:

```python
from blizzpy.wow import WoWPVP

MyAuction = WoWPVP(api_key, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Example:

For PVP data in "en_US",

```python
MyPVP = WoWPVP(api_key="SOME_API_KEY")
```

Or, for PVP data in eu_GB",

```python
MyPVP = WoWPVP(api_key="SOME_API_KEY", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving 2v2 arena data:_

**1) Raw API 2v2 arena data.**

```python
MyPVP.get_2v2_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint '2v2'.

See https://dev.battle.net/io-docs for details.

**2) Search for a 2v2 arena player.**

```python
MyPVP.search_2v2_player(player_name)
```

``PARAMS``:
- ``player_name``: ``str`` name of the player to search. Case sensitive.

Returns a dictionary that contains 2v2 arena information about the searched player.

Key in returned dictionary:
- ``ranking``:
- ``rating``:
- ``name``:
- ``realmId``:
- ``realmName``:
- ``realmSlug``:
- ``raceId``:
- ``classId``:
- ``specId``:
- ``factionId``:
- ``genderId``:
- ``seasonWins``:
- ``seasonLosses``:
- ``weeklyWins``:
- ``weeklyLosses``:
- ``tier``:

**3) Search 2v2 arena players by rank.**

```python
MyPVP.search_2v2_players_by_rank(rank, as_names=False)
```

``PARAMS``:
- ``rank``: ``int`` rank to search players by.
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank`` (see ``search_2v2_player(player_name)`` for keys).

Returns a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank``.

#### _Retrieving 3v3 arena data:_

**1) Raw API 3v3 arena data.**

```python
MyPVP.get_3v3_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint '3v3'.

See https://dev.battle.net/io-docs for details.

**2) Search for a 3v3 arena player.**

```python
MyPVP.search_3v3_player(player_name)
```

``PARAMS``:
- ``player_name``: ``str`` name of the player to search. Case sensitive.

Returns a dictionary that contains 3v3 arena information about the searched player.

Key in returned dictionary: see ``search_2v2_player(player_name)``.

**3) Search 3v3 arena players by rank.**

```python
MyPVP.search_3v3_players_by_rank(rank, as_names=False)
```

``PARAMS``:
- ``rank``: ``int`` rank to search players by.
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank`` (see ``search_3v3_player(player_name)`` for keys).

Returns a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank``.

#### _Retrieving RBG data:_

**1) Raw API RBG arena data.**

```python
MyPVP.get_rbg_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'RBG'.

See https://dev.battle.net/io-docs for details.

**2) Search for a RBG arena player.**

```python
MyPVP.search_rbg_player(player_name)
```

``PARAMS``:
- ``player_name``: ``str`` name of the player to search. Case sensitive.

Returns a dictionary that contains RBG information about the searched player.

Key in returned dictionary: see ``search_2v2_player(player_name)``.

**3) Search RBG arena players by rank.**

```python
MyPVP.search_rbg_players_by_rank(rank, as_names=False)
```

``PARAMS``:
- ``rank``: ``int`` rank to search players by.
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank`` (see ``search_rbg_player(player_name)`` for keys).

Returns a list of ``str`` of the names of the players whose rank is ``rank``. Otherwise, return a list of dictionaries of information of each player whose rank is ``rank``.

