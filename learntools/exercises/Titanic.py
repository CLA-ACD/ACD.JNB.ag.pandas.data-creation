import pandas as pd

from learntools.core import *

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv", index_col=0)

class Ejercicio1(EqualityCheckProblem):
    _var = 'p1'
    _expected = (
            df.shape,
    )

class Ejercicio2(EqualityCheckProblem):
    _var = 'p2'
    _expected = (
            df.head(),
    )

class Ejercicio3(EqualityCheckProblem):
    _var = 'p3'
    _expected = (
            df.Name,
    )

class Ejercicio4(EqualityCheckProblem):
    _var = 'p4'
    _expected = (
            df['Name'][7],
    )

class Ejercicio5(EqualityCheckProblem):
    _var = 'p5'
    _expected = (
            df.iloc[3, :],
    )

class Ejercicio6(EqualityCheckProblem):
    _var = 'p6'
    _expected = (
            df.iloc[5:11, 2:5],
    )

class Ejercicio7(EqualityCheckProblem):
    _var = 'p7'
    _expected = (
            df.describe(),
    )

class Ejercicio8(EqualityCheckProblem):
    _var = 'p8'
    _expected = (
            df.Name.describe(),
    )

class Ejercicio9(EqualityCheckProblem):
    _var = 'p9'
    _expected = (
            df.Age.unique(),
    )

class Ejercicio10(EqualityCheckProblem):
    _var = 'p10'
    _expected = (
            df.Age.value_counts(),
    )


qvars = bind_exercises(globals(), [
    Ejercicio1,
    Ejercicio2,
    Ejercicio3,
    Ejercicio4,
    Ejercicio5,
    Ejercicio6,
    Ejercicio7,
    Ejercicio8,
    Ejercicio9,
    Ejercicio10,
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)