# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # PS1

import math
import numpy as np
import scipy.stats as st
from timeit import Timer
import pandas as pd
from collections import defaultdict


# ## Question 0

#
# This is question o
#
# > Question 0 is about Markdown.
#
#
# The next question is about the **Fibonnaci sequence**, *Fn=Fn−2+Fn−1*. In part **a** we will define a Python function `fib_rec()`.
#
# Below is a …
#
# ### Level 3 Header
#
# Next, we can make a bulleted list:
# * Item 1
#     - detail 1
#     - detail 2
# * Item 2
# Finally, we can make an enumerated list:<br>
#  a.Item 1<br>
#  b.Item 2<br>
#  c.Item 3<br>

# ## Question 1
# ### a

# +

def fib_rec(n):
"""
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.
    
    This function computes $F_n$ using a linear-complexity recursion.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$.
    a, b : int, optional.
        Values to initialize the sequence $F_0 = a$, $F_1 = b$.

    Returns
    -------
    The Fibonacci number $F_n$.

    """   
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
print(fib_rec(0))
print(fib_rec(1))
print(fib_rec(2))   
print(fib_rec(7))
print(fib_rec(11))
print(fib_rec(13))


# -

# ### b.

# +

def fib_for(n):
"""
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ directly by iterating using a for loop.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$. 
    a, b : int, optional.
        Values to initialize the sequence $F_0 = a$, $F_1 = b$. 

    Returns
    -------
    The Fibonacci number $F_n$. 

    """
    first=0
    second = 1
    if n>1:
        for num in range(n-1):
            sum = first+second
            first = second
            second = sum
        return sum
    elif n==0:
        return 0
    else:
        return 1
print(fib_for(0))
print(fib_for(1))
print(fib_for(2))
print(fib_for(7))
print(fib_for(11))
print(fib_for(13))  


# -

# ### c

# +

def fib_whl(n):
    """
    Compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by direct summation, iterating using a
    while loop.

    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$.
    a, b : int, optional.
        Values to initialize the sequence $F_0 = a$, $F_1 = b$.

    Returns
    -------
    The Fibonacci number $F_n$.

    """
    count = 0
    n1,n2 = 0,1
    if n>1:
        while(count+1 < n):
            nth = n1+n2
            n1 = n2
            n2 = nth
            count +=1
        return nth
    elif n==1:
        return 1;
    else:
        return 0
print(fib_whl(0))
print(fib_whl(1))
print(fib_whl(2)) 
print(fib_whl(7))
print(fib_whl(11))
print(fib_whl(13))         


# -

# ### d

# +

def fib_rnd(n):
    """
    Directly compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by rounding $\phi^n / sqrt(5)$.
    The formula is used directly for n < 250, and is applied on the log scale
    for 250 <= n < 1478. A ValueError is raised for larger n to avoid
    overflow errors.


    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$, must be less than 1478.
    a, b : int, optional.
        Values to initialize the sequence $F_0 = a$, $F_1 = b$.

    Returns
    -------
    The Fibonacci number $F_n$ if n < 1478, else a ValueError.
    """
    phi = (1+math.sqrt(5))/2
    return round(math.pow(phi,n)/math.sqrt(5))
print(fib_rnd(0))
print(fib_rnd(1))
print(fib_rnd(2)) 
print(fib_rnd(7))
print(fib_rnd(11))
print(fib_rnd(13))   


# -

# ### e.

# +

def fib_flr(n):
    """
    Directly compute the Fibonacci number $F_n$, when $F_0 = a$ and $F_1 = b$.

    This function computes $F_n$ by finding the smallest integer less than
    $\phi^n / sqrt(5) + 0.5$. The formula is used directly for n < 250, and is
    applied on the log scale for 250 <= n < 1477. A ValueError is raised for
    larger n to avoid integer overflow.


    Parameters
    ----------
    n : int
        The desired Fibonacci number $F_n$, must be less than 1478.
    a, b : int, optional.
        Values to initialize the sequence $F_0 = a$, $F_1 = b$.

    Returns
    -------
    The Fibonacci number $F_n$ if n < 1477, else a ValueError.
    """
    phi = (1+math.sqrt(5))/2
    return math.floor(pow(phi,n)/math.sqrt(5)+1/2)
