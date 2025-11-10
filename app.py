import argparse
from tools import check_password

def main():
    parser = argparse.ArgumentParser(description='Security tools to help you stay safe')
    parser.add_argument('--password', action='store_true', help='Check password strength with personalized suggestions')
    
    args = parser.parse_args()
    
    if args.password:
        check_password()
    else:
        print("Security Tools")
        print("=============")
        print("Available commands:")
        print("--password : Check password strength with personalized suggestions")
        print("\nExample: python app.py --password")
        print("\nRun with --password flag to start the password checker")

if __name__ == "__main__":
    main()
