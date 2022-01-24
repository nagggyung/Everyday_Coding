--Q) 프로그래머스 코딩테스트 연습 selct 모든 레코드 조회
-- 조건: ANIMAL_ID 순으로 조회

select * from ANIMAL_INS order by ANIMAL_ID asc;

/*
* 모든 레코드 조회 시 select * from (table name);
* order by : 
  - sql 문장으로 조회된 데이터들을 다양한 목적에 맞게 특정 칼럼을 기준으로 정렬하여 출력한다.
  - ASC(Ascending): 조회한 데이터를 오름차순으로 정렬 (기본 default: 생략 가능)
  - DESC(Descending): 조회한 데이터를 내림차순으로 정렬  
*/