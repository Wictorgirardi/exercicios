# [cfg-list]

## QUESTAO 01

### Item 1

Json

```
?start  :   list
?list   :   "[" elem ("," elem)* "]"
```

### Item 2

Lisp

```
?start  :   list
?list   :   "(" elem+ ")"
```

### Item 3

Lispii

```
?start  :   list
?list   :  "(" (elem ","?)+ ")"
```

### Item 4

Python

```
?start  :   list
?list   :   "[" (elem ",")+ "]"
```

### Item 5

Js

```
?start  :   list
?list   :   "[" (elem? ","+)+ "]"
```
