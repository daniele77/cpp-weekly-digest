def generate_report(items):
    lines = []
    lines.append("# C++ Weekly Guru Digest\n")

    grouped = {}
    for item in items:
        grouped.setdefault(item["source"], []).append(item)

    for section, entries in grouped.items():
        lines.append(f"## {section}\n")
        for e in entries:
            if "error" in e:
                lines.append(f"- ⚠️ **Error**: {e['error']}\n")
            else:
                lines.append(f"- [{e['title']}]({e['link']})\n")

    return "\n".join(lines)

