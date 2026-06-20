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
# Behaviour assertion, parameterised by the caller: the document must be REJECTED, and
# the rejection output must contain <expected>. We test the outcome, not how it is
# enforced - passing "Duplicate key-sequence" accepts a unique, a key or a rename alike,
# as long as the duplicate is caught. Each future test declares its own <expected>.
# Fails closed: accepted, wrong reason, or xmllint not running all count as failures.
assert_rejected() { # <file> <schema> <expected error substring>
  out=$("${XMLLINT}" --noout --schema "$2" "$1" 2>&1); st=$?
  if [ "${st}" -eq 0 ]; then
    echo "SHOULD HAVE FAILED  $1 — accepted (must be rejected)"
    fail=1
  elif printf '%s\n' "${out}" | grep -q "$3"; then
    echo "OK                  $1"
  else
    echo "ERROR               $1 — rejected, but not matching '$3' (unrelated error / xmllint failure?)"
    fail=1
  fi
}

echo "Checking NeTEx 'should-fail' negative examples ..."
assert_rejected examples/should-fail/duplicate-GroupOfLinkSequences.xml xsd/NeTEx_publication.xsd "Duplicate key-sequence"

exit "${fail}"
