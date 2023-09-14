SELECT ANIMAL_TYPE,
CASE WHEN NAME IS NULL THEN 'No name' ELSE NAME END AS 'NAME',
SEX_UPON_INTAKE
FROM ANIMAL_INS



-- 기억! case when (column 조건) then (Result) else (column) end