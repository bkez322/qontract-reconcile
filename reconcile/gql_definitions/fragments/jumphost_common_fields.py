"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


class CommonJumphostFields(BaseModel):
    hostname: str = Field(..., alias="hostname")
    known_hosts: str = Field(..., alias="knownHosts")
    user: str = Field(..., alias="user")
    port: Optional[int] = Field(..., alias="port")
    remote_port: Optional[int] = Field(..., alias="remotePort")
    identity: VaultSecret = Field(..., alias="identity")

    class Config:
        smart_union = True
        extra = Extra.forbid
