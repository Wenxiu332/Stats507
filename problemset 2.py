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

import numpy as np
import random
import pandas as pd
from timeit import Timer
from collections import defaultdict
import feather


# ## Question 0

# a. for a given list of tuples, the function returns a list of tuples, 
# for every group of tuples that share the same first element, the returned list contains and only contains the one whose last element in the tuple is the largest among the group.<br>
# b. this code doesn't work because it forgets to consider that tuples start counting from one and that indexing the length of a tuple would result in going out of bounds error. This code is not easy to understand because of magic numbers, which I suggust substituting with parameterized numbers instead. Additionally, this code runs O(n^2) time with the double for loop structure, the efficiency could be improved by potentially using a hash table. Last but not list, I suggest the coder adding comments to the code to enhance readablity.

# ## Question 1

def listOfTuples(n, k=3, low = 0, high = 5):
    """
    Generate a list of n tuples of length tup_size of integers low to high.

    Parameters
    ----------
    n : integer
        The number of tuples in the list.
    tup_size : integer, optional
        The length of the tuples created. The default is 3.
    low : integer, optional
        The low end of the range to generate integers from.
    high : integer, optional
        The high end of hte range to generate integers from.
    rng: A random number generator object, e.g. from np.random.default_rng().
        If None, one is created within the context of the function.
    
    Returns
    -------
    A list of length `n` with tuples of size `tup_size` consting of uniform
    random integers in [low, high).
    """
    res = [tuple(np.random.randint(low, high, size = k)) for i in range(n)]
    return res
result = listOfTuples(5)
#print(result)
assert(all(isinstance(item, tuple) for item in result) and isinstance(result, list))
# ## Question 2


# ### a

def listofbigtup(sample_list):
    """
    Find tuples with maximum value in one position by unique value in another.
    
    Among all tuples in `tuple_list` sharing a common value in the `by`
    position, find those also having maximum value in the `max_of` position. 

    Parameters
    ----------
    tuple_list : list of tuples
        The list of tuples to organize as described above.
    
    Returns
    -------
    A list of all tuples, where, for each unique `by` value, the maximum
    value in the `max_of` position is achieved.
    """
    first_index = 0
    last_index = len(sample_list[0])-1
    op = []
    for m in range(len(sample_list)):
        li = [sample_list[m]]
        for n in range(len(sample_list)):
                if (sample_list[m][first_index] == sample_list[n][first_index] and
                        sample_list[m][last_index] != sample_list[n][last_index]):
                    li.append(sample_list[n])
        op.append(sorted(li, key=lambda dd: dd[last_index], reverse=True)[first_index])
    res = list(set(op))
    return res


# ### b

def improvedlistofbigtup(sample_list):
    """
    Find tuples with maximum value in one position by unique value in another.
    
    Among all tuples in `tuple_list` sharing a common value in the `by`
    position, find those also having maximum value in the `max_of` position. 

    Parameters
    ----------
    tuple_list : list of tuples
        The list of tuples to organize as described above.
   
    Returns
    -------
    A list of all tuples, where, for each unique `by` value, the maximum
    value in the `max_of` position is achieved.
    """
    first_index = 0
    last_index = len(sample_list[0])-1
    op = []
    for m in range(len(sample_list)):
        li = sample_list[m]
        for n in range(len(sample_list)):
            if (sample_list[m][first_index] == sample_list[n][first_index] and sample_list[m][last_index] < sample_list[n][last_index]):
                li = sample_list[n] ## substitute li if current tuple is of same first element and has bigger last element
        op.append(li)
    res = list(set(op))
    return res


# ### c

def newlistofbigtup(sample_list):
    """
    Find tuples with maximum value in one position by unique value in another.
    
    Among all tuples in `tuple_list` sharing a common value in the `by`
    position, find those also having maximum value in the `max_of` position. 

    Parameters
    ----------
    tuple_list : list of tuples
        The list of tuples to organize as described above.
    
    Returns
    -------
    A list of all tuples, where, for each unique `by` value, the maximum
    value in the `max_of` position is achieved.
    """
    mydict = {}
    res = []
    last_index = len(sample_list[0])-1
    for m in sample_list:
        if not m[0] in mydict:
            mydict[m[0]] = m[last_index]
        elif m[last_index] > mydict[m[0]]:
            mydict[m[0]] = m[last_index]
    for n in sample_list:
        if n[last_index] == mydict[n[0]]:
            res.append(n)
    return res


# ### d


