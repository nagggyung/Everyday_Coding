--Q) 프로그래머스 코딩테스트 연습 selct 어린 동물 찾기
-- 조건: (1) ANIMAL_ID, NAME 조회 (2) 어린 동물 조회

select ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION != 'Aged';