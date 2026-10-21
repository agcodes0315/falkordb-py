import pytest

from falkordb import FalkorDB
from falkordb.asyncio import FalkorDB as AsyncFalkorDB


@pytest.mark.parametrize("client_class", [FalkorDB, AsyncFalkorDB])
def test_select_graph_rejects_empty_name(client_class):
    client = client_class(host="localhost", port=6379)

    with pytest.raises(ValueError, match="Graph name cannot be empty"):
        client.select_graph("")


@pytest.mark.parametrize("client_class", [FalkorDB, AsyncFalkorDB])
@pytest.mark.parametrize("invalid_name", [None, 123, [], {}])
def test_select_graph_rejects_non_string_name(client_class, invalid_name):
    client = client_class(host="localhost", port=6379)

    with pytest.raises(TypeError, match="Expected a string parameter"):
        client.select_graph(invalid_name)


@pytest.mark.parametrize("client_class", [FalkorDB, AsyncFalkorDB])
def test_select_graph_accepts_valid_name(client_class):
    client = client_class(host="localhost", port=6379)

    graph = client.select_graph("test_graph")

    assert graph.name == "test_graph"
