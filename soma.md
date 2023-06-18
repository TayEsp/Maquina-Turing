bloco main 1
01 moverSoma 02
02 0 -- A i 11
02 1 -- B i 13
02 2 -- C i 15
02 3 -- D i 17
02 4 -- E i 19
02 5 -- F i 21
02 6 -- G i 23
02 7 -- H i 25
02 8 -- I i 27
02 9 -- J i 29
02 _ -- * i 31
02 * -- * e 02

;leu nada
31 moverIgual 32
32 0 -- A i 40
32 1 -- B i 42
32 2 -- C i 44
32 3 -- D i 46
32 4 -- E i 48
32 5 -- F i 50
32 6 -- G i 52
32 7 -- H i 54
32 8 -- I i 56
32 9 -- J i 58
32 + -- * d 61
32 * -- * e 32

;leu 0
11 moverIgual 12
12 0 -- A i 40
12 1 -- B i 42
12 2 -- C i 44
12 3 -- D i 46
12 4 -- E i 48
12 5 -- F i 50
12 6 -- G i 52
12 7 -- H i 54
12 8 -- I i 56
12 9 -- J i 58
12 + -- * i 40
12 * -- * e 12

;leu 1
13 moverIgual 14
14 0 -- A i 42
14 1 -- B i 44
14 2 -- C i 46
14 3 -- D i 48
14 4 -- E i 50
14 5 -- F i 52
14 6 -- G i 54
14 7 -- H i 56
14 8 -- I i 58
14 9 -- J i 70
14 + -- * i 42
14 * -- * e 14

;leu 2
15 moverIgual 16
16 0 -- A i 44
16 1 -- B i 46
16 2 -- C i 48
16 3 -- D i 50
16 4 -- E i 52
16 5 -- F i 54
16 6 -- G i 56
16 7 -- H i 58
16 8 -- I i 70
16 9 -- J i 73
16 + -- * i 44
16 * -- * e 16

;leu 3
17 moverIgual 18
18 0 -- A i 46
18 1 -- B i 48
18 2 -- C i 50
18 3 -- D i 52
18 4 -- E i 54
18 5 -- F i 56
18 6 -- G i 58
18 7 -- H i 70
18 8 -- I i 73
18 9 -- J i 76
18 + -- * i 46
18 * -- * e 18

;leu 4
19 moverIgual 20
20 0 -- A i 48
20 1 -- B i 50
20 2 -- C i 52
20 3 -- D i 54
20 4 -- E i 56
20 5 -- F i 58
20 6 -- G i 70
20 7 -- H i 73
20 8 -- I i 76
20 9 -- J i 79
20 + -- * i 48
20 * -- * e 20

;leu 5
21 moverIgual 22
22 0 -- A i 50
22 1 -- B i 52
22 2 -- C i 54
22 3 -- D i 56
22 4 -- E i 58
22 5 -- F i 70
22 6 -- G i 73
22 7 -- H i 76
22 8 -- I i 79
22 9 -- J i 82
22 + -- * i 50
22 * -- * e 22

;leu 6
23 moverIgual 24
24 0 -- A i 52
24 1 -- B i 54
24 2 -- C i 56
24 3 -- D i 58
24 4 -- E i 70
24 5 -- F i 73
24 6 -- G i 76
24 7 -- H i 79
24 8 -- I i 82
24 9 -- J i 85
24 + -- * i 52
24 * -- * e 24

;leu 7
25 moverIgual 26
26 0 -- A i 54
26 1 -- B i 56
26 2 -- C i 58
26 3 -- D i 70
26 4 -- E i 73
26 5 -- F i 76
26 6 -- G i 79
26 7 -- H i 82
26 8 -- I i 85
26 9 -- J i 89
26 + -- * i 54
26 * -- * e 26

;leu 8
27 moverIgual 28
28 0 -- A i 56
28 1 -- B i 58
28 2 -- C i 70
28 3 -- D i 73
28 4 -- E i 76
28 5 -- F i 79
28 6 -- G i 82
28 7 -- H i 85
28 8 -- I i 89
28 9 -- J i 93
28 + -- * i 56
28 * -- * e 28

;leu 9
29 moverIgual 30
30 0 -- A i 58
30 1 -- B i 70
30 2 -- C i 73
30 3 -- D i 76
30 4 -- E i 79
30 5 -- F i 82
30 6 -- G i 85
30 7 -- H i 89
30 8 -- I i 93
30 9 -- J i 96
30 + -- * i 58
30 * -- * e 30

;escreve 0
40 resultado 41
41 _ -- a d 60

;escreve 1
42 resultado 43
43 _ -- b d 60

;escreve 2
44 resultado 45
45 _ -- c d 60

;escreve 3
46 resultado 47
47 _ -- d d 60

