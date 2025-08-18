'''
 
'''

import re

def sanitization(web):
    """
    Tokenizes and cleans the URL into meaningful parts.
    (Reused from your old code)
    """
    web = web.lower()
    token = []
    dot_token_slash = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')
        slash_token = []
        for j in range(0, len(raw1)):
            raw2 = str(raw1[j]).split('.')
            slash_token = slash_token + raw2
        dot_token_slash = dot_token_slash + raw1 + slash_token
    token = list(set(dot_token_slash))
    if 'com' in token:
        token.remove('com')
    return token

def extract_url_features(url):
    """
    Extracts basic statistical features from a URL.
    """
    features = {
        "length": len(url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": len(re.findall(r"[\W]", url)),  # non-alphanumeric
    }
    return features

# Debugging: run directly to test
if __name__ == "__main__":
    test_url = "http://example.com/test123"
    print("Sanitized:", sanitization(test_url))
    print("Extracted Features:", extract_url_features(test_url))