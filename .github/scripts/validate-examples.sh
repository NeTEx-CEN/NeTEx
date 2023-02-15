#!/bin/bash
# Validate all OJP XML examples from the examples/ directory against the OJP XSD schema
#
# You need the binary `xmllint`
# apt-get install libxml2-utils

# The -e flag causes the script to exit as soon as one command returns a non-zero exit code
set -e

echo "Validating NeTEx XML examples ..."

if xmllint --noout --schema xsd/NeTEx_publication.xsd examples/functions/calendar/*xml examples/functions/fares/*xml examples/functions/grouping/*xml examples/functions/newModes/*xml examples/functions/patterns/*xml examples/functions/pointOfInterest/*xml examples/functions/simpleNetwork/*xml examples/functions/site/*xml examples/functions/stopPlace/*xml examples/functions/timetable/*xml examples/functions/validityCondition/*xml examples/functions/variant/*xml examples/functions/vehicleSchedule/*xml examples/functions/versioning/*xml examples/standards/epip/*xml examples/standards/era_uic/*xml examples/standards/fxc/*xml examples/standards/gbfs/*xml examples/standards/gtfs/*xml examples/standards/neptune/*xml  examples/standards/noptis/*xml examples/standards/tap_tsi/*xml examples/standards/txc/*xml examples/standards/vdv452/*/*xml examples/standards/vdv452/*/*/*xml; then
  echo -e '\033[0;32mValidating NeTEx XML examples succeeded\033[0m'
else
  echo -e '\033[0;31mValidating NeTEx XML examples failed\033[0m'
  exit 1
fi