;escreve 4
48 resultado 49
49 _ -- e d 60

;escreve 5
50 resultado 51
51 _ -- f d 60

;escreve 6
52 resultado 53
53 _ -- g d 60

;escreve 7
54 resultado 55
55 _ -- h d 60

;escreve 8
56 resultado 57
57 _ -- i d 60

;escreve 9
58 resultado 59
59 _ -- j d 60

;Carry 0
70 resultado 71
71 _ -- a d 72
72 carry 60

;Carry 1
73 resultado 74
74 _ -- b d 75
75 carry 60

;Carry 2
76 resultado 77
77 _ -- c d 78
78 carry 60

;Carry 3
79 resultado 80
80 _ -- d d 81
81 carry 60

;Carry 4
82 resultado 83
83 _ -- e d 84
84 carry 60

;Carry 5
85 resultado 86
86 _ -- f d 87
88 carry 60

;Carry 6
89 resultado 90
91 _ -- g d 92
92 carry 60

;Carry 7
93 resultado 94
94 _ -- h d 95
95 carry 60

;Carry 8
96 resultado 97
97 _ -- i d 98
98 carry 60

;Carry 9
99 resultado 100
100 _ -- j d 101
101 carry 60

60 inicio 01

61 trocar 62

62 sim pare

fim; acaba bloco main

; BLOCO CARRY
bloco carry 1
01 moverSoma 02
02 0 -- A i 11
02 1 -- B i 13
02 2 -- C i 15
02 3 -- D i 17
02 4 -- E i 19
02 5 -- F i 21
02 6 -- G i 23
02 7 -- H i 25
02 8 -- I i 27
02 9 -- J i 29
02 _ -- * i 31
02 * -- * e 02

;leu nada
31 moverIgual 32
32 0 -- A i 42
32 1 -- B i 44
32 2 -- C i 46
32 3 -- D i 48
32 4 -- E i 50
32 5 -- F i 52
32 6 -- G i 54
32 7 -- H i 56
32 8 -- I i 58
32 9 -- J i 70
32 _ -- b d retorne
32 * -- * e 32

;leu 0
11 moverIgual 12
12 0 -- A i 42
12 1 -- B i 44
12 2 -- C i 46
12 3 -- D i 48
12 4 -- E i 50
12 5 -- F i 52
12 6 -- G i 54
12 7 -- H i 56
12 8 -- I i 58
12 9 -- J i 70
12 + -- * i 40
12 * -- * e 12

;leu 1
13 moverIgual 14
14 0 -- A i 44
14 1 -- B i 46
14 2 -- C i 48
14 3 -- D i 50
14 4 -- E i 52
14 5 -- F i 54
14 6 -- G i 56
14 7 -- H i 58
14 8 -- I i 70
14 9 -- J i 73
14 + -- * i 44
14 * -- * e 14

;leu 2
15 moverIgual 16
16 0 -- A i 46
16 1 -- B i 48
16 2 -- C i 50
16 3 -- D i 52
16 4 -- E i 54
16 5 -- F i 56
16 6 -- G i 58
16 7 -- H i 70
16 8 -- I i 73
16 9 -- J i 76
16 + -- * i 46
16 * -- * e 16

;leu 3
17 moverIgual 18
18 0 -- A i 48
18 1 -- B i 50
18 2 -- C i 52
18 3 -- D i 54
18 4 -- E i 56
18 5 -- F i 58
18 6 -- G i 70
18 7 -- H i 73
18 8 -- I i 76
18 9 -- J i 79
18 + -- * i 48
18 * -- * e 18

;leu 4
19 moverIgual 20
20 0 -- A i 50
20 1 -- B i 52
20 2 -- C i 54
20 3 -- D i 56
20 4 -- E i 58
20 5 -- F i 70
20 6 -- G i 73
20 7 -- H i 76
20 8 -- I i 79
20 9 -- J i 82
20 + -- * i 50
20 * -- * e 20

;leu 5
21 moverIgual 22
22 0 -- A i 52
22 1 -- B i 54
22 2 -- C i 56
22 3 -- D i 58
22 4 -- E i 70
22 5 -- F i 73
22 6 -- G i 76
22 7 -- H i 79
22 8 -- I i 82
22 9 -- J i 85
22 + -- * i 52
22 * -- * e 22

;leu 6
23 moverIgual 24
24 0 -- A i 54
24 1 -- B i 56
24 2 -- C i 58
24 3 -- D i 70
24 4 -- E i 73
24 5 -- F i 76
24 6 -- G i 79
24 7 -- H i 82
24 8 -- I i 85
24 9 -- J i 89
24 + -- * i 54
24 * -- * e 24

