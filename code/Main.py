from ImportExport import ImportExport
from RowsAnalysis import RowsAnalysis
from Paths import data


def main():
    encoding_final = ImportExport.get_encoding(data)
    df = ImportExport.read_my_csv(encoding_final)
    # rows_analysis.rows_csv(df)
    # rows_analysis.read_number_of_null_values(df)
    RowsAnalysis.delete_null_columns(df)
    # rows_analysis.rows_csv(df)
    RowsAnalysis.read_number_of_null_values(df)
    RowsAnalysis.rename_column(df)
    RowsAnalysis.select_columns(df)
    RowsAnalysis.read_number_of_null_values(df)

    ImportExport.export_csv(df)


if __name__ == "__main__":
    main()
