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


DEFINITION = """
fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query SLODocuments {
  slo_documents: slo_document_v1 {
    name
    namespaces {
      name
      app {
        name
      }
      cluster {
        name
        automationToken {
          ... VaultSecret
        }
        prometheusUrl
        spec {
          private
        }
      }
    }
    slos {
      name
      expr
      SLIType
      SLOParameters {
        window
      }
      SLOTarget
      SLOTargetUnit
    }
  }
}
"""


class AppV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecV1(BaseModel):
    private: bool = Field(..., alias="private")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterV1(BaseModel):
    name: str = Field(..., alias="name")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    prometheus_url: str = Field(..., alias="prometheusUrl")
    spec: Optional[ClusterSpecV1] = Field(..., alias="spec")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceV1(BaseModel):
    name: str = Field(..., alias="name")
    app: AppV1 = Field(..., alias="app")
    cluster: ClusterV1 = Field(..., alias="cluster")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SLODocumentSLOSLOParametersV1(BaseModel):
    window: str = Field(..., alias="window")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SLODocumentSLOV1(BaseModel):
    name: str = Field(..., alias="name")
    expr: str = Field(..., alias="expr")
    sli_type: str = Field(..., alias="SLIType")
    slo_parameters: SLODocumentSLOSLOParametersV1 = Field(..., alias="SLOParameters")
    slo_target: float = Field(..., alias="SLOTarget")
    slo_target_unit: str = Field(..., alias="SLOTargetUnit")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SLODocumentV1(BaseModel):
    name: str = Field(..., alias="name")
    namespaces: list[NamespaceV1] = Field(..., alias="namespaces")
    slos: Optional[list[SLODocumentSLOV1]] = Field(..., alias="slos")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SLODocumentsQueryData(BaseModel):
    slo_documents: Optional[list[SLODocumentV1]] = Field(..., alias="slo_documents")

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> SLODocumentsQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        SLODocumentsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return SLODocumentsQueryData(**raw_data)
