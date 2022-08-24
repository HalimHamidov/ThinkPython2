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
