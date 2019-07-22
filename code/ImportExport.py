import chardet
import pandas as pd
from Paths import data, data_modified


class ImportExport:
    """
        FUNCIONES PARA:
            + IMPORTAR EL CSV
            + EXPORTAR EL CSV
    """

    def get_encoding(data):
        """
        FUNCION PARA OBTENER EL ENCODING DEL CSV QUE  VAMOS A TOMAR
        :return: encoding_final
        """
        rawdata = open(data, "rb").read()
        encoding_total = chardet.detect(rawdata)
        encoding_main = str(encoding_total).split('\'')
        # print(encoding_main)
        # print(encoding_main[3])
        print('\n' + encoding_main[3] + '\n' + 'ENCODING ----- EXITO' + '\n')
        return encoding_main[3]

    def read_my_csv(encoding_csv):
        """
        LEER EL CSV
        :param encoding_csv: encoding del csv
        :return: el DataSet con el que vamos a trabajar
        """
        df = pd.read_csv(data, header=0, encoding=encoding_csv, low_memory=False)
        print('CSV IMPORTADO ----- EXITO')
        return df

    def export_csv(df):
        """
        EXPORTA EL NUEVO DATASET MODIFICADO
        :param df: el DataSet que queremos obtener, el que hemos ido modificando
        :return: el DataSet con el que hemos trabajado
        """
        df.to_csv(data_modified)
        print('CSV MODIFICADO EXPORTADO ----- EXITO')

