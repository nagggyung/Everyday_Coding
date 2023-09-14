--Q) 프로그래머스 코딩테스트 연습 selct 여러 기준으로 정렬하기 
-- 조건: (1) ANIMAL_ID, NAME, DATETIME 조회 
--       (2) 이름 사전순 정렬, 같은 이름 인 경우 날짜가 늦은 것 먼저 정렬


select ANIMAL_ID, NAME, DATETIME from ANIMAL_INS order by NAME asc, DATETIME desc;


/*
여러가지 컬럼을 정렬하기 위해서는 order by 후 가장 먼저 정렬할 컬럼명을 쓰고 콤마(,) 
다음으로 정렬할 컬림을 입력해 준다. 각 컬럼의 정렬기준은 서로 다를 수 있다. 

*** 다중 정렬 시, 왼쪽부터 순차적으로 정렬되기 때문에 순서를 고려해야 한다. (= 우선순위가 높은 순서대로 나열하자)

*/