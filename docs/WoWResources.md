# WoWResources - Documentations
> Written by Lewis Kim

### Usage

``WoWResources`` is a wrapper for the general game data in the WoW Community API, such as achievements, spells, and zones.

To initialize an instance of ``WoWResources``:

```python
from blizzpy.wow import WoWResources

MyAuction = WoWResources(api_key, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Example:

For PVP data in "en_US",

```python
MyResources = WoWResources(api_key="SOME_API_KEY")
```

Or, for PVP data in eu_GB",

```python
MyResources = WoWResources(api_key="SOME_API_KEY", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving game achievements data:_

**1) Raw API game achievement data.**

```python
MyResources.get_achievement_data(achievement_id)
```

``PARAMS``:
- ``achievement_id``: ``int`` id of the achievement to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'achievement'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game boss data:_

**1) Raw API game boss data.**

```python
MyResources.get_boss_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'boss'.

See https://dev.battle.net/io-docs for details.

**2) Search for a specific boss's information.**

```python
MyResources.get_boss_info(boss_id)
```

``PARAMS``:
- ``boss_id``: ``int`` id associated with the boss to be searched.

Returns a dictionary containing information about the selected boss.

Keys in returned dictionary:
- ``id``:
- ``name``:
- ``urlSlug``:
- ``description``:
- ``zoneId``:
- ``availableInNormalMode``:
- ``availableInHeroicMode``:
- ``health``:
- ``heroicHealth``:
- ``level``:
- ``heroicLevel``:
- ``journalId``:
- ``npcs``:

#### _Retrieving game items data:_

**1) Raw API game item data.**

```python
MyResources.get_item_data(item_id)
```

``PARAMS``:
- ``item_id``: ``int`` id associated with the item to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'item'.

See https://dev.battle.net/io-docs for details.

**2) Raw API game item set data.**

```python
MyResources.get_item_set_data(itemSet_id)
```

``PARAMS``:
- ``itemSet_id``: ``int`` id associated with the item set to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'item-set'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game mounts data (master list):_

**1) Raw API game mounts data.**

```python
MyResources.get_mounts_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'mount'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game quest data:_

**1) Raw API quest data.**

```python
MyResources.get_quest_data(quest_id)
```

``PARAMS``:
- ``quest_id``: ``int`` id associated with the quest to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'quest'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game realms data:_

**1) Raw API game realms data.**

```python
MyResources.get_realms_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'realms'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game recipe data:_

**1) Raw API game recipe data.**

```python
MyResources.get_recipe_data(recipe_id)
```

``PARAMS``:
- ``recipe_id``: ``int`` id associated with the recipe to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'recipe'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game spell data:_

**1) Raw API game spell data.**

```python
MyResources.get_spell_data(spell_id)
```

``PARAMS``:
- ``spell_id``: ``int`` id associated with the spell to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'spell'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving game zone data:_

**1) Raw API game zones data.**

```python
MyResources.get_zones_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'zone'.

See https://dev.battle.net/io-docs for details.

**2) Search for a specific zone.**

```python
MyResources.get_zone_info(zone_id)
```

``PARAMS``:
- ``zone_id``: ``int`` id associated with the zone to be searched.

Returns a dictionary containing information about the selected zone.

Keys in returned dictionary:
- ``id``:
- ``name``:
- ``urlSlug``:
- ``description``:
- ``location``:
- ``expansionId``:
- ``numPlayers``:
- ``isDungeon``:
- ``isRaid``:
- ``advisedMinLevel``:
- ``advisedMaxLevel``:
- ``advisedHeroicMinLevel``:
- ``advisedHeroicMaxLevel``:
- ``availableModes``:
- ``lfgNormalMinGearLevel``:
- ``lfgHeroicMinGearLevel``:
- ``floors``:
- ``bosses``:

