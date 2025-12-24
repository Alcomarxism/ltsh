(deffacts init (a)(b)(c)(d)(e))

(defrule r1 (declare (salience 5000))(a)(b)=> (assert (m)))
(defrule r2 (declare (salience 6000))(a)(c)=> (assert (n)))
(defrule r3 (declare (salience 5000))(b)(c)(d)=> (assert (p)))
(defrule r4 (declare (salience 6000))(a)(d)(c)=> (assert (r)))
(defrule r5 (declare (salience 6000))(m)(n)=> (assert (s)))
(defrule r6 (declare (salience 5000))(n)(p)(r)=> (assert (t)))