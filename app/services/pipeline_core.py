def clean_and_normalize(records):
    cleaned = []
    anomalies = 0
    for r in records:
        item = {}
        for k, v in r.items():
            k_clean = k.strip().lower().replace(" ", "_")
            if isinstance(v, str):
                v_clean = v.strip()
                if v_clean == "" or v_clean.lower() == "n/a":
                    v_clean = None
                    anomalies += 1
                item[k_clean] = v_clean
            else:
                item[k_clean] = v
        cleaned.append(item)
        
    summary = f"Processed {len(records)} records. Normalized column keys and flagged {anomalies} missing value anomalies."
    return len(records), cleaned, anomalies, summary
