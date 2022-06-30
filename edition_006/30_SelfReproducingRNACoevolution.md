# ALife Papers

# Evolutionary transition from a single RNA replicator to a multiple replicator network

by [Mituyoshi Yamazaki](https://twitter.com/vespid)

This research is an attempt to realize a host-parasite coevolution model aiming at Open-Ended Evolution.
*[https://webpark2056.sakura.ne.jp/papers/2022_Mizuuchi.pdf](https://webpark2056.sakura.ne.jp/papers/2022_Mizuuchi.pdf)*

## Research Content

The following two conditions are necessary for evolution:

- Self-replication ability
- Inheritance of changes in replication ability

How to build a simple model that meets these conditions?

### Previous Research

In Spiegelmann's previous study, self-replicating RNA was evolved by feeding it raw material and an RNA-replicating enzyme to replicate it, and repeating the same procedure for the next generation. As a result, RNA converged on the shortest gene that has a trait with high replication efficiency. 

**Cause of convergence:**
- The selection pressure of RNA did not change because only RNA was passed in each procedure and the same type of RNA replication enzyme was added.
- The information encoded by RNA was meaningless (the genetic information encoding the protein was included but not used for replication procedure)
    - The susceptibility to replication depended only on the physical properties of RNA and the replication enzyme.

### Research by Professor Ichihashi

In this paper, Professor Ichihashi continues the previous work by introducing a cell-free protein synthesis, and implementing a model in which RNA makes an RNA-replicating enzyme and the replicating enzyme makes RNA. RNA mutations also affect replication enzymes, avoiding convergence by changing the selection pressure of the system.

Along with that change, they introduced a cellular structure. (In order to prevent the generated RNA-replicating enzyme from drifting somewhere, the cell structure pre-encloses RNA and the necessary nutrients. If it drifts, the tragedy of the commons arises).

As a result of conducting experiments on such a system, the introduction of a cell-free protein synthesis system was not enough, and it converged and stopped evolving.

At this point, the parasite had already developed, but it was suppressed to not inhibit the host's self-renewal. After removing the repression and subculturing for a while, co-evolution began with the RNA of the host and the RNA of the parasite, and new parasites were born.

### Specifications of the system that produces parasites

There is room for parasites to occur in this system (parasites seem to almost always appear) because there are vulnerabilities in the replication process that can be used by others. In this system, RNA does not replicate by itself, but has a structure that allows an RNA replication enzyme to replicate itself. RNA with a sequence ★ recognized by the replication enzyme as the replication target is replicated. The parasite is RNA of sequence ★ that lacks a gene that encodes a replicating enzyme, and because of this missing gene, the parasite's sequence is shorter and therefore it has a faster replication rate than that of the host RNA.


# Impressions

## Specifications of the system that produces parasites

This does not depend on the specific implementation target, so it can be installed in any kind of system including software simulators. In particular, Professor Ikegami's Machines and Tapes system seems to be easy to embed because the model structure is similar.

## Multi-phased self-replication process

The multi-phased process automatically removes the difficulty of self-referencing.


## Explanation that evolved from RNA world to single cell

This research / experiment is, as it is, an explanation of how the RNA world has evolved into a single cell.

Since RNA needs a cellular structure to make and retain a replicating enzyme, it becomes a prerequisite for self-renewal. From that starting point, it already is the simplest form of a cell and easily developed into a fully functional ancestral cell.