print(fib_flr(0))
print(fib_flr(1))
print(fib_flr(2)) 
print(fib_flr(7))
print(fib_flr(11))
print(fib_flr(13)) 
# -

# ### f

# +

time_nda = defaultdict(list)
for n in range(5,25,5):
    for f in [fib_rec,fib_for, fib_whl, fib_rnd,fib_flr]:
        t = Timer('f(n)', globals={'f': f, 'n':n})
        tm = t.repeat(repeat=10, number = 1)
        time_nda[n].append(np.median(tm))
time_nda = pd.DataFrame(time_nda).transpose()
time_nda.columns = ['fib_rec','fib_for', 'fib_whl', 'fib_rnd','fib_flr']
index = time_nda.index
index.name = "n"
time_nda

# -


# In the above table, value in cells are median runtime of five fib functions with n= 5,10,15,20. We observe that with increasnig n, fib_flr adn rib_rnd are faster than other three functions.

# ## Question 2
# ### a.

def pascal_row(n):
    """
    Compute an arbitrary row of Pacal's triangle.

    Row 0 is "1", row 1 is "1, 1".  

    Parameters
    ----------
    n : int
        The desired row.
 
    Returns
    -------
    A list with values for the desired row. 
    """
    zeroCol = 1;
    mylist = [zeroCol]
    for i in range(n):
        current = int(zeroCol * (n+1-(i+1))/(i+1))
        zeroCol = current
        mylist.append(zeroCol)
    return mylist
print(pascal_row(0))   
print(pascal_row(1))
print(pascal_row(2)) 
print(pascal_row(3))  
print(pascal_row(4)) 


# ### b.

def print_pascal_row(n):
    """
    Compute an arbitrary row of Pacal's triangle.

    Row 0 is "1", row 1 is "1, 1".  

    Parameters
    ----------
    n : int
        The desired number of rows.
    compact : bool, optional.
        If True, return a compact representation with minimal spacing. 
        Otherwise, return a representation with uniform spacing. 
        The default is True. 
 
    Returns
    -------
    A string which, when printed, displays the first n rows. 
    """
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(pascal_row(i)[j], end=" ")
        print()
print_pascal_row(10)


# ## Question3
# ### a.

def give_output(est, lwr, upr, level, outformat):
    """
    Output an estimate and confidence interval

    Parameters
    ----------
    est : estimate of average
    lwr : lower bound of the CI for the random variable
    upr : upper bound of the CI for the random variable
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    est = round(est,4)
    lwr = round(lwr, 4)
    upr = round(upr, 4)
    mydict = {'est':est, 'lwr':lwr, 
              'upr':upr, 'level':level}
    if outformat == "None":
        return mydict
    else:
        mystring = str(est)+ "[" + str(level) + "%CI:(" 
        mystring += str(lwr) 
        mystring +=  ","
        mystring += str(upr) 
        mystring += ")]"
        return mystring

def normal_theory(data, level, outformat):
    """
    compute the CI using normal theory method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    est = np.mean(data)
    sd = st.sem(data)
    lwr = est-st.norm.ppf(level/100)*sd
    upr = est+st.norm.ppf(level/100)*sd
    return give_output(est, lwr, upr, level, outformat)

