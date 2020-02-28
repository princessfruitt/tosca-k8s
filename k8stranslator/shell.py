import sys
import argparse
import os

from k8stranslator.k8sCreate import translate


class TranslatorShell(object):
    def __init__(self, argv):

        parser = self.get_parser()
        (args, args_list) = parser.parse_known_args(argv)

        self.template_file = args.template_file
        self.validate_only = args.validate_only
        self.output_file = args.output_file

        self.working_dir = os.getcwd()

        output = translate(self.template_file)
        self.output_print(output)

    def get_parser(self):
        parser = argparse.ArgumentParser(prog="kube-parser")

        parser.add_argument('--template-file',
                            metavar='<filename>',
                            required=True,
                            help='YAML template to parse.')
        parser.add_argument('--validate-only',
                            action='store_true',
                            default=False,
                            help='Only validate input template, do not perform translation.')
        parser.add_argument('--output-file',
                            metavar='<filename>',
                            required=False,
                            help='')

        return parser

    def output_print(self, output_msg):
        if self.output_file:
            with open(self.output_file, 'w') as file_obj:
                file_obj.write(output_msg)
        else:
            print(output_msg)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    TranslatorShell(args)


if __name__ == '__main__':
    main()
