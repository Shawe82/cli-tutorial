import click
import os
from funcy import identity


def read_csv(*args):
    print(f"READ {args}")


def process_csv(*args):
    print(f"PROCESS {args}")
    return object()


def write_excel(*args):
    print(f"WRITE {args}")


def upload_to(*args):
    print(f"UPLOAD {args}")


@click.command()
@click.option(
    "--in",
    "-i",
    "in_file",
    required=True,
    help="Path to csv file to be processed.",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.option(
    "--out-file",
    "-o",
    default="./output.xlsx",
    help="Path to excel file to store the result.",
    type=click.Path(dir_okay=False),
)
@click.option("--verbose", is_flag=True, help="Verbose output")
@click.option(
    "--dev",
    "server_url",
    help="Upload to dev server",
    flag_value="https://dev.server.org/api/v2/upload",
)
@click.option(
    "--test",
    "server_url",
    help="Upload to test server",
    flag_value="https://test.server.com/api/v2/upload",
)
@click.option(
    "--prod",
    "server_url",
    help="Upload to prod server",
    flag_value="https://real.server.com/api/v2/upload",
    default=True,
)
@click.option('--user', prompt=True,
              default=lambda: os.environ.get('USER', ''))
@click.password_option()
def process(in_file, out_file, verbose, server_url, user, password):
    """ Processes the input file IN and stores the result to output
    file OUT.
    """
    print_func = print if verbose else identity
    print_func("We will start with the input")
    input = read_csv(in_file)
    print_func("Next we procees the data")
    output = process_csv(input)
    print_func("Finally, we dump it")
    write_excel(output, out_file)
    print_func("Upload it to the server")
    upload_to(server_url, output, user, password)


if __name__ == "__main__":
    process()