def compute_point_and_interval(data, level, outformat = "string"):
    """
    compute the CI using normal theory method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    try:
        mylist = np.array(data)
    except:
        print("invalid input.")
    else:
        return normal_theory(mylist, level, outformat)


print(compute_point_and_interval([1,2,3], 99))  
print(compute_point_and_interval([1,2,3], 99, 'None'))   

# ###b
####i
def compute_binomial_interval(data, level , method, outformat = "string"):
    """
    compute the CI using binomial interval method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    method: the method to compute the CI
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    try:
        mylist = np.array(data)
    except:
        print("invalid input.")
    else:
        if(method == 'standard'):
            return stardard(mylist,level,outformat = "string")
        elif (method == 'clopper'):
            return Clopper(mylist,level,outformat = "string")
        elif (method == 'jeffery'):
            return Jeffery(mylist,level,outformat = "string")
        elif (method == 'agresti'):
            return Agresti(mylist,level,outformat = "string")

def stardard(data, level, outformat = "string"):
    """
    compute the CI using stardard method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    n = data.size
    x = sum(data)
    p = x/n
    z = st.norm.ppf(level/100)
    if (n*p < 12 or n*(1-p) < 12):
        print("Approximation condition not satisfied. ")
    return give_output(p, p-z*math.sqrt(p*(1-p)/n), p+z*math.sqrt(p*(1-p)/n),level, outformat)

def Clopper(data, level, outformat = "string"):
    """
    compute the CI using Clopper method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    alpha = (100- level)/100
    n = data.size
    x = sum(data)
    lwr = st.beta.ppf(alpha/2, x, n-x+1)
    upr = st.beta.ppf(1-alpha/2, x+1, n-x)
    est = (lwr + upr)/2
    return give_output(est, lwr, upr, level, outformat)

def Jeffery(data, level, outformat = "string"):
    """
    compute the CI using Jeffery method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    alpha = (100- level)/100
    n = data.size
    x = sum(data)
    lwr = max(0, st.beta.ppf(alpha/2, x+0.5, n-x+0.5))
    upr = min(1, st.beta.ppf(1-alpha/2, x+0.5, n-x+0.5))
    est = (lwr + upr)/2
    return give_output(est, lwr, upr, level, outformat)

def Agresti(data, level, outformat = "string"):
    """
    compute the CI using Agresti method

    Parameters
    ----------
    data : A 1-dimensional NumPy array or compatible sequence type (list, tuple).
        A data vector from which to form the estimates.
    level : float, optional.
        The desired confidence level, converted to a percent in the output.
        The default is 0.95.
    outformat : str or None, optional.
        If `None` a dictionary with entries `mean`, `level`, `lwr`, and
        `upr` whose values give the point estimate, confidence level (as a %),
        lower and upper confidence bounds, respectively. If a string, it's the
        result of calling the `.format_map()` method using this dictionary.
        The default is "{mean:.2f} [{level:.0f}%: ({lwr:.2f}, {upr:.2f})]".

    Returns
    -------
    By default, the function returns a string with a 95% confidence interval
    in the form "mean [95% CI: (lwr, upr)]". A dictionary containing the mean,
    confidence level, lower, bound, and upper bound can also be returned.

    """
    z = st.norm.ppf(level/100)
    n = data.size
    nest = n + z**2
    pest = ((sum(data) + z**2/2))/nest
    return give_output(pest, pest-z*math.sqrt(pest*(1-pest)/n), pest+z*math.sqrt(pest*(1-pest)/n),level, outformat)

    

# ###c.
mytable = defaultdict(list)
arr = [0]*48 + [1]*42
for level in [90,95,99]:
    for method in ['standard', 'clopper', 'jeffery', 'agresti']:
        mytable[level].append(compute_binomial_interval(arr, level , method, outformat = "string"))
alist = []
for level in [90,95,99]:
    alist.append(compute_point_and_interval(arr, level, outformat = "string"))
print("alist is", alist)
mytable = pd.DataFrame(mytable)        
mytable = mytable.transpose()
mytable.columns = ['standard', 'Clopper', 'Jeffery', 'Agresti']
index = mytable.index
index.name = 'confidence level'
mytable['normal thm'] = alist
mytable

# From above, 90% ci, normal thm produce the tightest Ci while and 95% and 99% confidence intervals both have tightest CI is contructed using Afresti-Coull method.



