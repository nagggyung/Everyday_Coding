--Q) 프로그래머스 코딩테스트 연습 GROUP BY 고양이와 개는 몇 마리 있을까
-- 조건: (1) 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리 인지 조회
--       (2) 동물 타입 오름차순 정렬 

select ANIMAL_TYPE, count(ANIMAL_TYPE) as count 
from ANIMAL_INS 
group by ANIMAL_TYPE 
order by ANIMAL_TYPE;

/*
* group by 절: 
 일반적으로 특정 그룹(포지션 별, 팀별)별 데이터를 필요로 할 경우에 group by절을 그룹함수와 함께 이용한다.
 group by 절 이용시, select에 지정한 컬럼은 group by절에 모두 포함해야 한다.

* HAVING: group by절을 사용할 때 그룹들에 대한 제한 조건이 필요하여 사용하는 조건절

* 예시 *
 SELECT [DISTINCT] 컬럼명 [ALIAS명]
 FROM 테이블명
 [WHERE 조건식]
 [GROUP BY 컬럼이나 표현식
 HAVING 그룹조건식]
 ORDER BY 칼럼이나 표현식[ASC 또는 DESC];


출처: https://pliss.tistory.com/8 [Pliss]



작성 순서: WHERE -> GROUP BY -> ORDER BY
group by 까지만 해도 정답이 나오는데 왜 order by 까지 해야할까?
group by는 정렬을 보장해 주지는 않기 때문에, order by 를 써주는 것을 원칙으로 한다.
*/