from pathlib import Path
from lxml import etree
import json
import sys

# --- CONFIG ---
NS = {"xsd": "http://www.w3.org/2001/XMLSchema"}
BASE_DIR = Path(sys.argv[1])  # map met alle XSD bestanden
INPUT_XSD = OUTPUT_XSD = BASE_DIR / "NeTEx_publication.xsd"     # bestand dat je wilt herschrijven
REPORT_JSON = "report.json"

# --- 1. Verzamel alle element-namen uit alle XSD's (recursief, inclusief nested, negeer abstract) ---
all_elements = set()
for xsd_file in BASE_DIR.rglob("*.xsd"):
    tree = etree.parse(str(xsd_file))
    root = tree.getroot()
    for elem in root.findall(".//xsd:element", namespaces=NS):
        if elem.get("abstract") == "true":
            continue  # negeer abstract elements
        name = elem.get("name")
        if name:
            all_elements.add(name)

print(f"Totale elementen gevonden (excl. abstract): {len(all_elements)}")

# --- 2. Open het doelbestand ---
tree = etree.parse(str(INPUT_XSD))
root = tree.getroot()

# --- 3. Prepare report dictionary ---
report = {"removed_selectors": [], "removed_elements": [], "removed_comments": []}

# --- 4. Functie om selector xpath te filteren ---
def filter_selector(node):
    selector = node.find("xsd:selector", namespaces=NS)
    if selector is None:
        return False  # geen selector
    xpath_expr = selector.get("xpath")
    if not xpath_expr:
        return False
    exprs = [e.strip() for e in xpath_expr.split("|")]
    kept_exprs = []
    removed_exprs = []
    for e in exprs:
        # strip leading .// en namespace prefix
        e_clean = e.replace(".//", "").split(":")[-1]
        if e_clean in all_elements:
            kept_exprs.append(e)
        else:
            removed_exprs.append(e)
    if removed_exprs:
        report["removed_selectors"].append({
            "parent_name": node.get("name"),
            "removed_expressions": removed_exprs
        })
    selector.set("xpath", " | ".join(kept_exprs))  # altijd bijwerken
    print(f"[DEBUG] Node: {node.tag}, name: {node.get('name')}, kept expressions: {kept_exprs}")
    return bool(kept_exprs)  # True als minstens één expression overblijft

# --- 5. Helper: verwijder alle comments direct boven een node ---
def remove_comments_above(node):
    parent = node.getparent()
    prev = node.getprevious()
    removed_comments = []
    while prev is not None and isinstance(prev, etree._Comment):
        removed_comments.append(prev.text)
        parent.remove(prev)
        prev = node.getprevious()  # update na verwijderen
    if removed_comments:
        report["removed_comments"].append({
            "parent_name": node.get("name"),
            "removed_comments": removed_comments
        })
        print(f"[DEBUG] Removed comment(s) above '{node.get('name')}': {removed_comments}")

# --- 6. Eerste pass: filter key, unique, keyref selectors ---
for tag in ["key", "unique"]:
    for node in root.findall(f".//xsd:{tag}", namespaces=NS):
        has_expr = filter_selector(node)
        if not has_expr:
            remove_comments_above(node)
            report["removed_elements"].append({
                "type": tag,
                "name": node.get("name"),
                "reason": "all selector expressions removed"
            })
            print(f"[DEBUG] Removing {tag} '{node.get('name')}' (no expressions left)")
            node.getparent().remove(node)

for kr in root.findall(".//xsd:keyref", namespaces=NS):
    has_expr = filter_selector(kr)
    refer_name = kr.get("refer")
    if not has_expr or refer_name is None:
        remove_comments_above(kr)
        report["removed_elements"].append({
            "type": "keyref",
            "name": kr.get("name"),
            "reason": "all selector expressions removed or no refer"
        })
        print(f"[DEBUG] Removing keyref '{kr.get('name')}' (no expressions or no refer)")
        kr.getparent().remove(kr)

# --- 7. Tweede pass: verwijder keys die nergens meer door keyrefs gebruikt worden ---
used_keys = set()
for kr in root.findall(".//xsd:keyref", namespaces=NS):
    refer = kr.get("refer")
    if refer:
        used_keys.add(refer.split(":")[-1])  # strip namespace prefix

for k in root.findall(".//xsd:key", namespaces=NS):
    kname = k.get("name").split(":")[-1]  # strip prefix
    if kname not in used_keys:
        remove_comments_above(k)
        report["removed_elements"].append({
            "type": "key",
            "name": kname,
            "reason": "no keyrefs reference this key anymore"
        })
        print(f"[DEBUG] Removing key '{kname}' (no keyrefs reference it)")
        k.getparent().remove(k)

# --- 8. Schrijf het XSD-bestand opnieuw ---
tree.write(str(OUTPUT_XSD), encoding="utf-8", xml_declaration=True, pretty_print=True)

# --- 9. Schrijf JSON rapport ---
# with open(REPORT_JSON, "w", encoding="utf-8") as jf:
#    json.dump(report, jf, indent=2, ensure_ascii=False, default=str)

# print(f"Verwerkt XSD opgeslagen als {OUTPUT_XSD}")
# print(f"JSON rapport opgeslagen als {REPORT_JSON}")

