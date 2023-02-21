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

from reconcile.gql_definitions.fragments.jumphost_common_fields import (
    CommonJumphostFields,
)
from reconcile.gql_definitions.fragments.resource_values import ResourceValues
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  remotePort
  identity {
    ... VaultSecret
  }
}

fragment ResourceValues on ResourceValues_v1 {
    cpu
    memory
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query Namespaces {
  namespaces: namespaces_v1 {
    name
    delete
    labels
    clusterAdmin
    managedRoles
    app {
      name
      serviceOwners {
        name
        email
      }
    }
    managedExternalResources
    externalResources {
      provider
      provisioner {
        name
      }
      ... on NamespaceTerraformProviderResourceAWS_v1 {
        resources {
          provider
          ... on NamespaceTerraformResourceRDS_v1
          {
            identifier
            output_resource_name
            defaults
            replica_source
          }
          ... on NamespaceTerraformResourceECR_v1
          {
            region
            identifier
            output_resource_name
            mirror {
              url
              pullCredentials {
                ... VaultSecret
              }
              tags
              tagsExclude
            }
          }
        }
      }
    }
    cluster {
      name
      serverUrl
      insecureSkipTLSVerify
      jumpHost {
        ... CommonJumphostFields
      }
      automationToken {
        ... VaultSecret
      }
      clusterAdminAutomationToken {
        ... VaultSecret
      }
      internal
      disable {
        integrations
        e2eTests
      }
    }
    managedResourceNames {
      resource
      resourceNames
    }
    limitRanges {
      name
      limits {
        default {
          ... ResourceValues
        }
        defaultRequest {
          ... ResourceValues
        }
        max {
          ... ResourceValues
        }
        maxLimitRequestRatio {
          ... ResourceValues
        }
        min {
          ... ResourceValues
        }
        type
      }
    }
    quota {
      quotas {
        name
        resources {
          limits {
            ... ResourceValues
          }
          requests {
            ... ResourceValues
          }
          pods
        }
        scopes
      }
    }
  }
}
"""


class OwnerV1(BaseModel):
    name: str = Field(..., alias="name")
    email: str = Field(..., alias="email")

    class Config:
        smart_union = True
        extra = Extra.forbid


class AppV1(BaseModel):
    name: str = Field(..., alias="name")
    service_owners: list[OwnerV1] = Field(..., alias="serviceOwners")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ExternalResourcesProvisionerV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceExternalResourceV1(BaseModel):
    provider: str = Field(..., alias="provider")
    provisioner: ExternalResourcesProvisionerV1 = Field(..., alias="provisioner")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceTerraformResourceAWSV1(BaseModel):
    provider: str = Field(..., alias="provider")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceTerraformResourceRDSV1(NamespaceTerraformResourceAWSV1):
    identifier: str = Field(..., alias="identifier")
    output_resource_name: Optional[str] = Field(..., alias="output_resource_name")
    defaults: str = Field(..., alias="defaults")
    replica_source: Optional[str] = Field(..., alias="replica_source")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ContainerImageMirrorV1(BaseModel):
    url: str = Field(..., alias="url")
    pull_credentials: Optional[VaultSecret] = Field(..., alias="pullCredentials")
    tags: Optional[list[str]] = Field(..., alias="tags")
    tags_exclude: Optional[list[str]] = Field(..., alias="tagsExclude")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceTerraformResourceECRV1(NamespaceTerraformResourceAWSV1):
    region: Optional[str] = Field(..., alias="region")
    identifier: str = Field(..., alias="identifier")
    output_resource_name: Optional[str] = Field(..., alias="output_resource_name")
    mirror: Optional[ContainerImageMirrorV1] = Field(..., alias="mirror")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceTerraformProviderResourceAWSV1(NamespaceExternalResourceV1):
    resources: list[
        Union[
            NamespaceTerraformResourceRDSV1,
            NamespaceTerraformResourceECRV1,
            NamespaceTerraformResourceAWSV1,
        ]
    ] = Field(..., alias="resources")

    class Config:
        smart_union = True
        extra = Extra.forbid


class DisableClusterAutomationsV1(BaseModel):
    integrations: Optional[list[str]] = Field(..., alias="integrations")
    e2e_tests: Optional[list[str]] = Field(..., alias="e2eTests")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterV1(BaseModel):
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")
    insecure_skip_tls_verify: Optional[bool] = Field(..., alias="insecureSkipTLSVerify")
    jump_host: Optional[CommonJumphostFields] = Field(..., alias="jumpHost")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    cluster_admin_automation_token: Optional[VaultSecret] = Field(
        ..., alias="clusterAdminAutomationToken"
    )
    internal: Optional[bool] = Field(..., alias="internal")
    disable: Optional[DisableClusterAutomationsV1] = Field(..., alias="disable")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ManagedResourceNamesV1(BaseModel):
    resource: str = Field(..., alias="resource")
    resource_names: list[str] = Field(..., alias="resourceNames")

    class Config:
        smart_union = True
        extra = Extra.forbid


class LimitRangeItemV1(BaseModel):
    default: Optional[ResourceValues] = Field(..., alias="default")
    default_request: Optional[ResourceValues] = Field(..., alias="defaultRequest")
    max: Optional[ResourceValues] = Field(..., alias="max")
    max_limit_request_ratio: Optional[ResourceValues] = Field(
        ..., alias="maxLimitRequestRatio"
    )
    min: Optional[ResourceValues] = Field(..., alias="min")
    q_type: Optional[str] = Field(..., alias="type")

    class Config:
        smart_union = True
        extra = Extra.forbid


class LimitRangeV1(BaseModel):
    name: str = Field(..., alias="name")
    limits: list[LimitRangeItemV1] = Field(..., alias="limits")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ResourceQuotaItemResourcesV1(BaseModel):
    limits: Optional[ResourceValues] = Field(..., alias="limits")
    requests: Optional[ResourceValues] = Field(..., alias="requests")
    pods: Optional[int] = Field(..., alias="pods")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ResourceQuotaItemV1(BaseModel):
    name: str = Field(..., alias="name")
    resources: ResourceQuotaItemResourcesV1 = Field(..., alias="resources")
    scopes: Optional[list[str]] = Field(..., alias="scopes")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ResourceQuotaV1(BaseModel):
    quotas: list[ResourceQuotaItemV1] = Field(..., alias="quotas")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceV1(BaseModel):
    name: str = Field(..., alias="name")
    delete: Optional[bool] = Field(..., alias="delete")
    labels: Optional[Json] = Field(..., alias="labels")
    cluster_admin: Optional[bool] = Field(..., alias="clusterAdmin")
    managed_roles: Optional[bool] = Field(..., alias="managedRoles")
    app: AppV1 = Field(..., alias="app")
    managed_external_resources: Optional[bool] = Field(
        ..., alias="managedExternalResources"
    )
    external_resources: Optional[
        list[
            Union[NamespaceTerraformProviderResourceAWSV1, NamespaceExternalResourceV1]
        ]
    ] = Field(..., alias="externalResources")
    cluster: ClusterV1 = Field(..., alias="cluster")
    managed_resource_names: Optional[list[ManagedResourceNamesV1]] = Field(
        ..., alias="managedResourceNames"
    )
    limit_ranges: Optional[LimitRangeV1] = Field(..., alias="limitRanges")
    quota: Optional[ResourceQuotaV1] = Field(..., alias="quota")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespacesQueryData(BaseModel):
    namespaces: Optional[list[NamespaceV1]] = Field(..., alias="namespaces")

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> NamespacesQueryData:
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
        NamespacesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return NamespacesQueryData(**raw_data)
