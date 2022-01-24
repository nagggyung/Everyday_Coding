--Q) 프로그래머스 코딩테스트 연습 selct 상위 n개 레코드
-- 조건: (1) NAME 조회 (2) 가장 보호서에 먼저 들어온 동물 조회

select NAME from ANIMAL_INS order by DATETIME asc limit 1;

/*
* 상위 데이터 1개만 출력하기 
 limit 을 사용하여 일정 개수만 출력할 수 있다. 
 페이징 처리에 사용된다. 

ex1) 
SELECT name from animal_ins order by datetime asc limit 1;
상위 데이터 1개만 가져온다.

ex2) 
SELECT name from animal_ins order by datetime asc limit 1,10;
두번째 (1) 데이터 부터 10개의 데이터를 가져온다. 
=> 11번째 데이터(10) 까지 가져온다. (인덱스 0부터 시작)

ex3) 
SELECT name from animal_ins order by datetime asc limit 10, 10;
11번째(10) 데이터 부터 10개의 데이터를 가져온다. 

*/