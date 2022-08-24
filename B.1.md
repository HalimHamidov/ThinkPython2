Exercise B.1. 
Read the Wikipedia page on Big-Oh notation at https://en.wikipedia.org/wiki/Big_O_notation and answer the following questions:

***
1. What is the order of growth of n3 + n2? What about 1000000n3 + n2? What about n3 + 1000000n2?

O(n3)

Ref. https://slidetodoc.com/order-of-growth-suppose-you-have-analyzed-two/

2. What is the order of growth of (n2 + n) · (n + 1)? Before you start multiplying, remember that you only need the leading term.

O(n3)

Ref. https://slidetodoc.com/order-of-growth-suppose-you-have-analyzed-two/

3. If f is in O(g), for some unspecified function g, what can we say about a f + b, where a and b are constants?

a*f+b = O(k*g) = O(g)

Ref.Wiki

4. If f1 and f2 are in O(g),what can we say about f1 + f2?

f1+f2 = O(g) is a convex cone.


Ref.Wiki

5. If f1 is in O(g) and f2 is in O(h),what can we say about f1 + f2?

O(max(g,h))


Ref.Wiki

6. If f1 is in O(g) and f2 is O(h),what can we say about f1 · f2?

O(g*h)


Ref.Wiki

***

More info"

4.1   Analysis of Algorithms

Order of growth classifications. We use just a few structural primitives (statements, conditionals, loops, and method calls) to build  programs, so very often the order of growth of our programs is one of just a few functions of the problem size, summarized in the table below.

Look at the  table

https://introcs.cs.princeton.edu/java/41analysis/

___________

What is a plain English explanation of "Big O" notation?

https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation?rq=1

BigOh complexity can be visualized with this graph:

___________

Some other exercises from stackoverflow:

Order of growth according to Big-O Notation [duplicate]

Ref. https://stackoverflow.com/questions/52248927/order-of-growth-according-to-big-o-notation

