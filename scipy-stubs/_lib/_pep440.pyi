"""
This type stub file was generated by pyright.
"""

"""Utility to compare pep440 compatible version strings.

The LooseVersion and StrictVersion classes that distutils provides don't
work; they don't recognize anything like alpha/beta/rc/dev versions.
"""
__all__ = ["parse", "Version", "LegacyVersion", "InvalidVersion", "VERSION_PATTERN"]
class Infinity:
    def __repr__(self): # -> Literal['Infinity']:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __neg__(self): # -> Type[NegativeInfinity]:
        ...
    


Infinity = ...
class NegativeInfinity:
    def __repr__(self): # -> Literal['-Infinity']:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __neg__(self): # -> Type[Infinity]:
        ...
    


NegativeInfinity = ...
_Version = ...
def parse(version): # -> Version | LegacyVersion:
    """
    Parse the given version string and return either a :class:`Version` object
    or a :class:`LegacyVersion` object depending on if the given version is
    a valid PEP 440 version or a legacy version.
    """
    ...

class InvalidVersion(ValueError):
    """
    An invalid version was found, users should refer to PEP 440.
    """
    ...


class _BaseVersion:
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class LegacyVersion(_BaseVersion):
    def __init__(self, version) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def public(self): # -> str:
        ...
    
    @property
    def base_version(self): # -> str:
        ...
    
    @property
    def local(self): # -> None:
        ...
    
    @property
    def is_prerelease(self): # -> Literal[False]:
        ...
    
    @property
    def is_postrelease(self): # -> Literal[False]:
        ...
    


_legacy_version_component_re = ...
_legacy_version_replacement_map = ...
VERSION_PATTERN = ...
class Version(_BaseVersion):
    _regex = ...
    def __init__(self, version) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    @property
    def public(self): # -> str:
        ...
    
    @property
    def base_version(self): # -> LiteralString:
        ...
    
    @property
    def local(self): # -> str | None:
        ...
    
    @property
    def is_prerelease(self): # -> bool:
        ...
    
    @property
    def is_postrelease(self): # -> bool:
        ...
    


_local_version_seperators = ...
