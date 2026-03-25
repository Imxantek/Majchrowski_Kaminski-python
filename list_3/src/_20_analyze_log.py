from _1_read_log import read_log
from _7_get_top_ips import get_top_ips
from _12_count_status_classes import count_status_classes
from _14_log_to_dict import log_to_dict
from _18_detect_sus import detect_sus

def analyze_log(log):

    top_ips_list = get_top_ips(log, 5)
    most_frequent_ips = {ip: count for ip, count in top_ips_list}

    uri_dict = log_to_dict(log, "uri")

    top_uris = sorted(uri_dict.keys(), key=lambda k: len(uri_dict[k]), reverse=True)[:5]
    most_frequent_uris = {uri: len(uri_dict[uri]) for uri in top_uris}

    method_dict = log_to_dict(log, "method")
    method_distribution = {method: len(entries) for method, entries in method_dict.items()}

    status_classes = count_status_classes(log)
    error_count = status_classes.get("4xx", 0) + status_classes.get("5xx", 0)

    sus_ip_set, median_val, mean_val = detect_sus(log, 25)

    return {
        "najczestsze_ip": most_frequent_ips,
        "najczestsze_uri": most_frequent_uris,
        "rozklad_metod": method_distribution,
        "liczba_bledow": error_count,
        "dodatkowe_statystyki": {
            "calkowita_liczba_zapytan": len(log),
            "srednia_zapytan_na_ip": round(mean_val, 2),
            "mediana_zapytan_na_ip": median_val,
            "liczba_podejrzanych_ip": len(sus_ip_set)
        }
    }

if __name__ == "__main__":
    log_data = read_log()
    raport = analyze_log(log_data)
    
    for klucz, wartosc in raport.items():
        if isinstance(wartosc, dict):
            print(f"{klucz}:")
            for sub_klucz, sub_wartosc in wartosc.items():
                print(f"  - {sub_klucz}: {sub_wartosc}")
        else:
            print(f"{klucz}: {wartosc}")