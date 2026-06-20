#!/bin/bash
# Negative examples: documents that MUST be rejected by the schema.
# Each case greps the EXACT expected constraint name, so dropping that constraint
# (document wrongly accepted) fails the build and can't be masked by another error.

set -u
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT_DIR=$( cd -- "${SCRIPT_DIR}/../.." &> /dev/null && pwd )
# CI uses the vendored 2025 Linux x86-64 xmllint ("Temporary xmllint master",
# https://github.com/TransmodelEcosystem/NeTEx/pull/915); set XMLLINT_BIN to a local
# xmllint to run this on any other OS or CPU architecture (macOS, Windows, ARM, ...).
XMLLINT="${XMLLINT_BIN:-${SCRIPT_DIR}/xmllint}"
cd "${ROOT_DIR}"

fail=0
assert_rejected() { # <file> <schema> <error-pattern>
  if "${XMLLINT}" --noout --schema "$2" "$1" 2>&1 | grep -q "$3"; then
    echo "OK               $1"
  else
    echo "SHOULD HAVE FAILED  $1 — not rejected by '$3' (constraint missing?)"
    fail=1
  fi
}

echo "Checking NeTEx 'should-fail' negative examples ..."
assert_rejected examples/should-fail/duplicate-GroupOfLinkSequences.xml xsd/NeTEx_publication.xsd GroupOfLinkSequences_UniqueBy_Id_Version

exit "${fail}"
