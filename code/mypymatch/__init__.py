from __future__ import division
import statsmodels.api as sm
from statsmodels.genmod.generalized_linear_model import GLM

from statsmodels.tools.sm_exceptions import PerfectSeparationError
from statsmodels.tools.sm_exceptions import ConvergenceWarning

from statsmodels.distributions.empirical_distribution import ECDF
from scipy import stats

# Data manipulation
from collections import Counter
from itertools import chain

# Adjusts the system path to include the current script's directory, ensuring that local modules and functions can be imported correctly.
import sys; sys.path.append(sys.argv[0])

# Imports functions from the current package as uf
from . import functions as uf
import statsmodels.api as sm

# describing statistical models
import patsy

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Exceeding of maximum iterations in statistical calculations, indicated by ConvergenceWarning.
import warnings
warnings.filterwarnings(
    "error",
    message='Maximum number of iterations has been exceeded',
    category=ConvergenceWarning)