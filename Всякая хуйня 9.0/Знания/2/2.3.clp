(deftemplate student
(slot name) ; имя студента
(slot age) ; возраст
(slot year) ; год обучения (курс)
(slot spec) ; специализация
(slot aver_mark)) ; средний балл

(deffacts students
(student (name Karl) (age 22) (year 5) (spec "soft") (aver_mark 5.0))
(student (name Frederick) (age 21) (year 4) (spec "ai") (aver_mark 4.5))
(student (name Vladimir) (age 20) (year 4) (spec "hard") (aver_mark 5.0))
(student (name Iosif) (age 19) (year 2) (spec "hard") (aver_mark 4.7))
(student (name Yakov) (age 20) (year 3) (spec "hard") (aver_mark 4.0))
(student (name Felix) (age 18) (year 1) (spec "soft") (aver_mark 4.2))
(student (name Lev) (age 22) (year 4) (spec "ai") (aver_mark 3.0))
(student (name Mao) (age 22) (year 5) (spec "hard") (aver_mark 3.7))
(student (name Kim) (age 19) (year 2) (spec "ai") (aver_mark  3.9))
(student (name Ernst) (age 18) (year 1) (spec "soft") (aver_mark 3.3))
(student (name Michail) (age 23) (year 2) (spec "ai") (aver_mark 4.8))
)

(defrule r3 
(student (name ?n)
	(year ?y&:(integerp ?y))
	(aver_mark ?m&:(floatp ?m)))
(test (= ?y 2))
(test (>= ?m 4.5))
=>
(printout t "Student " ?n " have averange mark " ?m crlf))
