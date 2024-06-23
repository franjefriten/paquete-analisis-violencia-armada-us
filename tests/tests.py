import unittest
import pandas as pd
import numpy as np
import data_fetching.utils as data_fetch
import os
import data_processing.utils as data_process
import data_grouping.utils as data_group
import data_analysis.utils as data_analyze

os.chdir("..")
global cwd
cwd = os.getcwd()


class TestFetching(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._ruta_df_armas = os.path.join(
            cwd,
            r"data/nics-firearm-background-checks.csv"
        )
        cls._ruta_df_uspop = os.path.join(
            cwd,
            r"data/us-state-populations.csv"
        )
        print(cls.__name__, "Archivos cargados, set up hecho")

    def test_read_csv(self):
        self.assertIsInstance(
            data_fetch.read_csv(self._ruta_df_armas),
            pd.DataFrame,
            f"Fallo al cargar el dataset de armas {self._ruta_df_armas}"
        )
        self.assertIsInstance(
            data_fetch.read_csv(self._ruta_df_uspop),
            pd.DataFrame,
            f"Fallo al cargar el dataset {self._ruta_df_uspop}"
        )


class TestCleanCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._df = data_fetch.read_csv(os.path.join(
            cwd,
            r"data/nics-firearm-background-checks.csv"
        ))
        print(cls.__name__, "Archivos cargados, set up hecho")

    def test_clean_csv(self):
        self._df = data_fetch.clean_csv(self._df)

        self.assertIsInstance(
            self._df,
            pd.DataFrame,
            "Limpieza erronea"
        )

        self.assertCountEqual(
            self._df.columns,
            ['month', 'state', 'permit', 'handgun', 'long_gun'],
            f"Discrepancia en las columnas: {self._df.columns}"
        )

    def test_rename_cols(self):
        self._df = data_fetch.clean_csv(self._df)
        self._df = data_fetch.rename_cols(
                self._df,
                "long_gun",
                "long_gun"
            )

        self.assertCountEqual(
            self._df.columns,
            ['month', 'state', 'permit', 'handgun', 'long_gun']
        )


class TestDataProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._df = data_fetch.read_csv(os.path.join(
            cwd,
            r"data/nics-firearm-background-checks.csv"
        ))
        print(cls.__name__, "Archivos cargados, set up hecho!")
        cls._df = data_fetch.clean_csv(cls._df)
        print(cls.__name__, "Dataset Limpio!")
        cls._df = data_fetch.rename_cols(
                cls._df,
                "long_gun",
                "long_gun"
            )
        print(cls.__name__, "Columnas renombradas!")

    def test_breakdown_date(self):
        self._df = data_process.breakdown_date(self._df)
        self._df = data_process.erase_month(self._df)

        self.assertCountEqual(
            self._df.columns,
            ['month', 'state', 'permit', 'handgun', 'long_gun', 'year']
        )

        self.assertEqual(
            np.max(np.float128(self._df.year)),
            2020
        )

        self.assertEqual(
            np.min(np.float128(self._df.month)),
            1
        )

        self.assertEqual(
            np.max(np.float128(self._df.month)),
            12
        )


class TestDataGrouping(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._df = data_fetch.read_csv(os.path.join(
            cwd,
            r"data/nics-firearm-background-checks.csv"
        ))
        print(cls.__name__, "Archivos cargados, set up hecho!")
        cls._df = data_fetch.clean_csv(cls._df)
        print(cls.__name__, "Dataset Limpio!")
        cls._df = data_fetch.rename_cols(
                cls._df,
                "long_gun",
                "long_gun"
            )
        print(cls.__name__, "Columnas renombradas!")
        cls._df = data_process.breakdown_date(cls._df)
        cls._df = data_process.erase_month(cls._df)
        print(cls.__name__, "Fecha desplegada en mes y año")
        cls._df_grouped = data_group.groupby_state_and_year(cls._df)
        print(cls.__name__, "Agrupado por state y year")

    def test_print_biggest_handguns(self):
        data_group.print_biggest_handguns(self._df_grouped)

    def test_print_biggest_longguns(self):
        data_group.print_biggest_longguns(self._df_grouped)

    def test_groupby_state(self):
        data_group.groupby_state(self._df_grouped)
    

class TestCleanMerge(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._df = data_fetch.read_csv(os.path.join(
            cwd,
            r"data/nics-firearm-background-checks.csv"
        ))
        cls._ruta_df_uspop = os.path.join(
            cwd,
            r"data/us-state-populations.csv"
        )
        print(cls.__name__, "Archivos cargados, set up hecho!")
        cls._df = data_fetch.clean_csv(cls._df)
        print(cls.__name__, "Dataset Limpio!")
        cls._df = data_fetch.rename_cols(
            cls._df,
            "long_gun",
            "long_gun"
        )
        print(cls.__name__, "Columnas renombradas!")
        cls._df = data_process.breakdown_date(cls._df)
        cls._df = data_process.erase_month(cls._df)
        print(cls.__name__, "Fecha desplegada en mes y año")
        cls._df_grouped = data_group.groupby_state_and_year(cls._df)
        print(cls.__name__, "Agrupado por state y year")
        cls._df_grouped = data_fetch.clean_states(cls._df_grouped)
        print(cls.__name__, "State limpiado")

    def test_clean_states(self):
        self.assertEqual(
            list(set(self._df_grouped.obj.state.unique()).\
                 intersection(["Guam", "Virgin Islands", "Puerto Rico", "Mariana Islands"])
                 ),
            []
        )

    def test_merge_datasets(self):
        self._df = data_process.merge_datasets(self._df, self._ruta_df_uspop)

    def calculate_relative_values(self):
        self._df = data_analyze.calculate_relative_values(self._df)


if __name__ == "__main__":
    suite_fetch = unittest.TestSuite()
    suite_fetch.addTest(unittest.makeSuite(TestFetching))
    unittest.TextTestRunner(verbosity=2).run(suite_fetch)

    suite_clean = unittest.TestSuite()
    suite_clean.addTest(unittest.makeSuite(TestCleanCSV))
    unittest.TextTestRunner(verbosity=2).run(suite_fetch)

    suite_process = unittest.TestSuite()
    suite_process.addTest(unittest.makeSuite(TestDataProcessing))
    unittest.TextTestRunner(verbosity=2).run(suite_process)

    suite_group = unittest.TestSuite()
    suite_group.addTest(unittest.makeSuite(TestDataGrouping))
    unittest.TextTestRunner(verbosity=2).run(suite_group)

    suite_merge = unittest.TestSuite()
    suite_merge.addTest(unittest.makeSuite(TestCleanMerge))
    unittest.TextTestRunner(verbosity=2).run(suite_merge)