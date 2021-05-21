# [ll1-conv]

## QUESTAO 1

### G1
1. S ⟶ a
2. S ⟶ ( S )
3. S ⟶ S *
4. S ⟶ S S 
5. S ⟶ S | S

Não compatível com LL(1) por possuir recursividade e ambiguidade em suas regras.

### G2

1.  S ⟶ + S S
2.  S ⟶ * S S
3.  S ⟶ ~ S
4.  S ⟶ n

--- | + | * | ~ | n | $ 
--- | - | - | - | - | - 
 S  | 1 | 2 | 3 | 4 | 

First(S) = {+,*,~,n}
Follow(S) = {$}

### G3
1. S ⟶ S + S
2. S ⟶ S * S
3. S ⟶ - S
4. S ⟶ ( S ) 
5. S ⟶ n

Gramática compatível com LL(1).
