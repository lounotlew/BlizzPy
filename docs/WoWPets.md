# WoWPets - Documentations
> Written by Lewis Kim

### Usage

``WoWPets`` is a wrapper for the non-hunter pets data in the WoW Community API. It is not character specific.

To initialize an instance of ``WoWPets``:

```python
from blizzpy.wow import WoWPets

MyPets = WoWPets(api_key, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Example:

For pets data in "en_US",

```python
MyPets = WoWPets(api_key="SOME_API_KEY")
```

Or, for pets data in eu_GB",

```python
MyPets = WoWPets(api_key="SOME_API_KEY", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving general pets data:_

**1) Raw API pets data.**

```python
MyPets.get_master_list()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Searching for a pet by its name or ID.**

```python
MyPets.search_pet(pet_param)
```

``PARAMS``:
- ``pet_param``: ``str`` name of the pet to be searched, or ``int`` ID of the pet. 

Returns a dictionary containing information about the searched pet.

Keys in returned dictionary:
- ``canBattle``:
- ``creatureId``:
- ``name``:
- ``family``:
- ``icon``:
- ``qualityId``:
- ``stats``:
- ``strongAgainst``:
- ``typeId``:
- ``weakAgainst``:

**3) Pet name to pet ID dictionary.**

```python
MyPets.get_nameToID_dict()
```

``PARAMS``: None

Returns a dictionary whose keys are ``str`` names of all pets, and values are the corresponding ``int`` IDs of that pet.

**4) Getting all battle pets.**

```python
MyPets.get_battle_pets(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` names of the battle pets. If ``False``, return a list of dictionaries containing information about each pet.

Returns a list of dictionaries containing information about each pet (see ``search_pet(pet_param)`` for keys) if ``as_names=False``. Returns a list of ``str`` names of each battle pet if ``as_names=True``.

**5) Searching for a pet's stats.**

```python
MyPets.get_pet_stats(pet_param)
```

``PARAMS``:
- ``pet_param``: ``str`` name of the pet to be searched, or ``int`` ID of the pet. 

Returns a dictionary containing stats information about the searched pet.

Keys in returned dictionary:
- ``speciesId``:
- ``breedId``:
- ``petQualityId``:
- ``level``:
- ``health``:
- ``power``:
- ``speed``:

#### _Retrieving pet ability data:_

**1) Raw API pet abilities data.**

```python
MyPets.get_ability_data(abilityId)
```

``PARAMS``:
- ``abilityId``: ``int`` ID of the pet ability to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving pet species data:_

**1) Raw API pet species data.**

```python
MyPets.get_species_data(speciesId)
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving pet species stats data:_

**1) Raw API pet species stats data.**

```python
MyPets.get_species_stats_data(speciesId, level=1, breedId=3, qualityId=1)
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.
