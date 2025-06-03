# Data pipeline

## SUMMARY
- Core Kafka services (Zookeeper, Broker)

- Schema management (Schema Registry)

- Data integration (Kafka Connect)

- Monitoring (Control Center)

- Storage (TimescaleDB)

- Data simulation (Kafka producer)

## CONNECTIVITY DIAGRAM
```bash
                  +------------------------+
                  |      control-center    |
                  |      (Kafka UI)        |
                  +-----------+------------+
                              |
                              v
 +-----------+     +----------+-----------+     +---------------------+
 | zookeeper |<--->|   broker (Kafka)     |<--->|   schema-registry   |
 +-----------+     +----------+-----------+     +---------------------+
                                |
                          +-----+------+
                          |  connect    | <--- [ Connectors / JDBC / Sink ]
                          +-----+------+
                                |
                        +-------v------+
                        | timescaledb  |  (Stores structured data)
                        +--------------+

      +------------------+
      | kafka_producer   |  (Simulates input)
      +------------------+
```