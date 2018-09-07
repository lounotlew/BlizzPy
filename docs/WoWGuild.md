# WoWGuild - Documentations
> Written by Lewis Kim

### Usage

``WoWGuild`` is a wrapper for guild data in the WoW Community API.

To initialize an instance of ``WoWGuild``:

```python
from blizzpy.wow import WoWGuild

MyGuild = WoWGuild(api_key, guild_name, realm, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Realms are not case sensitive.

Example:

For a guild named "Eternal Kingdom" in the realm "Proudmoore" of "en_US",

```python
MyCharacter = WoWGuild(api_key="SOME_API_KEY", guild_name="Eternal Kingdom", realm="proudmoore")
```

Or, for a guild named "Method" in the realm "Tarren Mill" of "eu_GB",

```python
MyCharacter = WoWGuild(api_key="SOME_API_KEY", guild_name="Method", realm="Tarren-Mill", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving basic guild data:_

**1) Raw API guild data.**

```python
MyGuild.get_guild_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.


**2) Selected guild's emblem.**

```python
MyGuild.get_guild_emblem()
```

``PARAMS``: None

Returns a dictionary containing information about the guild's emblem.

Keys in returned dictionary:
- ``icon``: ``int``.
- ``iconColor``: ``str``. Example: 'ffdfa55a'.
- ``iconColorId``: ``int``.
- ``border``: ``int``.
- ``borderColor``: ``str``. Example: 'fff9cc30'.
- ``borderColorId``: ``int``.
- `` backgroundColor``: ``str``. Example: 'ff9e0036'.
- ``backgroundColorId``: ``int``.

#### _Retrieving guild members data:_

**1) Raw API guild members data.**

```python
MyGuild.get_guild_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with enpoint 'members'.

See https://dev.battle.net/io-docs for details.

**2) Search for a guild member.**

```python
MyGuild.get_member_info(member_name)
```

``PARAMS``:
- ``member_name``: ``str`` of the member to be searched.

Returns a dictionary containing information about the searched guild member.

Keys in returned dictionary:
- ``character``: a dictionary containing character data of the searched member. Keys: ``name``, ``realm``, ``battlegroup``, ``class``, ``race``, ``gender``, ``level``, ``achievementPoints``, ``thumbnail``, ``spec``, ``guild``, ``guildRealm``, ``lastModified``.
- ``rank``: ``int`` of the guild rank.

**3) Search for the rank of a guild member.**

```python
MyGuild.get_member_rank(member_name)
```

``PARAMS``:
- ``member_name``: ``str`` of the member to be searched.

Returns an ``int`` of the searched guild member's rank.

**4) Number of members in the guild.**

```python
MyGuild.get_num_members()
```

``PARAMS``: None

Returns an ``int`` of the number of members in the selected guild.

**5) Selected guild's members' names.**

```python
MyGuild.get_members_names()
```

``PARAMS``: None

Returns a list of ``str`` of the guild's members' names.

**6) Search for guild members by a class spec.**

```python
get_members_by_spec(spec, as_names=False)
```

``PARAMS``:
- ``spec``: ``str`` name the class spec.
- ``as_names``: ``boolean``. If ``True``, return the guild members that match the spec as a list of ``str`` of their names. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

Return a list of ``str`` of the guild members' names that match ``spec`` if ``as_names=True``. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

**7) Search for guild members by role (Tank, Healer, DPS).**

```python
get_members_by_spec(role, as_names=False)
```

``PARAMS``:
- ``role``: ``str`` name of the role: 'Tank', 'Healer', 'DPS'.
- ``as_names``: ``boolean``. If ``True``, return the guild members that match the role as a list of ``str`` of their names. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

Return a list of ``str`` of the guild members' names that match ``role`` if ``as_names=True``. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

**8) Search for guild members by rank.**

```python
get_members_by_rank(rank, names=False)
```

``PARAMS``:
- ``rank``: ``int`` rank to search.
- ``as_names``: ``boolean``. If ``True``, return the guild members that match the rank as a list of ``str`` of their names. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

Return a list of ``str`` of the guild members' names that match ``rank`` if ``as_names=True``. Otherwise, Return the members as dictionaries (see ``get_member_info()`` for dictionary keys).

#### _Retrieving guild achievements data:_

**1) Raw API guild achievements data.**

```python
MyGuild.get_achievements_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'achievements'.

See https://dev.battle.net/io-docs for details.

**2) Whether or not the guild has an achievement completed.**

```python
MyGuild.has_achievement(achievement_id)
```

``PARAMS``:
- ``achievement_id``: ``int`` achievement ID to search.

Returns a ``boolean``. ``True`` if the selected guild has completed the achievement that matches ``achievement_id``. ``False`` otherwise.

#### _Retrieving guild news feed data:_

**1) Raw API guild news feed data.**

```python
MyGuild.get_guild_news_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'feed'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving guild challenge data:_

**1) Raw API guild challenge data.**

```python
MyGuild.get_guild_challenge_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'challenge'.

See https://dev.battle.net/io-docs for details.

**2) Selected guild's completed challenges.**

```python
MyGuild.get_completed_challenges(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. If ``True``, return the guild's completed challenges as a list of ``str`` of their names. Otherwise, Return the challenges in a list of dictionaries.

Return a list of ``str`` of the guild's completed challenge names if ``as_names=True``. Otherwise, Return the completed challenges in a list of dictionaries.

Keys in returned dictionary (elements of the list):
- ``realm``:
- ``map``:
- ``groups``:

**3) Whether or not the guild has completed a challenge.**

```python
MyGuild.has_challenge(name)
```

``PARAMS``:
- ``name``: ``str`` name of the challenge to search. Not case sensitive.

Returns a ``boolean``. ``True`` if the guild has completed the challenge called ``name``. ``False`` otherwise.

