# SC2Ladder - Documentations
> Written by Lewis Kim

### Usage

``SC2Ladder`` is a wrapper for PVP ladder data in the SC2 Community API.

To initialize an instance of ``SC2Ladder``:

```python
from blizzpy.sc2 import SC2Ladder

MyLadder = SC2Ladder(api_key, ladder_id, locale="en_US", token=None):
```

Supported locales: "en_US", "en_GB", "ko_KR".

Example:

For a ladder with the ID 123456,

```python
MyLadder = SC2Ladder(api_key="SOME_API_KEY", ladder_id=123456)
```

Or, for a player named "Hoozah" in "en_GB",

```python
MyLadder = SC2Ladder(api_key="SOME_API_KEY", ladder_id=123456, locale="en_GB")
```

To get a ``ladder_id``, search a player's name and look at the URLs to find their ladder ID.

There is currently no native way in the Blizzard API to obtain this information.

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving ladder data:_

**1) Raw API ladder data.**

```python
MyLadder.get_ladder_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Selected ladder's members.**

```python
MyLadder.get_ladder_members(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of dictionaries containing information about the ladder's members. If ``False``, return a list of ``str`` names of the members.

Return a list of ``str`` names of the ladder's members if ``as_names=True``.Else, return a list of dictionaries containing information about the ladder's members.

Keys in returned dictionary:
- ``character``:
- ``joinTimestamp``:
- ``points``:
- ``wins``:
- ``losses``:
- ``highestRank``:
- ``previousRank``:
- ``favoriteRaceP1``:

**3) Search for a specific ladder member.**

```python
MyLadder.search_ladder_member(self, name)
```

``PARAMS``:
- ``name``: ``str`` name of the player to be searched. Case sensitive.

Returns a dictionary that contains information about the searched player. See ``get_ladder_members()`` for dictionary keys.

**4) Average ladder rank.**

```python
MyLadder.get_ladder_avg_rank()
```

``PARAMS``: None

Returns a ``float`` mean of the ranks in the selected ladder.

**5) Ladder members' winrates.**

```python
MyLadder.get_member_winrates()
```

``PARAMS``: None

Returns a dictionary whose keys are the ladder's members' ``str`` names, and values are that player's ``float`` winrate.

**6) Average ladder win rate.**

```python
MyLadder.get_ladder_avg_winrate()
```

``PARAMS``: None

Returns a ``float`` mean of the players' winrates in the selected ladder.

**7) Ladder's favorite races.**

```python
MyLadder.get_ladder_favorite_races()
```

``PARAMS``: None

Returns a dictionary whose keys are the ladder's members' ``str`` names, and values are that player's ``str`` favorite race.

