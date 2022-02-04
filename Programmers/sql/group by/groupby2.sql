--Q) 프로그래머스 코딩테스트 연습 GROUP BY 동명 동물 수 찾기
-- 조건: (1) 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 쓰인 횟수 조회
--       (2) 이름이 없는 동물은 집계에서 제외, 이름 순으로 조회

select NAME, count(NAME) from ANIMAL_INS 
where NAME is not null
group by NAME 
having count(NAME) >= 2
order by NAME;

