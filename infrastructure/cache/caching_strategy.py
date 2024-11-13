class CacheConfig:
    class metadata_cache:
        ttl_seconds: 300
        max_size_mb: 1024
        eviction_policy: "LRU"
    
    class binary_cache:
        ttl_seconds: 3600
        max_size_gb: 50
        eviction_policy: "LFU"
    
    class search_cache:
        ttl_seconds: 60
        max_size_mb: 512
        eviction_policy: "LRU"