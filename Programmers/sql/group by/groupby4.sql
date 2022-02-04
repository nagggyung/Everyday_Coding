--Q) 프로그래머스 코딩테스트 연습 GROUP BY 입양 시각 구하기(2)
-- 조건: (1) 0시 부터 23시까지 각 시간대 별로 입양이 몇건이나 발생했는지 조회
--       (2) 결과는 시간대 순으로 정렬

set @hour = -1;
select (@hour := @hour + 1) as HOUR,
    (select count(hour(DATETIME))
     from ANIMAL_OUTS
     where HOUR(DATETIME) = @hour) as COUNT 
from ANIMAL_OUTS
where @hour < 23;

/*
풀이: 
--> hour 변수를 -1로 선언하여서 22까지 +1 씩 더해주었다. 
  -1 부터 더했기 때문에 0부터 23까지 생성된다.
--> ANIMAL_OUTS 테이블에 있는 DATETIME 변수와 @hour 변수가 동일한 순간 카운트를 진행한다. 

*/

/*
개념: 
    * set:
    set 구문은 변수를 선언할 때 사용한다. 
    * 예시:
    set @ 변수이름 = 대입 값; 혹은 set @ 변수이름 := 대입 값;
    select @ 변수이름 := 대입 값;

    * set 이외의 명령문에서는 = 가 비교연산자로 취급되기 때문에 select 변수를 선언하고 
    값을 대입할 때는 :=를 사용한다.

*/