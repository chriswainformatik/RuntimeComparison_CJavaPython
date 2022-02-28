# Runtime comparison between C, Java and Python

Based on [this article](https://medium.com/swlh/a-performance-comparison-between-c-java-and-python-df3890545f6d) I did a runtime comparison between (optimzied) C, Java and Python code. The code is doing matrix multiplication with nesetd for-loops. I also added a solution using `numpy` which seems to be the fastet (for C and Java I didn't use any libraries for matrix multiplication).

The C code was compiled by running

```
gcc -O3 main.c -o matrix
```
