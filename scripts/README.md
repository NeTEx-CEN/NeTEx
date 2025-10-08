## README

# XML Schema XPath selector cleaning

Executed via `python scripts/xsd_selector_clear.py xsd`
Filters `NeTEx_publication.xsd` for unknown elements that are being used in xsd:selector for xsd:key, xsd:keyref, and xsd:unique.
Elements that are not in the schema, cannot be referenced, hence they cannot be found in a document.
It also resolves issues with extra spaces in the xsd:selector.
