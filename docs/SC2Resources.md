# SC2Resources - Documentations
> Written by Lewis Kim

### Usage

``SC2Resources`` is a wrapper for the achievements and rewards data in the SC2 Community API.

To initialize an instance of ``SC2Resources``:

```python
from blizzpy.sc2 import SC2Resources

MyResources = SC2Resources(api_key, locale="en_US", token=None):
```

Supported locales: "en_US", "en_GB", "ko_KR".

Example:

```python
MyResources = SC2Resources(api_key="SOME_API_KEY")
```

Or,

```python
MyResources = SC2Resources(api_key="SOME_API_KEY", locale="en_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving achievements data:_

**1) Raw API achievements data.**

```python
MyResources.get_achievements_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) All available achievement names.**

```python
MyResources.get_achievement_names()
```

``PARAMS``: None

Returns a list of ``str`` names of all available achievements in SC2.

**2) Achievment name to ID dictionary.

```python
MyResources.get_achievement_nameToID_dict()
```

``PARAMS``: None

Returns a dictionary whose keys are the ``str`` names of the achievments, and values are the ``int`` ID of that achievement.

#### _Retrieving rewards data:_

**1) Raw API rewards data.**

```python
MyResources.get_rewards_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Searching a reward by its ID. **

```python
MyResources.get_reward_by_id(reward_id)
```

``PARAMS``:
- ``reward_id``: ``int`` ID of the reward to be searched.

Returns a dictionary that contains information about the reward whose ID is ``reward_id``.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

**3) Searching a reward by its name.**

```python
MyResources.get_reward_by_name(reward_name)
```

``PARAMS``:
- ``reward_name``: ``str`` name of the reward to be searched.

Returns a dictionary that contains information about the reward whose name is ``reward_name``.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

**4) All portrait rewards in the game.**

```python
MyResources.get_portraits(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` that contains the names of the portraits. If ``False``, return a list of dictionaries that contains information about each portrait.

return a list of ``str`` that contains the names of the portraits if ``as_names=True``. Else, return a list of dictionaries that contains information about each portrait.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

**5) Race decals.**

```python
MyResources.get_RACEDecals(as_names=False)
```

Replace 'RACE' with 'zerg', 'terran', or 'protoss'.

Example:

```python
MyResources.get_zergDecals(as_names=True)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` names of the decal rewards associated with that race. If ``False``, return a list of dictionaries containing information about the decals.

Returns a list of ``str`` names of the decal rewards associated with RACE if ``as_names=True``. Otherwise, returns a list of dictionaries containing information about the decals.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

**6) Skin rewards.**

```python
MyResources.get_skins(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` names of the skin rewards. If ``False``, return a list of dictionaries containing information about the skins.

Returns a list of ``str`` names of the skin rewards if ``as_names=True``. Otherwise, returns a list of dictionaries containing information about the skins.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

**7) Animation rewards.**

```python
MyResources.get_animations(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return a list of ``str`` names of the animation rewards. If ``False``, return a list of dictionaries containing information about the animation.

Returns a list of ``str`` names of the animation rewards if ``as_names=True``. Otherwise, returns a list of dictionaries containing information about the animation.

Keys in returned dictionary:
- ``title``:
- ``id``:
- ``icon``:
- ``achievementId``:

