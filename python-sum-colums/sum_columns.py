import pandas as pd
import argparse


def convert_to_df(file_name):
    # Returning dataframe converted from prvided as argument csv file
    with open(file_name) as f:
        df = pd.read_csv(f)
    return df


def sum_column(df, id):
    # Summing column with provided id and print the output in the CLI
    column = df.iloc[:, [id]]
    sum_of_column = df.iloc[:, [id]].sum(numeric_only=True).round(1)
    if not sum_of_column.empty:
        print(
            f'Sum of "{column.columns[0]}" column is equal {sum_of_column[0]}'
        )
    else:
        print(f'Column: {column.columns[0]} has non number type')



if __name__ == "__main__":
    # Parsing the arguments and run the program
    parser = argparse.ArgumentParser(
        description="Script sums values from specific column from csv files. "
    )
    parser.add_argument(
        "csv_name",
        metavar="FILE_NAME",
        type=argparse.FileType("r"),
        help="csv source file",
    )
    parser.add_argument("id", type=int, help="index of column to sum")

    args = parser.parse_args()
    df = convert_to_df(args.csv_name.name)
    sum_column(df, args.id)
