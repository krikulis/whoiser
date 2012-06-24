#!/usr/bin/env python2.7
from dispatch import get_whois_query
import argparse 

def whois(domain):
    query = get_whois_query(domain)
    query = query()
    query.query(domain)
    return query.raw_response

def main():
    parser = argparse.ArgumentParser(description = "whois client program")
    parser.add_argument("domain", help = "domain name")
    args = parser.parse_args()
    try:    
        print whois(args.domain)
    except NotImplementedError as e:
        print str(e)
if __name__ == "__main__":
    main()
