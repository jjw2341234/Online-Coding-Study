# [Silver I] Bitaro the Brave 2 - 33725 

[문제 링크](https://www.acmicpc.net/problem/33725) 

### 성능 요약

메모리: 222404 KB, 시간: 324 ms

### 분류

그리디 알고리즘, 수학, 누적 합

### 제출 일자

2025년 4월 16일 15:01:34

### 문제 설명

<p>Bitaro, the brave hero, has set out on an adventure to defeat monsters.</p>

<p>Bitaro has a strength value, denoted as $x$, which starts at an initial value. There are $N$ monsters, each labeled with a number from $1$ to $N$. To defeat the $i$-th monster ($1 ≤ i ≤ N$), Bitaro must have a strength of at least $A_i$. Defeating the $i$-th monster increases Bitaro’s strength by $B_i$.</p>

<p>Bitaro wants to defeat all the monsters using the following strategy:</p>

<ol>
	<li>Start with a specific monster $j$ ($1 ≤ j ≤ N$) and defeat the monsters in order: $j, j + 1, \dots , N$.</li>
	<li>If $j ≥ 2$, go back and defeat the monsters $1, 2, \dots , j − 1$ in sequence.</li>
</ol>

<p>Given the information about the monsters, write a program to determine the minimum initial strength $x$ required for Bitaro to defeat all the monsters.</p>

### 입력 

 <p>Read the following data from the standard input.</p>

<blockquote>
<p>$N$</p>

<p>$A_1$ $A_2$ $\dots$ $A_N$</p>

<p>$B_1$ $B_2$ $\dots$ $B_N$</p>
</blockquote>

### 출력 

 <p>Output a single integer, the minimum initial strength $x$ required for Bitaro to defeat all the monsters.</p>

