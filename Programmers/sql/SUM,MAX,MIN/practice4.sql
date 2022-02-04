--Q) 프로그래머스 코딩테스트 연습 SUM,MAX,MIN 중복 제거하기 
-- 조건: NULL 과 중복된 이름 제외 보호소에 들어온 동물의 이름 수 

select count(distinct NAME) as count from ANIMAL_INS 
where NAME is not null;

/*
1. 'select distinct' statement is used to return only distinct (different) values.
2. It is not possible to test for NULL values with comparison operators, such as =, < , or <>
we will have to use 'is null' and 'is not null' operators instead.
*/