from scipy.stats import spearmanr

#This is ti find the correllation coefficent using the spearman equation of all the graphs
def find_Spearman_coefficient(data1, data2):
    """
    Short summary.

    Args:
        variable:

    Returns:
        Returns...
    """
    coef, p = spearmanr(data1, data2)
    print('Spearmans correlation coefficient: %.3f' % coef)
    # interpret the significance
    alpha = 0.05
    if p > alpha:
        print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
    else:
        print('Samples are correlated (reject H0) p=%.3f' % p)