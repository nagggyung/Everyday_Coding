--Q) 프로그래머스 코딩테스트 연습 SUM,MAX,MIN 최솟값 구하기 
-- 조건: (1) DATETIME 조회 (2) 가장 먼저 들어온 동물의 시간 조회

-- 다른 풀이:
-- select DATETIME as 시간 from ANIMAL_INS 
-- order by DATETIME asc limit 1;

select min(DATETIME) as 시간 from ANIMAL_INS;