time_nda = defaultdict(list)
for f in [listofbigtup, improvedlistofbigtup, newlistofbigtup]:
    t = Timer('f(k)', globals={'f': f, 'k':listOfTuples(5,3,0,9)})
    tm = t.repeat(repeat=9999, number = 1)
    time_nda["time"].append(np.median(tm))
print(time_nda)

# from the median runtime of three methods, we could see that the the function in c is much more efficient compared to b, which is more efficient compared to the function in a.

# ## Question 3
# ### a

# +

table1 = pd.read_sas('/Users/echoliao/Downloads/DEMO_G.XPT')
table2 = pd.read_sas('/Users/echoliao/Downloads/DEMO_H.XPT')
table3 = pd.read_sas('/Users/echoliao/Downloads/DEMO_I.XPT')
table4 = pd.read_sas('/Users/echoliao/Downloads/DEMO_J.XPT')
table1 = table1[["SEQN", "RIAGENDR","RIDAGEYR","RIDRETH3","DMDEDUC2","DMDMARTL", 
                "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]]
table2 = table2[["SEQN", "RIAGENDR","RIDAGEYR","RIDRETH3","DMDEDUC2","DMDMARTL", 
                "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]]
table3 = table3[["SEQN", "RIAGENDR","RIDAGEYR","RIDRETH3","DMDEDUC2","DMDMARTL", 
                "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]]
table4 = table4[["SEQN", "RIAGENDR","RIDAGEYR","RIDRETH3","DMDEDUC2","DMDMARTL", 
                "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]]
table1["year"] = pd.Series("2011-2012" for x in range(len(table1.index)))
table2["year"] = pd.Series("2013-2014" for x in range(len(table2.index)))
table3["year"] = pd.Series("2015-2016" for x in range(len(table3.index)))
table4["year"] = pd.Series("2017-2018" for x in range(len(table4.index)))
res = table1.append([table2, table3, table4])
res.rename({"SEQN": "unique_id", "RIDAGEYR":"age",
            "RIDRETH3":"race_and_ethnicity","DMDEDUC2":"education","DMDMARTL":"marital status", 
                "RIDSTATR":"interview/examination_status", 
                "SDMVPSU":"masked_variance_pseudo_psu", 
                "SDMVSTRA":"masked_variance_pseudo-stratum", 
                "WTMEC2YR":"full_sample_2_year_mec_exam_weight", 
                "WTINT2YR":"full_sample_2_year_interview_weight"}, axis = 1, inplace =True)
res = res.astype({"unique_id":str, "year":str})
# -


res.reset_index().to_feather("/Users/echoliao/Documents/stats507/demographic.ftr")


# ### b

# +

t1 = pd.read_sas('/Users/echoliao/Downloads/OHXDEN_G.XPT', format= 'xport', encoding='utf-8')
a = t1[["SEQN","OHDDESTS"]]
b = t1.filter(regex="OHX..TC" )
c = t1.filter(regex= "OHX..CTC")
b = b.replace({1:"primary_tooth_present",
                                          2:"permanent_tooth_present", 3:"dental_implant", 
                                          4:"tooth_not_present",
                                          5:"permanent_dental_root_fragment_present",
                                          np.nan:"missing"})
c = c.replace({"D": "Sound primary tooth",
               "E": "Missing due to dental disease",
               "J":"Permanent root tip is present but no restorative replacement is present",
               "M":"Missing due to other causes",
               "P":"Missing due to dental disease but replaced by a removable restoration",
               "Q": "Missing due to other causes but replaced by a removable restoration",
               "R":"Missing due to dental disease, but replaced by a fixed restoration",
               "S":"Sound permanent tooth",
               "T":"Permanent root tip is present but a restorative replacement is present",
               "U":"Unerupted",
               "X":"Missing due to other causes, but replaced by a fixed restoration",
               "Y":"Tooth present, condition cannot be assessed",
               "Z":"Permanent tooth with surface condition (s)",
               np.nan:"missing"
    })
t1 = pd.concat([a,b,c], axis = 1)
columnlist = ["unique_id", "dentition_status_code"]
for num in range(32):
    columnlist.append("tooth_count" + str(num+1))
for num in range(14):
    columnlist.append("coronal_caries" + str(num+2))
for num in range(14):
    columnlist.append("coronal_caries" + str(num+18))
t2 = pd.read_sas('/Users/echoliao/Downloads/OHXDEN_H.XPT', format= 'xport', encoding='utf-8')
d = t2[["SEQN","OHDDESTS"]]
e = t2.filter(regex="OHX..TC" )
f = t2.filter(regex= "OHX..CTC")
e = e.replace({1:"primary_tooth_present",
                                          2:"permanent_tooth_present", 3:"dental_implant", 
                                          4:"tooth_not_present",
                                          5:"permanent_dental_root_fragment_present",
                                          np.nan:"missing"})
f = f.replace({"D": "Sound primary tooth",
               "E": "Missing due to dental disease",
               "J":"Permanent root tip is present but no restorative replacement is present",
               "M":"Missing due to other causes",
               "P":"Missing due to dental disease but replaced by a removable restoration",
               "Q": "Missing due to other causes but replaced by a removable restoration",
               "R":"Missing due to dental disease, but replaced by a fixed restoration",
               "S":"Sound permanent tooth",
               "T":"Permanent root tip is present but a restorative replacement is present",
               "U":"Unerupted",
               "X":"Missing due to other causes, but replaced by a fixed restoration",
               "Y":"Tooth present, condition cannot be assessed",
               "Z":"Permanent tooth with surface condition (s)",
               np.nan:"missing"
    })
t2 = pd.concat([d,e,f], axis = 1)
t3 = pd.read_sas('/Users/echoliao/Downloads/OHXDEN_I.XPT', format= 'xport', encoding='utf-8')
g = t3[["SEQN","OHDDESTS"]]
h = t3.filter(regex="OHX..TC" )
i = t3.filter(regex= "OHX..CTC")
h = h.replace({1:"primary_tooth_present",
                                          2:"permanent_tooth_present", 3:"dental_implant", 
                                          4:"tooth_not_present",
                                          5:"permanent_dental_root_fragment_present",
                                          np.nan:"missing"})
i = i.replace({"D": "Sound primary tooth",
               "E": "Missing due to dental disease",
               "J":"Permanent root tip is present but no restorative replacement is present",
               "M":"Missing due to other causes",
               "P":"Missing due to dental disease but replaced by a removable restoration",
               "Q": "Missing due to other causes but replaced by a removable restoration",
               "R":"Missing due to dental disease, but replaced by a fixed restoration",
               "S":"Sound permanent tooth",
               "T":"Permanent root tip is present but a restorative replacement is present",
               "U":"Unerupted",
               "X":"Missing due to other causes, but replaced by a fixed restoration",
               "Y":"Tooth present, condition cannot be assessed",
               "Z":"Permanent tooth with surface condition (s)",
               np.nan:"missing"
    })
t3 = pd.concat([g,h,i], axis = 1)
t4 = pd.read_sas('/Users/echoliao/Downloads/OHXDEN_J.XPT', format= 'xport', encoding='utf-8')
j = t4[["SEQN","OHDDESTS"]]
k = t4.filter(regex="OHX..TC" )
l = t4.filter(regex= "OHX..CTC")
k = k.replace({1:"primary_tooth_present",
                                          2:"permanent_tooth_present", 3:"dental_implant", 
                                          4:"tooth_not_present",
                                          5:"permanent_dental_root_fragment_present",
                                          np.nan:"missing"})
l = l.replace({"D": "Sound primary tooth",
               "E": "Missing due to dental disease",
               "J":"Permanent root tip is present but no restorative replacement is present",
               "M":"Missing due to other causes",
               "P":"Missing due to dental disease but replaced by a removable restoration",
               "Q": "Missing due to other causes but replaced by a removable restoration",
               "R":"Missing due to dental disease, but replaced by a fixed restoration",
               "S":"Sound permanent tooth",
               "K":"Primary tooth with surface condition (s)",
               "T":"Permanent root tip is present but a restorative replacement is present",
               "U":"Unerupted",
               "X":"Missing due to other causes, but replaced by a fixed restoration",
               "Y":"Tooth present, condition cannot be assessed",
               "Z":"Permanent tooth with surface condition (s)",
               np.nan:"missing"
    })
t4 = pd.concat([j,k,l], axis = 1)
t1["year"] = pd.Series("2011-2012" for x in range(len(t1.index)))
t2["year"] = pd.Series("2013-2014" for x in range(len(t2.index)))
t3["year"] = pd.Series("2015-2016" for x in range(len(t3.index)))
t4["year"] = pd.Series("2017-2018" for x in range(len(t4.index)))
res1 = pd.concat([t1,t2,t3,t4], axis = 0)
columnlist.append("year")
res1.columns = columnlist
res1 = res1.astype({"unique_id":str, "year":str})
res1["dentition_status_code"] = res1["dentition_status_code"].replace({1:"complete", 2:"partial",3:"not_done"})
res1.reset_index().to_feather("/Users/echoliao/Documents/stats507/oral.ftr")
# -

# ### c

# total number of cases in the demographics dataset is 39156.
# and total number of cases in the oral dataset is 35909.