;leu 7
25 moverIgual 26
26 0 -- A i 56
26 1 -- B i 58
26 2 -- C i 70
26 3 -- D i 73
26 4 -- E i 76
26 5 -- F i 79
26 6 -- G i 82
26 7 -- H i 85
26 8 -- I i 89
26 9 -- J i 93
26 + -- * i 56
26 * -- * e 26

;leu 8
27 moverIgual 28
28 0 -- A i 58
28 1 -- B i 70
28 2 -- C i 73
28 3 -- D i 76
28 4 -- E i 79
28 5 -- F i 82
28 6 -- G i 85
28 7 -- H i 89
28 8 -- I i 93
28 9 -- J i 96
28 + -- * i 58
28 * -- * e 28

;leu 9
29 moverIgual 30
30 0 -- A i 70
30 1 -- B i 73
30 2 -- C i 76
30 3 -- D i 79
30 4 -- E i 82
30 5 -- F i 85
30 6 -- G i 89
30 7 -- H i 93
30 8 -- I i 96
30 9 -- J i 99
30 + -- * i 70
30 * -- * e 30

;escreve 0
40 resultado 41
41 _ -- a d retorne

;escreve 1
42 resultado 43
43 _ -- b d retorne

;escreve 2
44 resultado 45
45 _ -- c d retorne

;escreve 3
46 resultado 47
47 _ -- d d retorne

;escreve 4
48 resultado 49
49 _ -- e d retorne

;escreve 5
50 resultado 51
51 _ -- f d retorne

;escreve 6
52 resultado 53
53 _ -- g d retorne

;escreve 7
54 resultado 55
55 _ -- h d retorne

;escreve 8
56 resultado 57
57 _ -- i d retorne

;escreve 9
58 resultado 59
59 _ -- j d retorne

;Carry 0
70 resultado 71
71 _ -- a d 72
72 carry 61

;Carry 1
73 resultado 74
74 _ -- b d 75
75 carry 61

;Carry 2
76 resultado 77
77 _ -- c d 78
78 carry 61

;Carry 3
79 resultado 80
80 _ -- d d 81
81 carry 61

;Carry 4
82 resultado 83
83 _ -- e d 84
84 carry 61

;Carry 5
85 resultado 86
86 _ -- f d 87
87 carry 61

;Carry 6
89 resultado 90
91 _ -- g d 92
92 carry 61

;Carry 7
93 resultado 94
94 _ -- h d 95
95 carry 61

;Carry 8
96 resultado 97
97 _ -- i d 98
98 carry 61

;Carry 9
99 resultado 100
100 _ -- j d 101
101 carry 61

60 inicio 01

61 * -- * i retorne

fim ; acaba bloco carry

bloco moverSoma 1
01 + -- * e retorne
01 * -- * d 01

fim; acaba bloco moverSoma

bloco moverIgual 1
01 = -- * e retorne
01 * -- * d 01

fim; acaba moverIgual 

bloco resultado 1
01 _ -- * i retorne
01 * -- * e 01

fim; acaba resultado

bloco inicio 1
01 _ -- * d retorne
01 * -- * e 01

fim; acaba inicio

bloco trocar 1
01 _ -- * d 02
01 * -- * e 01

02 A -- * i retorne
02 B -- * i retorne
02 C -- * i retorne
02 D -- * i retorne
02 E -- * i retorne
02 F -- * i retorne
02 G -- * i retorne
02 H -- * i retorne
02 I -- * i retorne
02 J -- * i retorne
02 a -- _ d 03
02 b -- _ d 04 
02 c -- _ d 05
02 d -- _ d 06
02 e -- _ d 07
02 f -- _ d 08
02 g -- _ d 09
02 h -- _ d 10
02 i -- _ d 11
02 j -- _ d 12

;leu 0
03 _ -- 0 e 01
03 * -- * d 03

;leu 1
04 _ -- 1 e 01
04 * -- * d 04

;leu 2
05 _ -- 2 e 01
05 * -- * d 05

;leu 3
06 _ -- 3 e 01
06 * -- * d 06

;leu 4
07 _ -- 4 e 01
07 * -- * d 07

;leu 5
08 _ -- 5 e 01
08 * -- * d 08

;leu 6
09 _ -- 6 e 01
09 * -- * d 09

;leu 7
10 _ -- 7 e 01
10 * -- * d 10

;leu 8
11 _ -- 8 e 01
11 * -- * d 11

;leu 9
12 _ -- 9 e 01
12 * -- * d 12

fim ; 

bloco sim 1
01 A -- 0 d 01
01 B -- 1 d 01
01 C -- 2 d 01
01 D -- 3 d 01
01 E -- 4 d 01
01 F -- 5 d 01
01 G -- 6 d 01
01 H -- 7 d 01
01 I -- 8 d 01
01 J -- 9 d 01
01 _ -- * i retorne
01 * -- * d 01
fim ;