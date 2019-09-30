# ML-naive-bayes-algorithm
Naive Bayes algorithm implementation in python
## Running instruction
python naive_bayes.py <training data> <test data>

* The first argument is the path name of the training file, where the training data is stored. The path name can specify any file stored on the local computer.
* The second argument is the path name of the test file, where the test data is stored. The path name can specify any file stored on the local computer.
* Both the training file and the test file are text files, containing data in tabular format. Each value is a number, and values are separated by white space. The i-th row and j-th column contain the value for the j-th feature of the i-th object. The only exception is the LAST column, that stores the class label for each object. 
