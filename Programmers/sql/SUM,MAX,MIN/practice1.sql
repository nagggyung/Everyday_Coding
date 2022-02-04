--Q) 프로그래머스 코딩테스트 연습 SUM,MAX,MIN 최댓값 구하기 
-- 조건: (1) DATETIME 조회 (2) 가장 늦게 들어온 동물의 시간 조회

-- 다른 풀이:
--  select DATETIME as 시간 from ANIMAL_INS 
--  order by DATETIME desc limit 1;

select max(DATETIME) as 시간 from ANIMAL_INS;

/*
max() function returns the largest value of the selected column.
min() function returns the smallest value of the selected column.
*/