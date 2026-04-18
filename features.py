import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    domain = urlparse(url).netloc

    # 1. having_IP_Address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(-1 if re.search(ip_pattern, url) else 1)

    # 2. URL_Length
    if len(url) < 54:
        features.append(1)
    elif len(url) <= 75:
        features.append(0)
    else:
        features.append(-1)

    # 3. Shortining_Service
    features.append(-1 if re.search(r'bit\.ly|goo\.gl|tinyurl|ow\.ly', url) else 1)

    # 4. having_At_Symbol
    features.append(-1 if '@' in url else 1)

    # 5. double_slash_redirecting
    features.append(-1 if url.rfind('//') > 6 else 1)

    # 6. Prefix_Suffix
    features.append(-1 if '-' in domain else 1)

    # 7. having_Sub_Domain
    if domain.count('.') == 1:
        features.append(1)
    elif domain.count('.') == 2:
        features.append(0)
    else:
        features.append(-1)

    # 8. SSLfinal_State
    features.append(1 if url.startswith('https') else -1)

    # 9. Domain_registeration_length (default)
    features.append(1)

    # 10. Favicon (default)
    features.append(1)

    # 11. port (default)
    features.append(1)

    # 12. HTTPS_token
    features.append(-1 if 'https' in domain else 1)

    # 13. Request_URL (default)
    features.append(1)

    # 14. URL_of_Anchor (default)
    features.append(1)

    # 15. Links_in_tags (default)
    features.append(1)

    # 16. SFH (default)
    features.append(1)

    # 17. Submitting_to_email
    features.append(-1 if "mailto:" in url else 1)

    # 18. Abnormal_URL (default)
    features.append(1)

    # 19. Redirect (default)
    features.append(1)

    # 20. on_mouseover (default)
    features.append(1)

    # 21. RightClick (default)
    features.append(1)

    # 22. popUpWidnow (default)
    features.append(1)

    # 23. Iframe (default)
    features.append(1)

    # 24. age_of_domain (default)
    features.append(1)

    # 25. DNSRecord (default)
    features.append(1)

    # 26. web_traffic (default)
    features.append(1)

    # 27. Page_Rank (default)
    features.append(1)

    # 28. Google_Index (default)
    features.append(1)

    # 29. Links_pointing_to_page (default)
    features.append(1)

    # 30. Statistical_report (default)
    features.append(1)

    return features
