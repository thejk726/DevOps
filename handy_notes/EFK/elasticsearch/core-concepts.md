## Architecture ##

* An elastic search cluster consists of one or more nodes that collectively store data and provide indexing and search capabilities.

* Clusters can scale horizontally by adding more nodes, enhancing both storage capacity and search throughput.

* In elastic search, data is stored in json format as documents. Each document is a unit of search and retrieval, grouped into indices which have a key to traditional database systems.

* `Indexing` is the process of storing documents in elasticsearch for quick retrieval. When a document is indexed, elastic search creates an inverted index allowing for fast form text searches.

* Searching in elasticsearch uses the thein `search` library to perform efficient and gainable search operation.

* It supports various queries including term queries, match queries etc.

* Elasticsearch splits indices into shards to handle large data volumes and distribute search operations. `Shards` are independent indices that can be hosted on any node and replicas are copies of these shards that ensure high availability and fault tolerance.

## Nodes and Clusters ##

A `node` is a single running instance of elasticsearch. A `cluster` is a collection of multiple nodes. A cluster can be setup in single or across multiple availability zones.

Each node can serve multiple roles such as storing data, indexing documents and executing search queries.

A cluster in elasticsearch provides a single `namespace` that specifies data managed.

Redundancy and high availability are ensured through replica shards which are copies of the primary shard. They ensure that in case of a node failure, the data remains available and the cluster continues to operate without any interruption.

Elasticsearch is designed to `scale horizontally`. New nodes can be added without downtime, automatically integrating into the cluster and distributing the workload.

### NodeRoles in Elasticsearch ###

1. Master node
* It's the brain of the elasticsearch cluster.
* Manages cluster-wide changes and maintains the metadata.
* Eg: When nodes and indices are created, or removed, the master node ensures these operations are executed smoothly.

2. Data node
* These nodes are responsible for storing and indexing the data.
* They handle search and aggregation queries, making them the workhorses of the cluster.

3. Data ingest node
* It pre-processes documents via ingest pipeline before indexing.
* Particularly useful for transforming or enriching data on the fly.

4. ML node
* Handles machine learning tasks like anomaly detection.
* They enable real-time data analysis and alerting.
* Eg: Detecting unusual spike in web traffic that may indicate a DoS attack

5. Transform node
* Execute data transformations.
* This is useful for summarizing or aggregating data over time.
* Eg: Transforming raw sales data to daily sales summary.

6. Remote cluster client
* Acts as a gateway for cross cluster searches.
* Enables search across multiple clusters as though they were a single entity providing a unified search experience even in a geographically distributed environment.

7. Data cold nodes
* Stores infrequently accessed data
* Optimized for costs rather than performance
* Best for archiving use cases

8. Data frozen nodes
* Stores rarely accessed data
* Prioritize costs with high latency

9. Data hot nodes
* Store frequently accessed data
* Optimized for low latency and high performance
* Eg: Real time analytics and dashboard

10. Data warm nodes
* Balance storage efficiency and performance for moderately accessed nodes
* Eg: Weekly reports


