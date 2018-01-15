NeTEX XML schema
(C) 2009-2017  NeTEX, CEN, Crown Copyright

# NeTwork EXchange
## Core, Part 1 (Network),  Part 2 (Timetables), Part3 (Fares) Schemas
Version 1.06 - Base version plus minor fixes comprising Norway contributions

Plus most of the 1.1 CRs

See the NeTEx UML Physical and Conceptual models for an UML view

The Part 1, Part 2 & Part3 Schemas include minor  corrections since the issue of the documents,

There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples

  - netex-v1.06.spp

There is also an Oxygen project file

  - netex-v1.06.xpr


## Getting Started

There are two main root schemas:

  - netex_publication : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object.

  - netex_siri.xsd : Embeds NeTEx XML model elements in the SIRI protocol  for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition:

  - nx.xsd : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.
    The NX schema is not intended for actual use.

There are XML examples of the use of both protocols, see examples subdirectory.
