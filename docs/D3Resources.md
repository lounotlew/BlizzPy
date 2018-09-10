# D3Resources - Documentations
> Written by Lewis Kim

### Usage

``D3General`` is a wrapper for general Diablo 3 game data in the D3 Community API.

To initialize an instance of ``D3General``:

```python
from blizzpy.d3 import D3General

MyResources = D3General(api_key, locale="en_US", token=None):
```

Supported locales: "en_US", "en_GB", "ko_KR".

Example:

```python
MyResources = D3General(api_key="SOME_API_KEY")
```

Or,

```python
MyResources = D3General(api_key="SOME_API_KEY", locale="en_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

There are currently only methods for fetching raw API data in ``D3Profile``.

#### _Retrieving act data:_

**1) Raw API act index data.**

```python
MyResources.get_act_index_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Raw API act data by Act ID.**

```python
MyResources.get_act_data(act_id)
```

``PARAMS``:
- ``act_id``: ``int`` ID of the act to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving artisan and recipe data:_

**1) Raw API artisan data.**

```python
MyResources.get_artisan_data(artisanSlug)
```

``PARAMS``:
- ``artisanSlug``: ``str`` slug of the artisan to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Raw API recipe data.**

```python
MyResources.get_recipe_data(artisanSlug, recipeSlug)
```

``PARAMS``:
- ``artisanSlug``: ``str`` slug of the artisan to be searched.
- ``recipeSlug``: ``str`` slug of the recipe to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving follower data:_

**1) Raw API follower data.**

```python
MyResources.get_follower_data(followerSlug)
```

``PARAMS``:
- ``followerSlug``: ``str`` slug of the follower to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving character class and skill data:_

**1) Raw API character class data.**

```python
MyResources.get_character_class_data(classSlug)
```

``PARAMS``:
- ``classSlug``: ``str`` slug of the class to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Raw API skill data.**

```python
MyResources.get_skill_data(classSlug, skillSlug)
```

``PARAMS``:
- ``classSlug``: ``str`` slug of the class to be searched.
- ``skillSlug``: ``str`` slug of the skill to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

#### _Retrieving item data:_

**1) Raw API item index data.**

```python
MyResources.get_itemtype_index_data()
```

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Raw API item type data.**

```python
MyResources.get_itemtype_data(itemTypeSlug)
```

``PARAMS``:
- ``itemTypeSlug``: ``str`` slug of the item type to be searched.

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**3) Raw API item data.**

```python
MyResources.get_item_data(itemSlugAndId)
```

``PARAMS``:
- ``itemSlugAndId``: ``str`` slug and ID of the item to be searched. Example: ``"corrupted-ashbringer-Unique_Sword_2H_104_x1"``

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

