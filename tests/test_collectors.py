```python
import pytest
import aiohttp
import asyncio
from src.collectors.base_collector import WikiSourceCollector, ArchiveOrgCollector

@pytest.mark.asyncio
async def test_wikisource_collector():
    async with WikiSourceCollector() as collector:
        results = await collector.collect()
        assert isinstance(results, list)
        assert len(results) > 0
        for item in results:
            assert 'text' in item
            assert 'metadata' in item

@pytest.mark.asyncio
async def test_archiveorg_collector():
    async with ArchiveOrgCollector() as collector:
        results = await collector.collect()
        assert isinstance(results, list)
        assert len(results) > 0
        for item in results:
            assert 'text' in item
            assert 'metadata' in item
