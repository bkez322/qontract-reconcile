from reconcile.gql_definitions.common.clusters import (
    ClusterV1,
    query,
)
from reconcile.utils import gql
from reconcile.utils.gql import GqlApi


def get_clusters(
    gql_api: GqlApi | None = None,
    name: str | None = None,
) -> list[ClusterV1]:
    variables = {}
    if name:
        variables["name"] = name
    api = gql_api or gql.get_api()
    data = query(query_func=api.query, variables=variables)
    return list(data.clusters or [])
