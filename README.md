# Replicated Concurrency Control and Recovery

## Project Description

This project tries to simulate Replicated Concurrency Control and Recovery in a Database System. The objective is to implement a distributed database system with concurreny control and fault tolerance through concurrent transaction processing, data replication and site failure simulations.

We leverage the following algorithms to achieve the objectives:

1. Serializable Snapshot Isolation Algorithm for Concurrency Control and validation at commit time.
2. Available Copies Algorithm for Fault Tolerance and Recover

## Main Components

1. __Driver__: The project will have a root driver program to parse the input file comprising of transaction operations. The driver initializes the other components - the *Transaction Manager (TM)* and *10 Site Managers (SM)*. The parsed instructions are then passed into the Transaction Manager.

2. __Transaction Manager__: Transaction Manager will be responsible for maintaining the Data Broker (a data structure to store data replication info) and the Site Broker (a data structure to store site health information) and implementing the Available Copies algorithm between the 10 site managers

3. __Site Manager__: 10 Data Managers managing operations for every site.

4. __Site__: Each Site Manager manages a single __Site__ will store information about the data items stored in site. This includes *before images* of a data-item before a transaction commit and the *after images* of a data-item after commit. This will allow the site to maintain correct status if a Transaction aborts.

## UML Diagram

