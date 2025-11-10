import re
import requests

def check_url_safety(url):
    suspicious_patterns = [
        r'login.*\.', r'account.*\.', r'secure.*\.', 
        r'paypal|bank|amazon|facebook|google'
    ]
    
    result = {
        'safe': True,
        'warnings': [],
        'risk_score': 0
    }
    
    for pattern in suspicious_patterns:
        if re.search(pattern, url.lower()):
            result['warnings'].append(f"Contains suspicious pattern: {pattern}")
            result['risk_score'] += 20
    
    if not url.startswith('https://'):
        result['warnings'].append("Not using HTTPS - data may be intercepted")
        result['risk_score'] += 30
    
    domain = url.split('//')[-1].split('/')[0]
    if len(domain.split('.')) < 2:
        result['warnings'].append("Invalid domain format")
        result['risk_score'] += 25
    
    if result['risk_score'] > 50:
        result['safe'] = False
    
    return result
