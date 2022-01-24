--Q) 프로그래머스 코딩테스트 연습 selct 아픈 동물 찾기 
-- 조건: (1) ANIMAL_ID, NAME 조회 (2) INTAKE_CONDITION이 Sick 인 경우 조회


select ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION = 'Sick';

/*
* where 조건 절:
- Where 절을 사용하여 원하는 자료들로 결과를 제한 할 수 있다. 
- select [distinct/all] 컬럼명 from 테이블 명 where 조건식;
- where 절은 from 절 다음에 위치하며, 조건 식은 다음과 같이 구성된다. 
    --> 비교 연산자: =,>,>=,<,<=
    --> sql 연산자: between a and b, in (list), like '비교 문자열', is null
    --> 논리 연산자: and, or, not
    --> 부정 비교 연산자: !=(같지않다), ^=(같지않다), <>(같지않다), not 칼럼명 =, not 칼럼명 >
    --> 부정 sql 연산자: not between a and b, not in (list), is not null
*/