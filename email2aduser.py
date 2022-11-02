#!/usr/bin/python3

import argparse


def args_init():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,prog="email2aduser",description="""Email list parser to AD user common format. 
    Common format: sharon.r.whorthy@example.com -> swhorthy
    Common format: sharon.whorthy@example.com   -> swhorthy
    Common format: swhorthy@example.com         -> swhorthy
Great for REDTEAM when you have a lot of emails from OSINT tools 
    and need to get AD userformat for bruteforce or spraying or 
    connecting to external/internal services, etc
Credits:
    https://elprofesor.io
    https://github.com/elprofesor96""", epilog="Example: email2aduser -f input_file.txt -o output_file.txt")
    parser.add_argument("-f", "--filename", help="input file to parse")
    parser.add_argument("-o", "--output", help="output file ")
    args = parser.parse_args()
    return args, parser

def open_input_list(list_file):
    f = open(list_file, 'r')
    data = f.readlines()
    f.close()
    return data

def parse_email_to_aduser(email):
    point_in_email = email.count('.')
    if point_in_email == 2 and '@' in email:
        split_email = email.split(sep=".")
        parsed_email = split_email[0][0] + split_email[1].split(sep='@')[0]
        return parsed_email
    elif point_in_email == 3 and '@' in email:
        split_email = email.split(sep=".")
        parsed_email = split_email[0][0] + split_email[2].split(sep='@')[0]
        return parsed_email
    elif point_in_email == 1 and '@' in email:
        parsed_email = email.split(sep='@')[0]
        return parsed_email
    else:
        pass


def write_output_list(input_list, output_list):
    f = open(output_list, 'w')
    f.writelines(input_list)
    f.close()
    return True

def main():
    args, parser = args_init()
    if args.filename and args.output:
        aduser_list = []
        data = open_input_list(args.filename)
        for email in data:
            aduser = parse_email_to_aduser(email)
            if aduser != None:
                aduser_list.append(aduser + '\n')
        write_output_list(aduser_list, args.output)
        print('\n[*] Data uploaded: ', len(data))
        print('[*] AdUsers parsed: ', len(aduser_list))
        print('[*] Writing output to: ', args.output)
        print('[*] Done')
    else:
        parser.print_help()
    

if __name__ == '__main__':
    main()
