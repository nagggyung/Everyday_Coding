--Q) 프로그래머스 코딩테스트 연습 GROUP BY 입양 시각 구하기(1)
-- 조건: (1) 9시 부터 19:59까지 각 시간대 별로 입양이 몇건이나 발생했는지 조회
--       (2) 결과는 시간대 순으로 정렬

select hour(DATETIME) as HOUR, 
count(hour(DATETIME)) as COUNT 
from ANIMAL_OUTS
where hour(DATETIME) BETWEEN 9 and 20
group by hour(DATETIME)
order by hour(DATETIME);

/*
hour() function returns the hour part for a given date (from 0 to 838)
*/